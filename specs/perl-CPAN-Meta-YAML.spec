Name:           perl-CPAN-Meta-YAML
Version:        0.012
Release:        1%{?dist}
Summary:        Read and write a subset of YAML for CPAN Meta files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Meta-YAML/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-YAML-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008001
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.99
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like META.yml and MYMETA.yml. It
should not be used for any other general YAML parsing or generation task.

%prep
%setup -q -n CPAN-Meta-YAML-%{version}

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
%doc Changes cpanfile LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.012-1
- Specfile autogenerated by cpanspec 1.78.
