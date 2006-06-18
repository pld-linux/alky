%define	_snap 20060619
%define	_rev 28
%define	_rel 0.1
Summary:	alky
Name:		alky
Version:	0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{_snap}.%{_rev}.tar.bz2
# Source0-md5:	fae86cf47c03718c6b9a3ef875718404
URL:		http://www.alkyproject.com/
ExclusiveOs:	MacOSX Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alky (pronounced "AL-KEE") is a tool that allows you to convert a
Windows executable to a Mac OS X or Linux binary. We are focused on
high-end gaming at the moment, though we will support other
applications in the future. Our binary translation layer is already
working fully for OS X and Linux support is in progress. Of course,
Windows applications use a very different set of libraries from Linux
or OS X applications so we are also working on a library called
LibAlky that will provide those Windows libraries to the application.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
