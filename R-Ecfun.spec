#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Ecfun
Version  : 0.3.2
Release  : 58
URL      : https://cran.r-project.org/src/contrib/Ecfun_0.3-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Ecfun_0.3-2.tar.gz
Summary  : Functions for 'Ecdat'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-BMA
Requires: R-TeachingDemos
Requires: R-fda
Requires: R-jpeg
Requires: R-mvtnorm
Requires: R-rvest
Requires: R-stringi
Requires: R-tis
Requires: R-xml2
BuildRequires : R-BMA
BuildRequires : R-TeachingDemos
BuildRequires : R-fda
BuildRequires : R-jpeg
BuildRequires : R-mvtnorm
BuildRequires : R-rvest
BuildRequires : R-stringi
BuildRequires : R-tis
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
data sets in 'Ecdat' and to create, manipulate, 
    plot, and analyze those and similar data sets.

%prep
%setup -q -n Ecfun
cd %{_builddir}/Ecfun

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665424656

%install
export SOURCE_DATE_EPOCH=1665424656
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Ecfun/DESCRIPTION
/usr/lib64/R/library/Ecfun/INDEX
/usr/lib64/R/library/Ecfun/Meta/Rd.rds
/usr/lib64/R/library/Ecfun/Meta/features.rds
/usr/lib64/R/library/Ecfun/Meta/hsearch.rds
/usr/lib64/R/library/Ecfun/Meta/links.rds
/usr/lib64/R/library/Ecfun/Meta/nsInfo.rds
/usr/lib64/R/library/Ecfun/Meta/package.rds
/usr/lib64/R/library/Ecfun/Meta/vignette.rds
/usr/lib64/R/library/Ecfun/NAMESPACE
/usr/lib64/R/library/Ecfun/NEWS.md
/usr/lib64/R/library/Ecfun/R/Ecfun
/usr/lib64/R/library/Ecfun/R/Ecfun.rdb
/usr/lib64/R/library/Ecfun/R/Ecfun.rdx
/usr/lib64/R/library/Ecfun/WORDLIST
/usr/lib64/R/library/Ecfun/doc/UpdatingUSGDPpresidents.R
/usr/lib64/R/library/Ecfun/doc/UpdatingUSGDPpresidents.Rmd
/usr/lib64/R/library/Ecfun/doc/UpdatingUSGDPpresidents.html
/usr/lib64/R/library/Ecfun/doc/index.html
/usr/lib64/R/library/Ecfun/doc/nuclearArmageddon.R
/usr/lib64/R/library/Ecfun/doc/nuclearArmageddon.Rmd
/usr/lib64/R/library/Ecfun/doc/nuclearArmageddon.html
/usr/lib64/R/library/Ecfun/doc/updateOCC1950.R
/usr/lib64/R/library/Ecfun/doc/updateOCC1950.Rmd
/usr/lib64/R/library/Ecfun/doc/updateOCC1950.html
/usr/lib64/R/library/Ecfun/doc/update_nuclearWeaponStates.R
/usr/lib64/R/library/Ecfun/doc/update_nuclearWeaponStates.Rmd
/usr/lib64/R/library/Ecfun/doc/update_nuclearWeaponStates.html
/usr/lib64/R/library/Ecfun/help/AnIndex
/usr/lib64/R/library/Ecfun/help/Ecfun.rdb
/usr/lib64/R/library/Ecfun/help/Ecfun.rdx
/usr/lib64/R/library/Ecfun/help/aliases.rds
/usr/lib64/R/library/Ecfun/help/paths.rds
/usr/lib64/R/library/Ecfun/html/00Index.html
/usr/lib64/R/library/Ecfun/html/R.css
