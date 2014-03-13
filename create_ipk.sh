#!/bin/bash

D=$(pushd $(dirname $0) &> /dev/null; pwd; popd &> /dev/null)
P=${D}/ipkg.tmp.$$
B=${D}/ipkg.build.$$

pushd ${D} &> /dev/null
#VER=$(head -n 3 CHANGES.md | grep -i '## Version' | sed 's/^## Version \([[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+\)/\1/')
#VER=1.0
GITVER=git$(git log -1 --format="%ci" | awk -F" " '{ print $1 }' | tr -d "-")
PKG=${D}/enigma2-plugin-skins-infinityhd-nbox_${GITVER}_all.ipk
popd &> /dev/null

mkdir -p ${P}
mkdir -p ${P}/CONTROL
mkdir -p ${B}

cat > ${P}/CONTROL/control << EOF
Package: enigma2-plugin-skins-infinityhd-nbox
Version: ${GITVER}
Section: extra
Priority: optional
Architecture: all
Maintainer: herpoi <herpoi2006@gmail.com>
Description: InfinityHD-nbox skin for OpenPLi with inHDcontroler
Source: https://github.com/herpoi
Homepage: https://github.com/herpoi
EOF

cat > ${P}/CONTROL/postrm << EOF
#!/bin/sh
rm -R /usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler
rm -R /usr/share/enigma2/infinityHD-nbox
EOF

chmod +x ${P}/CONTROL/postrm
cp -rp ${D}/infinityHD-nbox/* ${P}/
#find ${P}/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/locale/ -name '*.po' -execdir msgfmt inHDcontroler.po -o inHDcontroler.mo \;
find ${P}/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/locale/ -name '*.po' -exec rm -f {} \;
rm -f ${P}/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/locale/inHDcontroler.pot

tar -C ${P} -czf ${B}/data.tar.gz . --exclude=CONTROL
tar -C ${P}/CONTROL -czf ${B}/control.tar.gz .

echo "2.0" > ${B}/debian-binary

cd ${B}
ls -la
ar -r ${PKG} ./debian-binary ./data.tar.gz ./control.tar.gz 
cd -

rm -rf ${P}
rm -rf ${B}
