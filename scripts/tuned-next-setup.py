#!/usr/bin/env python3

import os
import sys
import subprocess


def run_command(cmd: list[str], description: str, exit_on_fail: bool = False) -> None:
    print(f"[*] {description}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"    [FAIL] {result.stderr.strip()}")
        if exit_on_fail:
            print("[!] Rolling back...")
            rollback()
            sys.exit(1)
    else:
        print("    [OK]")


def rollback() -> None:
    run_command(["systemctl", "unmask", "power-profiles-daemon.service"], "Unmasking PPD")
    run_command(["systemctl", "enable", "--now", "power-profiles-daemon.service"], "Re-enabling PPD")
    run_command(["systemctl", "disable", "--now", "tuned.service"], "Disabling TuneD")
    run_command(["systemctl", "disable", "--now", "tuned-ppd.service"], "Disabling TuneD-PPD")
    run_command(["systemctl", "stop", "systemd-zram-setup@zram0.service"], "Stopping ZRAM")


def main() -> None:
    if os.geteuid() != 0:
        print("[!] Error: This script must be run as root (sudo).")
        sys.exit(1)

    print("=== Post-Installation Setup: TuneD-Next ===")

    run_command(["systemctl", "stop", "power-profiles-daemon.service"], "Stopping power-profiles-daemon")
    run_command(["systemctl", "mask", "power-profiles-daemon.service"], "Masking power-profiles-daemon")
    run_command(["cp", "-f", "/usr/share/tuned-next/ppd.conf", "/etc/tuned/ppd.conf"], "Injecting custom PPD configuration")

    run_command(["systemctl", "enable", "--now", "tuned.service"], "Enabling TuneD service", exit_on_fail=True)

    print("[*] Checking for GUI Integration (tuned-ppd)...")
    ppd_check = subprocess.run(['systemctl', 'list-unit-files', 'tuned-ppd.service'], capture_output=True, text=True)

    if 'tuned-ppd.service' in ppd_check.stdout:
        run_command(["systemctl", "enable", "--now", "tuned-ppd.service"], "Enabling TuneD-PPD (GUI Integration)", exit_on_fail=False)
    else:
        print("    [WARN] tuned-ppd.service not found. Skipping GUI integration.")

    run_command(["systemctl", "daemon-reload"], "Reloading systemd daemons")
    run_command(["systemctl", "restart", "systemd-zram-setup@zram0.service"], "Initializing ZRAM")

    print("\n[+] Setup complete! Power management is now handled by TuneD.")


if __name__ == "__main__":
    main()