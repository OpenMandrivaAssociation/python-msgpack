%define debug_package	%{nil}

%define tarname	msgpack

Summary:	MessagePack (de)serializer for Python
Name:		python-msgpack
Version:	1.1.2
Release:	2
# https://pypi.org/project/msgpack/
Source0:	https://files.pythonhosted.org/packages/source/m/msgpack/msgpack-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		https://msgpack.org/
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	pkgconfig(python3)
BuildSystem:	python

%description
MessagePack is a binary-based efficient data interchange format that
is focused on high performance. It is like JSON, but very fast and
small.

%files 
%doc COPYING README.md
%{py_platsitedir}/msgpack*
