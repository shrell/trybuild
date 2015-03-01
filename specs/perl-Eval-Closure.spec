Name:           perl-Eval-Closure
Version:        0.12
Release:        1%{?dist}
Summary:        Safely and cleanly create closures via string eval
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Eval-Closure/
Source0:        http://www.cpan.org/authors/id/D/DO/DOY/Eval-Closure-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Devel::LexAlias) >= 0.05
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Devel::LexAlias) >= 0.05
Requires:       perl(Perl::Tidy)
Requires:       perl(Try::Tiny)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
String eval is often used for dynamic code generation. For instance, Moose
uses it heavily, to generate inlined versions of accessors and
constructors, which speeds code up at runtime by a significant amount.
String eval is not without its issues however - it's difficult to control
the scope it's used in (which determines which variables are in scope
inside the eval), and it's easy to miss compilation errors, since eval
catches them and sticks them in $@ instead.

%prep
%setup -q -n Eval-Closure-%{version}

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
%doc Changes dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.12-1
- Specfile autogenerated by cpanspec 1.78.