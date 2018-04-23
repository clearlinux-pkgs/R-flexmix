#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-flexmix
Version  : 2.3.14
Release  : 5
URL      : https://cran.r-project.org/src/contrib/flexmix_2.3-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/flexmix_2.3-14.tar.gz
Summary  : Flexible Mixture Modeling
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-SuppDists
Requires: R-actuar
Requires: R-diptest
Requires: R-ellipse
Requires: R-glmnet
Requires: R-lme4
Requires: R-modeltools
Requires: R-mvtnorm
BuildRequires : R-SuppDists
BuildRequires : R-actuar
BuildRequires : R-diptest
BuildRequires : R-ellipse
BuildRequires : R-glmnet
BuildRequires : R-lme4
BuildRequires : R-modeltools
BuildRequires : R-mvtnorm
BuildRequires : clr-R-helpers

%description
using the EM algorithm is implemented. The package provides the E-step
  and all data handling, while the M-step can be supplied by the user to
  easily define new models. Existing drivers implement mixtures of standard
  linear models, generalized linear models and model-based clustering.

%prep
%setup -q -c -n flexmix

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521225429

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521225429
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flexmix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flexmix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flexmix
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library flexmix|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/flexmix/CITATION
/usr/lib64/R/library/flexmix/DESCRIPTION
/usr/lib64/R/library/flexmix/INDEX
/usr/lib64/R/library/flexmix/Meta/Rd.rds
/usr/lib64/R/library/flexmix/Meta/data.rds
/usr/lib64/R/library/flexmix/Meta/features.rds
/usr/lib64/R/library/flexmix/Meta/hsearch.rds
/usr/lib64/R/library/flexmix/Meta/links.rds
/usr/lib64/R/library/flexmix/Meta/nsInfo.rds
/usr/lib64/R/library/flexmix/Meta/package.rds
/usr/lib64/R/library/flexmix/Meta/vignette.rds
/usr/lib64/R/library/flexmix/NAMESPACE
/usr/lib64/R/library/flexmix/NEWS.Rd
/usr/lib64/R/library/flexmix/R/flexmix
/usr/lib64/R/library/flexmix/R/flexmix.rdb
/usr/lib64/R/library/flexmix/R/flexmix.rdx
/usr/lib64/R/library/flexmix/data/BregFix.RData
/usr/lib64/R/library/flexmix/data/Mehta.RData
/usr/lib64/R/library/flexmix/data/NPreg.RData
/usr/lib64/R/library/flexmix/data/Nclus.RData
/usr/lib64/R/library/flexmix/data/NregFix.RData
/usr/lib64/R/library/flexmix/data/betablocker.RData
/usr/lib64/R/library/flexmix/data/bioChemists.RData
/usr/lib64/R/library/flexmix/data/candy.RData
/usr/lib64/R/library/flexmix/data/dmft.RData
/usr/lib64/R/library/flexmix/data/fabricfault.RData
/usr/lib64/R/library/flexmix/data/patent.RData
/usr/lib64/R/library/flexmix/data/salmonellaTA98.txt.gz
/usr/lib64/R/library/flexmix/data/seizure.RData
/usr/lib64/R/library/flexmix/data/tribolium.RData
/usr/lib64/R/library/flexmix/data/trypanosome.RData
/usr/lib64/R/library/flexmix/data/whiskey.RData
/usr/lib64/R/library/flexmix/doc/bootstrapping.R
/usr/lib64/R/library/flexmix/doc/bootstrapping.Rnw
/usr/lib64/R/library/flexmix/doc/bootstrapping.pdf
/usr/lib64/R/library/flexmix/doc/flexmix-intro.R
/usr/lib64/R/library/flexmix/doc/flexmix-intro.Rnw
/usr/lib64/R/library/flexmix/doc/flexmix-intro.pdf
/usr/lib64/R/library/flexmix/doc/index.html
/usr/lib64/R/library/flexmix/doc/mixture-regressions.R
/usr/lib64/R/library/flexmix/doc/mixture-regressions.Rnw
/usr/lib64/R/library/flexmix/doc/mixture-regressions.pdf
/usr/lib64/R/library/flexmix/doc/myConcomitant.R
/usr/lib64/R/library/flexmix/doc/mymclust.R
/usr/lib64/R/library/flexmix/doc/regression-examples.R
/usr/lib64/R/library/flexmix/doc/regression-examples.Rnw
/usr/lib64/R/library/flexmix/doc/regression-examples.pdf
/usr/lib64/R/library/flexmix/doc/ziglm.R
/usr/lib64/R/library/flexmix/help/AnIndex
/usr/lib64/R/library/flexmix/help/aliases.rds
/usr/lib64/R/library/flexmix/help/flexmix.rdb
/usr/lib64/R/library/flexmix/help/flexmix.rdx
/usr/lib64/R/library/flexmix/help/paths.rds
/usr/lib64/R/library/flexmix/html/00Index.html
/usr/lib64/R/library/flexmix/html/R.css
