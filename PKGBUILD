# Maintainer: @klock.mt

pkgname=tuned-next
pkgver=1.0.0
pkgrel=1
pkgdesc="Advanced power management profiles with TuneD, PPD replacement, and ZRAM optimization"
arch=('any')
url="https://gitlab.com/KlockMt/tuned-next" 
license=('GPL-3.0-or-later')
depends=('tuned' 'zram-generator' 'python')
conflicts=('power-profiles-daemon')
provides=('power-profiles-daemon')
source=("${pkgname}-${pkgver}.tar.gz::${url}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('bdc4618140f61b6251bdb139a3a763583d72dc5f13360f222ae7b0beeb055b03')

package() {
    cd "${srcdir}/${pkgname}-v${pkgver}"

    for profile in Ultra-Saver Bat-Balanced Bat-Performance Ac-Performance Gaming-mode Kernel-comp; do

        install -dm755 "${pkgdir}/usr/lib/tuned/${profile}"

        install -Dm644 "profiles/${profile}/tuned.conf" "${pkgdir}/usr/lib/tuned/${profile}/tuned.conf"

    done

    install -Dm644 "config/ppd.conf" "${pkgdir}/etc/tuned/ppd.conf"

    install -Dm644 "config/tuned-next.conf" "${pkgdir}/etc/systemd/zram-generator.conf.d/tuned-next.conf"

    install -Dm755 "scripts/tuned-next-setup.py" "${pkgdir}/usr/bin/tuned-next-setup"
}
