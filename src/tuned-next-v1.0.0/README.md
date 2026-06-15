# TuneD-Next 🚀

TuneD-Next is an advanced power management suite for modern Linux laptops. It seamlessly replaces the default `power-profiles-daemon` with the robust `tuned` and `tuned-ppd`, integrating directly with your desktop environment's (GNOME/KDE) quick settings.

*Note: This package was born as a Software Engineering university extension project. It is actively maintained, and I am eager to bring more updates, improvements, and refinements over time based on real-world usage and community feedback!*

## 🌟 Key Features

* **Modern Hardware Optimization:** Built to take advantage of relatively recent hardware technologies (like modern CPU p-states, dynamic boosting, and PCIe ASPM) to deliver maximum battery life or extreme performance without the bloat of legacy hardware settings.
* **Aggressive ZRAM Utilization:** In a world of RAM scarcity, TuneD-Next heavily abuses the capabilities of `zram-generator`. It automatically configures a highly efficient ZRAM block using the `zstd` algorithm, drastically improving system responsiveness during heavy multitasking and saving your SSD's lifespan.
* **Native GUI Integration:** Transition automatically between extreme performance on AC and smart power-saving on battery, all controlled seamlessly via your DE's standard power slider.

## ⚡ Included Profiles

### Battery Profiles (Automatic upon unplugging)
* **Ultra-Saver:** Absolute survival mode. Locks down CPU clocks, aggressively suspends PCIe/USB buses, and prioritizes battery life above all else.
* **Bat-Balanced:** The sweet spot for daily use. Fluid for web browsing and coding, with moderate power-saving measures that won't drop your Wi-Fi or cause audio stutters.
* **Bat-Performance:** High throughput for productivity on the go (compiling, running VMs), while strictly limiting GPU power to save battery since gaming isn't the focus here.

### AC / Mains Profiles (Automatic upon plugging in)
* **Ac-Performance:** Maximum desktop fluidity. Zero power saving, keeping the CPU and buses ready for instant I/O response.
* **Gaming-Mode:** Extreme performance focused on reducing input lag and frame-times. Locks CPU C-states to prevent micro-stutters and optimizes memory mapping for Proton/Wine gaming.
* **Kernel-Comp:** Throughput beast. Configures the kernel to use RAM as a massive I/O cache, dramatically speeding up heavy software compilation (`make -j`) while protecting the SSD from thousands of tiny writes.

## 🛠️ Installation

Once published to the AUR, you can install it using your favorite AUR helper:

```bash
yay -S tuned-next
```

**Post-Installation Setup:**
After the package manager finishes, you must run the included setup script to safely mask the old daemon and enable the new ones:

```bash
sudo tuned-next-setup
```

## 🤝 Contributing
Since this started as an academic project with long-term goals, contributions, issues, and pull requests are highly welcome. Let's make Linux power management better!