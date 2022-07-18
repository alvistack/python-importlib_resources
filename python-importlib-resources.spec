%global debug_package %{nil}

Name: python-importlib-resources
Epoch: 100
Version: 5.7.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Read resources from Python packages
License: Apache-2.0
URL: https://github.com/python/importlib_resources/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
importlib_resources is a backport of Python 3.7's standard library
importlib.resources module for 3.4 through 3.6. Users of Python 3.7 and
beyond should use the standard library module, since for these versions,
importlib_resources just delegates to that module.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-importlib-resources
Summary: Read resources from Python packages
Requires: python3
Provides: python3-importlib-resources = %{epoch}:%{version}-%{release}
Provides: python3dist(importlib-resources) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-importlib-resources = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(importlib-resources) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-importlib-resources = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(importlib-resources) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-importlib-resources
importlib_resources is a backport of Python 3.7's standard library
importlib.resources module for 3.4 through 3.6. Users of Python 3.7 and
beyond should use the standard library module, since for these versions,
importlib_resources just delegates to that module.

%files -n python%{python3_version_nodots}-importlib-resources
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-importlib-resources
Summary: Read resources from Python packages
Requires: python3
Provides: python3-importlib-resources = %{epoch}:%{version}-%{release}
Provides: python3dist(importlib-resources) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-importlib-resources = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(importlib-resources) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-importlib-resources = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(importlib-resources) = %{epoch}:%{version}-%{release}

%description -n python3-importlib-resources
importlib_resources is a backport of Python 3.7's standard library
importlib.resources module for 3.4 through 3.6. Users of Python 3.7 and
beyond should use the standard library module, since for these versions,
importlib_resources just delegates to that module.

%files -n python3-importlib-resources
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
