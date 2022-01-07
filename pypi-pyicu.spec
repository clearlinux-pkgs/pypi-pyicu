#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyicu
Version  : 2.8
Release  : 30
URL      : https://files.pythonhosted.org/packages/1a/b6/ede5f19d79655898162afa778d2f38cbde04b0cccb8737c649cd5d3d38e0/PyICU-2.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/1a/b6/ede5f19d79655898162afa778d2f38cbde04b0cccb8737c649cd5d3d38e0/PyICU-2.8.tar.gz
Summary  : Python extension wrapping the ICU C++ API
Group    : Development/Tools
License  : MIT
Requires: pypi-pyicu-license = %{version}-%{release}
Requires: pypi-pyicu-python = %{version}-%{release}
Requires: pypi-pyicu-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
Provides: pyicu

%description
## Welcome
Welcome to PyICU, a Python extension wrapping the ICU C++ libraries.
ICU stands for "International Components for Unicode".
These are the i18n libraries of the Unicode Consortium.
They implement much of the Unicode Standard,
many of its companion Unicode Technical Standards,
and much of Unicode CLDR.

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
Requires: python3-core
Provides: pypi(pyicu)

%description python3
python3 components for the pypi-pyicu package.


%prep
%setup -q -n PyICU-2.8
cd %{_builddir}/PyICU-2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641569781
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyicu
cp %{_builddir}/PyICU-2.8/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyicu/30410e52eb79243849038655af921b51845dfed4
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyicu/30410e52eb79243849038655af921b51845dfed4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
