%define 	module	geojson
Summary:	Encoder/decoder for simple GIS features
Name:		python-%{module}
Version:	1.0.1
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/geojson/geojson-1.0.1.tar.gz
# Source0-md5:  e71eadfa718684480b99f6be5269558a
URL:		http://pypi.python.org/pypi/geojson
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains:
- The reference implementation of the Python geo interface.
- Functions for encoding and decoding GeoJSON (http://geojson.org) formatted
  data.

Geojson provides geometry, feature, and collection classes, and supports
pickle-style dump and load of objects that provide the lab's Python geo
interface. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt DEPENDENCIES.txt FAQ.txt GeoInterface.txt README.txt VERSION.txt
%{py_sitescriptdir}/geojson/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/geojson-*.egg-info
%endif
