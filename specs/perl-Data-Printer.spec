Name:           perl-Data-Printer
Version:        0.35
Release:        2%{?dist}
Summary:        Data::Printer Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Printer/
Source0:        http://www.cpan.org/authors/id/G/GA/GARU/Data-Printer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir) >= 0.91
BuildRequires:  perl(Package::Stash) >= 0.3
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(Term::ANSIColor) >= 3.00
Requires:       perl(Clone::PP)
Requires:       perl(File::HomeDir) >= 0.91
Requires:       perl(Package::Stash) >= 0.3
Requires:       perl(Sort::Naturally)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(version) >= 0.77
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Term::ANSIColor) >= 3.00

%description
Data::Printer is a Perl module to pretty-print Perl data structures and
objects in full color. It is meant to display variables on screen, properly
formatted to be inspected by a human.

%prep
%setup -q -n Data-Printer-%{version}

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
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.35-2
- Ajoute la dépendance sur Term::ANSIColor >= 3.00

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.35-1
- Specfile autogenerated by cpanspec 1.78.
