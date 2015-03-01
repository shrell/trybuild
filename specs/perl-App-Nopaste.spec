Name:           perl-App-Nopaste
Version:        1.003
Release:        2%{?dist}
Summary:        Easy access to any pastebin
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/App-Nopaste/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/App-Nopaste-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008003
BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Clipboard)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(WWW::Pastebin::PastebinCom::Create) >= 1.003
Requires:       perl(Browser::Open)
Requires:       perl(Class::Load)
Requires:       perl(Clipboard)
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Module::Pluggable)
Requires:       perl(Module::Runtime)
Requires:       perl(namespace::clean)
Requires:       perl(URI::Escape)
Requires:       perl(WWW::Mechanize)
Requires:       perl(WWW::Pastebin::PastebinCom::Create) >= 1.003
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the
name nopaste).

%prep
%setup -q -n App-Nopaste-%{version}

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
%doc Changes CONTRIBUTING dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%doc %{_mandir}/man1/nopaste.1*
%{_bindir}/nopaste

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.003-2
- ajoute les lignes de #files

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 1.003-1
- Specfile autogenerated by cpanspec 1.78.