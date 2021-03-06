#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyicu
Version  : 2.9
Release  : 34
URL      : https://files.pythonhosted.org/packages/11/76/9256430e729ad0dd4675a15a7bf0555b9085d1bea36083b9a1b095602f23/PyICU-2.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/76/9256430e729ad0dd4675a15a7bf0555b9085d1bea36083b9a1b095602f23/PyICU-2.9.tar.gz
Summary  : Python extension wrapping the ICU C++ API
Group    : Development/Tools
License  : MIT
Requires: pypi-pyicu-filemap = %{version}-%{release}
Requires: pypi-pyicu-lib = %{version}-%{release}
Requires: pypi-pyicu-license = %{version}-%{release}
Requires: pypi-pyicu-python = %{version}-%{release}
Requires: pypi-pyicu-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
## Welcome
Welcome to PyICU, a Python extension wrapping the ICU C++ libraries.
ICU stands for "International Components for Unicode".
These are the i18n libraries of the Unicode Consortium.
They implement much of the Unicode Standard,
many of its companion Unicode Technical Standards,
and much of Unicode CLDR.

%package filemap
Summary: filemap components for the pypi-pyicu package.
Group: Default

%description filemap
filemap components for the pypi-pyicu package.


%package lib
Summary: lib components for the pypi-pyicu package.
Group: Libraries
Requires: pypi-pyicu-license = %{version}-%{release}
Requires: pypi-pyicu-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pyicu package.


%package license
Summary: license components for the pypi-pyicu package.
Group: Default

%description license
license components for the pypi-pyicu package.


%package python
Summary: python components for the pypi-pyicu package.
Group: Default
Requires: pypi-pyicu-python3 = %{version}-%{release}

%description python
python components for the pypi-pyicu package.


%package python3
Summary: python3 components for the pypi-pyicu package.
Group: Default
Requires: pypi-pyicu-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pyicu)

%description python3
python3 components for the pypi-pyicu package.


%prep
%setup -q -n PyICU-2.9
cd %{_builddir}/PyICU-2.9
pushd ..
cp -a PyICU-2.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656398361
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyicu
cp %{_builddir}/PyICU-2.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyicu/120b05ff6be69ae17ed45de923f7ce2ca3471f18
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pyicu

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyicu/120b05ff6be69ae17ed45de923f7ce2ca3471f18

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
