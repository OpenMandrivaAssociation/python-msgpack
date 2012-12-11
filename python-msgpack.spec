%define tarname	msgpack-python
%define name	python-msgpack
%define version 0.2.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release	%rel
%endif

Summary:	MessagePack (de)serializer for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/m/%{tarname}/%{tarname}-%{version}.tar.gz
Patch0:		egg-info-0.2.0.patch
License:	Apache License
Group:		Development/Python
Url:		http://msgpack.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-cython
BuildRequires:	python-setuptools

%description
MessagePack is a binary-based efficient data interchange format that
is focused on high performance. It is like JSON, but very fast and
small.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p0

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc COPYING README.rst
%py_platsitedir/msgpack*


%changelog
* Thu Aug 09 2012 Lev Givon <lev@mandriva.org> 0.2.0-1
+ Revision: 813601
- imported package python-msgpack

