Name:		python-license-expression
Version:	30.4.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/license-expression/license_expression-%{version}.tar.gz
Summary:	license-expression is a comprehensive utility library to parse, compare, simplify and normalize license expressions (such as SPDX license expressions) using boolean logic.
URL:		https://pypi.org/project/license-expression/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
license-expression is a comprehensive utility library to parse, compare, simplify and normalize license expressions (such as SPDX license expressions) using boolean logic.

%files
%{py_sitedir}/license_expression
%{py_sitedir}/license_expression-*.*-info
