Name:           perl-Hash-FieldHash
Version:        0.14
Release:        5%{?dist}
Summary:        Lightweight field hash for inside-out objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Hash-FieldHash/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Hash-FieldHash-%{version}.tar.gz
Patch0:         Hash-FieldHash-0.14-MYMETA.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.008005
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(Test::LeakTrace) >= 0.07
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(CPAN::Meta)
Requires:       perl(parent) >= 0.221
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Hash::FieldHash provides the field hash mechanism which supports the inside-
out technique.

%prep
%setup -q -n Hash-FieldHash-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes cpanfile LICENSE META.json minil.toml README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Hash*
%{_mandir}/man3/*

%changelog
* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.14-5
- et en appliquant le patch c'est encore mieux ...

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.14-4
- Patch Hash-FieldHash-0.14-MYMETA.patch : MYMETA.json n'existe pas dans la distribution

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.14-3
- Add BuildRequires:  perl(CPAN::Meta)

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.14-2
- essai sans le BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59

* Sat Feb 28 2015 Jean-Michel REY <vreb87@gmail.com> 0.14-1
- Specfile autogenerated by cpanspec 1.78.
