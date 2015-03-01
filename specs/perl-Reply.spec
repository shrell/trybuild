Name:           perl-Reply
Version:        0.37
Release:        2%{?dist}
Summary:        Read, eval, print, loop, yay!
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Reply/
Source0:        http://www.cpan.org/authors/id/D/DO/DOY/Reply-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(App::Nopaste)
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(Class::Refresh) >= 0.05
BuildRequires:  perl(Config::INI::Reader::Ordered)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Printer)
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(Eval::Closure) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Proc::InvokeEditor)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(App::Nopaste)
Requires:       perl(B::Keywords)
Requires:       perl(Carp::Always)
Requires:       perl(Class::Refresh) >= 0.05
Requires:       perl(Config::INI::Reader::Ordered)
Requires:       perl(Data::Dump)
Requires:       perl(Data::Printer)
Requires:       perl(Devel::LexAlias)
Requires:       perl(Eval::Closure) >= 0.11
Requires:       perl(File::HomeDir)
Requires:       perl(Module::Runtime)
Requires:       perl(Package::Stash)
Requires:       perl(PadWalker)
Requires:       perl(Proc::InvokeEditor)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(Time::HiRes)
Requires:       perl(Try::Tiny)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
NOTE: This is an early release, and implementation details of this module
      are still very much in flux. Feedback is welcome!

%prep
%setup -q -n Reply-%{version}

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
%doc %{_mandir}/man1/reply.1*
%{_bindir}/reply

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.37-2
- ajoute les lignes de %files

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.37-1
- Specfile autogenerated by cpanspec 1.78.