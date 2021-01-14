%define debug_package	%{nil}

%define tarname	msgpack

Summary:	MessagePack (de)serializer for Python
Name:		python-msgpack
Version:	1.0.2
Release:	1
# https://pypi.org/project/msgpack/
Source0:	https://files.pythonhosted.org/packages/source/m/msgpack/msgpack-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		http://msgpack.org/
BuildRequires:	python-cython
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)

%description
MessagePack is a binary-based efficient data interchange format that
is focused on high performance. It is like JSON, but very fast and
small.

%prep
%autosetup -p1 -n msgpack-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE=  python3 setup.py install --root=%{buildroot}

%files 
%doc COPYING README.md
%{py_platsitedir}/msgpack*
