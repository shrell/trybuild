Name:           perl-Module-Build
Version:        0.4211
Release:        2%{?dist}
Summary:        Build and install Perl modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Build/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008000
BuildRequires:  perl(CPAN::Meta) >= 2.142060
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.003
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::Install) >= 0.3
BuildRequires:  perl(ExtUtils::Manifest) >= 1.54
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Metadata) >= 1.000002
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4401
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(Test::Harness) >= 3.16
BuildRequires:  perl(Test::More) >= 0.49
BuildRequires:  perl(version) >= 0.87
Requires:       perl(CPAN::Meta) >= 2.142060
Requires:       perl(ExtUtils::CBuilder) >= 0.27
Requires:       perl(ExtUtils::Install) >= 0.3
Requires:       perl(ExtUtils::Manifest) >= 1.54
Requires:       perl(ExtUtils::Mkbootstrap)
Requires:       perl(ExtUtils::ParseXS) >= 2.21
Requires:       perl(Module::Metadata) >= 1.000002
Requires:       perl(Perl::OSType) >= 1
Requires:       perl(Test::Harness)
Requires:       perl(version) >= 0.87
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through subclassing in a
much more straightforward way than with MakeMaker. It also does not require
a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way.

%prep
%setup -q -n Module-Build-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes contrib LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%doc %{_mandir}/man1/config_data.1*
%{_bindir}/config_data

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.4211-2
- ajout des lignes de %files

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.4211-1
- Specfile autogenerated by cpanspec 1.78.
