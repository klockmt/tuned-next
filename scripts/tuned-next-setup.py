#!/usr/bin/env python3
import os
import subprocess
import sys

def run_command(command, description, exit_on_fail=False):
    print(f"[*] {description}...")
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("    [ OK ] Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"    [ ERROR ] Failed to execute: {' '.join(command)}")
        print(f"    Details: {e.stderr.decode().strip()}")
        if exit_on_fail:
            rollback()
        return False

def rollback():
    print("\n[!] Critical failure detected. Initiating rollback to maintain system stability...")
    run_command(["systemctl", "unmask", "power-profiles-daemon.service"], "Unmasking power-profiles-daemon")
    run_command(["systemctl", "start", "power-profiles-daemon.service"], "Restarting power-profiles-daemon")
    print("[-] Rollback complete. Original state restored. TuneD-Next setup aborted.")
    sys.exit(1)

def main():
    if os.geteuid() != 0:
        print("[!] Error: This script must be run as root (sudo).")
        sys.exit(1)

    print("=== Post-Installation Setup: TuneD-Next ===")

    # Stop and mask the original PPD
    run_command(["systemctl", "stop", "power-profiles-daemon.service"], "Stopping power-profiles-daemon (if active)")
    run_command(["systemctl", "mask", "power-profiles-daemon.service"], "Masking power-profiles-daemon")
    
    # Try to start TuneD. If it fails, rollback is triggered automatically.
    run_command(["systemctl", "enable", "--now", "tuned.service"], "Enabling and starting TuneD service", exit_on_fail=True)
    
    # Check if tuned-ppd exists before trying to enable it (Professor's Code Review)
    print("[*] Checking for GUI Integration (tuned-ppd)...")
    ppd_check = subprocess.run(['systemctl', 'list-unit-files', 'tuned-ppd.service'], capture_output=True, text=True)
    
    if 'tuned-ppd.service' in ppd_check.stdout:
        run_command(["systemctl", "enable", "--now", "tuned-ppd.service"], "Enabling and starting TuneD-PPD (GUI Integration)", exit_on_fail=False)
    else:
        print("    [ WARN ] tuned-ppd.service not found. Skipping GNOME/KDE GUI integration.")
    
    # ZRAM setup is independent, a failure here shouldn't break the power profiles
    run_command(["systemctl", "daemon-reload"], "Reloading systemd daemons")
    run_command(["systemctl", "restart", "systemd-zram-setup@zram0.service"], "Initializing optimized ZRAM module")

    print("\n[+] Setup complete! Power management is now handled by TuneD.")

if __name__ == "__main__":
    main()