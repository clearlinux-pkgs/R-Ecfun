#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Ecfun
Version  : 0.2.0
Release  : 20
URL      : https://cran.r-project.org/src/contrib/Ecfun_0.2-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Ecfun_0.2-0.tar.gz
Summary  : Functions for Ecdat
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DescTools
Requires: R-EnvStats
Requires: R-RCurl
Requires: R-TeachingDemos
Requires: R-XML
Requires: R-drc
Requires: R-fda
Requires: R-gdata
Requires: R-jpeg
Requires: R-tis
Requires: R-xml2
BuildRequires : R-DescTools
BuildRequires : R-EnvStats
BuildRequires : R-RCurl
BuildRequires : R-TeachingDemos
BuildRequires : R-XML
BuildRequires : R-drc
BuildRequires : R-fda
BuildRequires : R-gdata
BuildRequires : R-jpeg
BuildRequires : R-tis
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
manipulate, plot and analyze those and similar data sets.

%prep
%setup -q -c -n Ecfun

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551140195

%install
export SOURCE_DATE_EPOCH=1551140195
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Ecfun
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Ecfun
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Ecfun
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Ecfun|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/Ecfun/R/Ecfun
/usr/lib64/R/library/Ecfun/R/Ecfun.rdb
/usr/lib64/R/library/Ecfun/R/Ecfun.rdx
/usr/lib64/R/library/Ecfun/doc/index.html
/usr/lib64/R/library/Ecfun/doc/nuclearArmageddon.Rmd
/usr/lib64/R/library/Ecfun/doc/nuclearArmageddon.html
/usr/lib64/R/library/Ecfun/help/AnIndex
/usr/lib64/R/library/Ecfun/help/Ecfun.rdb
/usr/lib64/R/library/Ecfun/help/Ecfun.rdx
/usr/lib64/R/library/Ecfun/help/aliases.rds
/usr/lib64/R/library/Ecfun/help/paths.rds
/usr/lib64/R/library/Ecfun/html/00Index.html
/usr/lib64/R/library/Ecfun/html/R.css
