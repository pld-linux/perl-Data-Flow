#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

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
Summary(nb):	Perlmodul Data::Flow
Summary(pl):	Modu� Perla Data::Flow
Summary(pt):	M�dulo de Perl Data::Flow
Summary(pt_BR):	M�dulo Perl Data::Flow
Summary(ru):	������ ��� Perl Data::Flow
Summary(sv):	Data::Flow Perlmodul
Summary(uk):	������ ��� Perl Data::Flow
Summary(zh_CN):	Data::Flow Perl ģ��
Name:		perl-Data-Flow
Version:	0.08
Release:	1
License:	Unknown
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/authors/id/R/RA/RADOS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c6823b51cac7ca583c032574238d128
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.8
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Data/Flow.pm
%dir %{perl_vendorlib}/auto/Data/Flow
%{perl_vendorlib}/auto/Data/Flow/autosplit.ix
%{_mandir}/man3/*
