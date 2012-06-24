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
Summary(es):	M�dulo de Perl Data::Flow
Summary(fr):	Module Perl Data::Flow
Summary(it):	Modulo di Perl Data::Flow
Summary(ja):	Data::Flow Perl �⥸�塼��
Summary(ko):	Data::Flow �� ����
Summary(no):	Perlmodul Data::Flow
Summary(pl):	Modu� Perla Data::Flow
Summary(pt):	M�dulo de Perl Data::Flow
Summary(pt_BR):	M�dulo Perl Data::Flow
Summary(ru):	������ ��� Perl Data::Flow
Summary(sv):	Data::Flow Perlmodul
Summary(uk):	������ ��� Perl Data::Flow
Summary(zh_CN):	Data::Flow Perl ģ��
Name:		perl-Data-Flow
Version:	0.05
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Flow - Perl extension for simple-minded recipe-controlled build
of data.

%description -l pl
Modu� perla Data::Flow.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/Data/Flow.pm
%dir %{perl_sitelib}/auto/Data/Flow
%{perl_sitelib}/auto/Data/Flow/autosplit.ix
%{_mandir}/man3/*
