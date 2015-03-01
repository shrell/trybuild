Name:           perl-WWW-Mechanize
Version:        1.74
Release:        3%{?dist}
Summary:        WWW::Mechanize Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Mechanize/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/WWW-Mechanize-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Form) >= 6
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTML::Parser) >= 3.33
BuildRequires:  perl(HTML::TokeParser) >= 2.28
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Request) >= 1.3
BuildRequires:  perl(HTTP::Server::Simple) >= 0.35
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP) >= 5.829
BuildRequires:  perl(LWP::UserAgent) >= 5.829
BuildRequires:  perl(Test::More) >= 0.34
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(URI) >= 1.36
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(CGI)
Requires:       perl(HTML::Form) >= 6
Requires:       perl(HTML::HeadParser)
Requires:       perl(HTML::Parser) >= 3.33
Requires:       perl(HTML::TokeParser) >= 2.28
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(HTTP::Daemon)
Requires:       perl(HTTP::Request) >= 1.3
Requires:       perl(HTTP::Server::Simple) >= 0.35
Requires:       perl(HTTP::Server::Simple::CGI)
Requires:       perl(HTTP::Status)
Requires:       perl(LWP) >= 5.829
Requires:       perl(LWP::UserAgent) >= 5.829
Requires:       perl(Test::More) >= 0.34
Requires:       perl(Test::Warn) >= 0.11
Requires:       perl(URI) >= 1.36
Requires:       perl(URI::file)
Requires:       perl(URI::URL)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
WWW::Mechanize Perl module

%prep
%setup -q -n WWW-Mechanize-%{version}

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
%doc Changes Makefile.old META.json perlcriticrc
%{perl_vendorlib}/*
%{_mandir}/man3/*
%doc %{_mandir}/man1/mech-dump.1*
%{_bindir}/mech-dump

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.74-3
- ajout des lignes de #files

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.74-2
- add BuildRequires:  perl(CGI)

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.74-1
- Specfile autogenerated by cpanspec 1.78.