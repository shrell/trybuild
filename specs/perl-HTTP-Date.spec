Name:           perl-HTTP-Date
Version:        6.02
Release:        3%{?dist}
Summary:        Date conversion routines
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Date/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Date-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006002
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Time::Zone)
Requires:       perl(Time::Zone)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides functions that deal the date formats used by the HTTP
protocol (and then some more). Only the first two functions, time2str() and
str2time(), are exported by default.

%prep
%setup -q -n HTTP-Date-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=site
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

#suppression des documentations
find $RPM_BUILD_ROOT -type f -name "*.3pm" -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_sitelib}/*
#%{_mandir}/man3/*

%changelog
* Fri Jul 29 2016 Jean-Michel REY <vreb87@gmail.com> 6.02-3
- passe dans le dossier perl/site

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 6.02-2
- supprime les fichiers de manuel, en conflit avec perl-libwww-perl-5.833-2.el6.noarch

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 6.02-1
- Specfile autogenerated by cpanspec 1.78.
