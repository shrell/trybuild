Name:           perl-CPAN-Meta
Version:        2.143240
Release:        1%{?dist}
Summary:        Distribution metadata for a CPAN dist
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.008
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::PP) >= 2.27200
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4414
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.88
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(CPAN::Meta::YAML) >= 0.008
Requires:       perl(JSON::PP) >= 2.27200
Requires:       perl(Parse::CPAN::Meta) >= 1.4414
Requires:       perl(version) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Software distributions released to the CPAN include a META.json or, for
older distributions, META.yml, which describes the distribution, its
contents, and the requirements for building and installing the
distribution. The data structure stored in the META.json file is described
in CPAN::Meta::Spec.

%prep
%setup -q -n CPAN-Meta-%{version}

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
%doc Changes CONTRIBUTING cpanfile dist.ini LICENSE META.json perlcritic.rc README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 2.143240-1
- Specfile autogenerated by cpanspec 1.78.
