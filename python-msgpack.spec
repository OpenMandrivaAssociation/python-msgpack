%define debug_package	%{nil}

%define tarname	msgpack

Summary:	MessagePack (de)serializer for Python
Name:		python-msgpack
Version:	0.6.1
Release:	1
# https://pypi.org/project/msgpack/
Source0:	https://files.pythonhosted.org/packages/source/m/msgpack/msgpack-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		http://msgpack.org/
BuildRequires:	python-cython
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)

%description
MessagePack is a binary-based efficient data interchange format that
is focused on high performance. It is like JSON, but very fast and
small.

%package -n python2-msgpack
Summary: %{summary} / Python2

%description -n python2-msgpack
MessagePack is a binary-based efficient data interchange format that
is focused on high performance. It is like JSON, but very fast and
small.


%prep
%setup -qc
mv %{tarname}-%{version} python2
cp -a python2 python3

%build
pushd python2
python2 setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE=  python2 setup.py install --root=%{buildroot}
popd

pushd python3
PYTHONDONTWRITEBYTECODE=  python3 setup.py install --root=%{buildroot}
popd

%files 
%doc python3/COPYING python3/README.rst
%{py_platsitedir}/msgpack*

%files -n python2-msgpack
%doc python2/COPYING python2/README.rst
%{py2_platsitedir}/msgpack*

