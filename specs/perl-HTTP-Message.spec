Name:           perl-HTTP-Message
Version:        6.06
Release:        3%{?dist}
Summary:        HTTP style message (base class)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Message/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Message-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008001
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Encode::Locale) >= 1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(IO::Compress::Bzip2) >= 2.021
BuildRequires:  perl(IO::Compress::Deflate)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::HTML)
BuildRequires:  perl(IO::Uncompress::Bunzip2) >= 2.021
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(Test::More)
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(Encode::Locale) >= 1
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(IO::Compress::Bzip2) >= 2.021
Requires:       perl(IO::Compress::Deflate)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::HTML)
Requires:       perl(IO::Uncompress::Bunzip2) >= 2.021
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(IO::Uncompress::RawInflate)
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(URI) >= 1.10
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
An HTTP::Message object contains some headers and a content body. The
following methods are available:

%prep
%setup -q -n HTTP-Message-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

#suppression des documentations
find $RPM_BUILD_ROOT -type f -name "*.3pm" -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
#%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 6.06-3
- supprime les fichiers de manuel, en conflit avec perl-libwww-perl-5.833-2.el6.noarch

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 6.06-2
- add BuildRequires:  perl(Test::More)

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 6.06-1
- Specfile autogenerated by cpanspec 1.78.