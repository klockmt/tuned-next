# Maintainer: @klock.mt

pkgname=tuned-next
pkgver=1.0.6
pkgrel=1
pkgdesc="Advanced power management profiles with TuneD, PPD replacement, and ZRAM optimization"
arch=('any')
url="https://gitlab.com/klock.mt/tuned-next" 
license=('GPL-3.0-or-later')
depends=('tuned' 'tuned-ppd' 'zram-generator' 'python')
source=("${pkgname}-${pkgver}.tar.gz::${url}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('8fae3f3ab3432b092a177cd31cea32527aea981f1681eaa20b32f7e898115eee')

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
