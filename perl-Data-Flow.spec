%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Flow
Summary:	Data-Flow perl module
Summary(pl):	Modu³ perla Data-Flow
Name:		perl-Data-Flow
Version:	0.05
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Flow - Perl extension for simple-minded recipe-controlled build
of data.

%description -l pl
Modu³ perla Data-Flow.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Data/Flow.pm
%{_mandir}/man3/*
