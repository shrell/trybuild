%define mybuilddir %{_builddir}/%{name}-%{version}-root

Summary:	a headless WebKit with JavaScript API
Name:		phantomjs
Version:	2.1.1
License:	BSD
Release:	5
Packager:	Jean-Michel Rey <vreb87@gmail.com>
Source0:    https://bitbucket.org/ariya/phantomjs/downloads/%{name}-%{version}-linux-i686.tar.bz2
Source1:    https://bitbucket.org/ariya/phantomjs/downloads/%{name}-%{version}-linux-x86_64.tar.bz2
Requires:   fontconfig

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%ifarch x86_64
%setup -T -b 1 -n %{name}-%{version}-linux-x86_64
%else
%setup -T -b 0 -n %{name}-%{version}-linux-i686
%endif

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cp bin/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/%{name}

%changelog

* Thu Mar 8 2016 Jean-Michel Rey <vreb87@gmail.com> 2.1.1-5
- packaging JMR

* Thu Mar 8 2016 Jean-Michel Rey <vreb87@gmail.com> 2.1.1-4
- packaging JMR

* Thu Mar 8 2016 Jean-Michel Rey <vreb87@gmail.com> 2.1.1-3
- packaging JMR

* Thu Mar 8 2016 Jean-Michel Rey <vreb87@gmail.com> 2.1.1-2
- packaging JMR

* Thu Mar 8 2016 Jean-Michel Rey <vreb87@gmail.com> 2.1.1-1
- packaging JMR