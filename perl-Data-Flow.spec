%include	/usr/lib/rpm/macros.perl
Summary:	Data-Flow perl module
Summary(pl):	Modu³ perla Data-Flow
Name:		perl-Data-Flow
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Flow-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Flow - Perl extension for simple-minded recipe-controlled build
of data.

%description -l pl
Modu³ perla Data-Flow.

%prep
%setup -q -n Data-Flow-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/Flow
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.gz

%{perl_sitelib}/Data/Flow.pm
%{perl_sitearch}/auto/Data/Flow

%{_mandir}/man3/*
