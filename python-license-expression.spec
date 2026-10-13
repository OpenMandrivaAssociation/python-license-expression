Name:		python-license-expression
Version:	30.4.4
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/l/license-expression/license_expression-%{version}.tar.gz
Summary:	Parse and normalize SPDX license expressions
URL:		https://pypi.org/project/license-expression/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(boolean.py)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%build -p
# No git tag in the sdist, so setuptools-scm would otherwise emit 0.0.0.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%description
license-expression is a comprehensive utility library to parse, compare, simplify and normalize license expressions (such as SPDX license expressions) using boolean logic.

%files
%{py_sitedir}/license_expression
%{py_sitedir}/license_expression-*.*-info
