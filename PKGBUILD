# Maintainer: @klock.mt

pkgname=tuned-next
pkgver=1.0.5.4
pkgrel=1
pkgdesc="Advanced power management profiles with TuneD, PPD replacement, and ZRAM optimization"
arch=('any')
url="https://gitlab.com/klock.mt/tuned-next" 
license=('GPL-3.0-or-later')
depends=('tuned' 'tuned-ppd' 'zram-generator' 'python')
source=("${pkgname}-${pkgver}.tar.gz::${url}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('bc734475600db8d74ebae7c950764ec5ae1ad1926ed9409fbde3ae5c15c5be5d')

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
