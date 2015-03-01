Name:           perl-App-Sqitch
Version:        0.999
Release:        5%{?dist}
Summary:        App::Sqitch Perl module
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/App-Sqitch/
Source0:        http://www.cpan.org/authors/id/D/DW/DWHEELER/App-Sqitch-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.010
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Class::XSAccessor) >= 1.18
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::GitLike) >= 1.11
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Devel::StackTrace) >= 1.30
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(IO::Pager)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPC::System::Simple) >= 1.17
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Messages)
BuildRequires:  perl(Locale::TextDomain) >= 1.20
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moo) >= 1.002000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moo::sification)
BuildRequires:  perl(namespace::autoclean) >= 0.16
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.33
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Pod::Simple) >= 1.41
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Template::Tiny) >= 0.11
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Dir)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::File::Contents) >= 0.20
BuildRequires:  perl(Test::MockModule) >= 0.05
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoWarnings) >= 0.083
BuildRequires:  perl(Throwable) >= 0.200009
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library) >= 0.040
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Type::Tiny::XS) >= 0.010
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::db) >= 0.15
Requires:       perl(Class::XSAccessor) >= 1.18
Requires:       perl(Clone)
Requires:       perl(Config::GitLike) >= 1.11
Requires:       perl(DateTime)
Requires:       perl(DBI)
Requires:       perl(Devel::StackTrace) >= 1.30
Requires:       perl(Digest::SHA)
Requires:       perl(Encode::Locale)
Requires:       perl(File::HomeDir)
Requires:       perl(Hash::Merge)
Requires:       perl(IO::Pager)
Requires:       perl(IPC::Run3)
Requires:       perl(IPC::System::Simple) >= 1.17
Requires:       perl(List::MoreUtils)
Requires:       perl(Locale::Messages)
Requires:       perl(Locale::TextDomain) >= 1.20
Requires:       perl(Moo) >= 1.002000
Requires:       perl(Moo::Role)
Requires:       perl(Moo::sification)
Requires:       perl(namespace::autoclean) >= 0.16
Requires:       perl(parent)
Requires:       perl(Path::Class) >= 0.33
Requires:       perl(PerlIO::utf8_strict)
Requires:       perl(Pod::Simple) >= 1.41
Requires:       perl(StackTrace::Auto)
Requires:       perl(String::Formatter)
Requires:       perl(String::ShellQuote)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Template::Tiny) >= 0.11
Requires:       perl(Throwable) >= 0.200009
Requires:       perl(Time::HiRes)
Requires:       perl(Try::Tiny)
Requires:       perl(Type::Library) >= 0.040
Requires:       perl(Types::Standard)
Requires:       perl(Type::Tiny::XS) >= 0.010
Requires:       perl(Type::Utils)
Requires:       perl(URI)
Requires:       perl(URI::db) >= 0.15
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
App::Sqitch Perl module

%prep
%setup -q -n App-Sqitch-%{version}

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
%doc Changes dist LICENSE META.json README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
%config %{_usr}/etc/sqitch/templates/*
%{_bindir}/sqitch

%package mysql
Summary :       MySQL connector for App::Sqitch Perl Module
Requires:       perl(App::Sqitch)
Requires:       perl(DBD::mysql) >= 4.018
Requires:       mysql >= 5.6.4
%description mysql
MySQL connector for App::Sqitch Perl Module

%files mysql
#empty list, we just want to build dependencies here


%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.999-4
- mysql en minuscules

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.999-4
- construction d'un package vide

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.999-3
- ajout du package mysql

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.999-2
- Ajout des lignes de files

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.999-1
- Specfile autogenerated by cpanspec 1.78.
