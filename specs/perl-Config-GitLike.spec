Name:           perl-Config-GitLike
Version:        1.16
Release:        1%{?dist}
Summary:        Git-compatible config file parsing
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-GitLike/
Source0:        http://www.cpan.org/authors/id/A/AL/ALEXMV/Config-GitLike-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Moo)
Requires:       perl(MooX::Types::MooseLike)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

%prep
%setup -q -n Config-GitLike-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.16-1
- Specfile autogenerated by cpanspec 1.78.
