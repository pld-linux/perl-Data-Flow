#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Flow
Summary:	Data::Flow Perl module
Summary(cs):	Modul Data::Flow pro Perl
Summary(da):	Perlmodul Data::Flow
Summary(de):	Data::Flow Perl Modul
Summary(es):	Módulo de Perl Data::Flow
Summary(fr):	Module Perl Data::Flow
Summary(it):	Modulo di Perl Data::Flow
Summary(ja):	Data::Flow Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Data::Flow ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Data::Flow
Summary(pl):	Modu³ Perla Data::Flow
Summary(pt):	Módulo de Perl Data::Flow
Summary(pt_BR):	Módulo Perl Data::Flow
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Data::Flow
Summary(sv):	Data::Flow Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Data::Flow
Summary(zh_CN):	Data::Flow Perl Ä£¿é
Name:		perl-Data-Flow
Version:	0.05
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aac4ec71bc145ce6bb9663360524b258
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Flow - Perl extension for simple-minded recipe-controlled build
of data.

%description -l pl
Modu³ perla Data::Flow.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Data/Flow.pm
%dir %{perl_vendorlib}/auto/Data/Flow
%{perl_vendorlib}/auto/Data/Flow/autosplit.ix
%{_mandir}/man3/*
