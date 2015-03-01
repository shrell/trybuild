Name:           perl-Module-Metadata
Version:        1.000026
Release:        1%{?dist}
Summary:        Gather package and POD information from perl module files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Metadata/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/Module-Metadata-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(version) >= 0.87
Requires:       perl(version) >= 0.87
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a standard way to gather metadata about a .pm file
through (mostly) static analysis and (some) code execution. When
determining the version of a module, the $VERSION assignment is evaled, as
is traditional in the CPAN toolchain.

%prep
%setup -q -n Module-Metadata-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.000026-1
- Specfile autogenerated by cpanspec 1.78.
