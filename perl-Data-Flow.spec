#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Flow
Summary:	Data::Flow - Perl extension for simple-minded recipe-controlled build of data
Summary(pl):	Data::Flow - rozszerzenie Perla do prostego budowania danych w oparciu o regu³y
Name:		perl-Data-Flow
Version:	0.09
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c889739cb1eb15055b91df08819ff542
#Source0:	http://www.cpan.org/authors/id/R/RA/RADOS/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Flow - Perl extension for simple-minded recipe-controlled build
of data.

%description -l pl
Data::Flow - rozszerzenie Perla s³u¿±ce do prostego budowania danych
w oparciu o regu³y.

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
