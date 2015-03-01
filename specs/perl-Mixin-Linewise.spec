Name:           perl-Mixin-Linewise
Version:        0.106
Release:        1%{?dist}
Summary:        Write your linewise code for handles; this does the rest
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mixin-Linewise/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Mixin-Linewise-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008001
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(PerlIO::utf8_strict)
Requires:       perl(Sub::Exporter)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
It's boring to deal with opening files for IO, converting strings to handle-
like objects, and all that. With Mixin::Linewise::Readers and
Mixin::Linewise::Writers, you can just write a method to handle handles,
and methods for handling strings and filenames are added for you.

%prep
%setup -q -n Mixin-Linewise-%{version}

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
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.106-1
- Specfile autogenerated by cpanspec 1.78.
