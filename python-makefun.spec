#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Small library to dynamically create Python functions
Summary(pl.UTF-8):	Mała biblioteka do dynamicznego tworzenia funkcji w Pythonie
Name:		python-makefun
Version:	1.15.6
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/makefun/
Source0:	https://files.pythonhosted.org/packages/source/m/makefun/makefun-%{version}.tar.gz
# Source0-md5:	5ceb672609f44b348ca3370d995e74f8
URL:		https://pypi.org/project/makefun/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pytest-runner
BuildRequires:	python-setuptools >= 1:39.2
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-funcsigs
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools >= 1:39.2
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small library to dynamically create Python functions.

%description -l pl.UTF-8
Mała biblioteka do dynamicznego tworzenia funkcji w Pythonie.

%package -n python3-makefun
Summary:	Small library to dynamically create Python functions
Summary(pl.UTF-8):	Mała biblioteka do dynamicznego tworzenia funkcji w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-makefun
Small library to dynamically create Python functions.

%description -n python3-makefun -l pl.UTF-8
Mała biblioteka do dynamicznego tworzenia funkcji w Pythonie.

%prep
%setup -q -n makefun-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md docs/*.md
%{py_sitescriptdir}/makefun
%{py_sitescriptdir}/makefun-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-makefun
%defattr(644,root,root,755)
%doc LICENSE README.md docs/*.md
%{py3_sitescriptdir}/makefun
%{py3_sitescriptdir}/makefun-%{version}-py*.egg-info
%endif
