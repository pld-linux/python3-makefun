# TODO: run mkdocs
#
# Conditional build:
%bcond_with	doc	# mkdocs documentation
%bcond_without	tests	# unit tests

Summary:	Small library to dynamically create Python functions
Summary(pl.UTF-8):	Mała biblioteka do dynamicznego tworzenia funkcji w Pythonie
Name:		python3-makefun
Version:	1.16.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/makefun/
Source0:	https://files.pythonhosted.org/packages/source/m/makefun/makefun-%{version}.tar.gz
# Source0-md5:	1d836c3a07619fcc951b1ea02ceab179
URL:		https://pypi.org/project/makefun/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools >= 1:39.2
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-asyncio
%endif
%if %{with doc}
BuildRequires:	python3-mkdocs
BuildRequires:	python3-mkdocs-material
BuildRequires:	python3-pygments
BuildRequires:	python3-pymdown-extensions
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small library to dynamically create Python functions.

%description -l pl.UTF-8
Mała biblioteka do dynamicznego tworzenia funkcji w Pythonie.

%prep
%setup -q -n makefun-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md docs/*.md
%{py3_sitescriptdir}/makefun
%{py3_sitescriptdir}/makefun-%{version}-py*.egg-info
