# Maintainer: @klock.mt

pkgname=tuned-next
pkgver=1.0.4.1
pkgrel=1
pkgdesc="Advanced power management profiles with TuneD, PPD replacement, and ZRAM optimization"
arch=('any')
url="https://gitlab.com/klock.mt/tuned-next" 
license=('GPL-3.0-or-later')
depends=('tuned' 'tuned-ppd' 'zram-generator' 'python')
source=("${pkgname}-${pkgver}.tar.gz::${url}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('beecc31290556cf323a1864d2c08428ca069eec7253538dcb0cccc46e7b86d36')

package() {
    cd "${srcdir}/${pkgname}-v${pkgver}"

    for profile in Ultra-Saver Bat-Balanced Bat-Performance Ac-Performance Gaming-mode Kernel-comp; do
        install -dm755 "${pkgdir}/etc/tuned/profiles/${profile}"
        install -Dm644 "profiles/${profile}/tuned.conf" "${pkgdir}/etc/tuned/profiles/${profile}/tuned.conf"
    done

    install -Dm644 "config/ppd.conf" "${pkgdir}/usr/share/tuned-next/ppd.conf"
    
    install -Dm644 "config/tuned-next.conf" "${pkgdir}/etc/systemd/zram-generator.conf.d/tuned-next.conf"
    install -Dm755 "scripts/tuned-next-setup.py" "${pkgdir}/usr/bin/tuned-next-setup"
}
