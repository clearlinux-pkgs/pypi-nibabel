#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nibabel
Version  : 4.0.2
Release  : 15
URL      : https://github.com/nipy/nibabel/archive/4.0.2/nibabel-4.0.2.tar.gz
Source0  : https://github.com/nipy/nibabel/archive/4.0.2/nibabel-4.0.2.tar.gz
Summary  : Access a multitude of neuroimaging data formats
Group    : Development/Tools
License  : MIT
Requires: pypi-nibabel-bin = %{version}-%{release}
Requires: pypi-nibabel-license = %{version}-%{release}
Requires: pypi-nibabel-python = %{version}-%{release}
Requires: pypi-nibabel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(packaging)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
These files implement NiBabel CI for GitHub actions.
The testing logic is implemented in tools/ci/*.sh, and these files adapt
the generic logic to the details of GH.

%package bin
Summary: bin components for the pypi-nibabel package.
Group: Binaries
Requires: pypi-nibabel-license = %{version}-%{release}

%description bin
bin components for the pypi-nibabel package.


%package license
Summary: license components for the pypi-nibabel package.
Group: Default

%description license
license components for the pypi-nibabel package.


%package python
Summary: python components for the pypi-nibabel package.
Group: Default
Requires: pypi-nibabel-python3 = %{version}-%{release}

%description python
python components for the pypi-nibabel package.


%package python3
Summary: python3 components for the pypi-nibabel package.
Group: Default
Requires: python3-core
Provides: pypi(nibabel)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-nibabel package.


%prep
%setup -q -n nibabel-4.0.2
cd %{_builddir}/nibabel-4.0.2
pushd ..
cp -a nibabel-4.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672292900
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nibabel
cp %{_builddir}/nibabel-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-nibabel/9c0c415abfe603c9591ab70fa55f3c0f10cab417 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nib-conform
/usr/bin/nib-convert
/usr/bin/nib-dicomfs
/usr/bin/nib-diff
/usr/bin/nib-ls
/usr/bin/nib-nifti-dx
/usr/bin/nib-roi
/usr/bin/nib-stats
/usr/bin/nib-tck2trk
/usr/bin/nib-trk2tck
/usr/bin/parrec2nii

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nibabel/9c0c415abfe603c9591ab70fa55f3c0f10cab417

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
