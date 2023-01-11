#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Data
%define		pnam	Flow
Summary:	Data::Flow - Perl extension for simple-minded recipe-controlled build of data
Summary(pl.UTF-8):	Data::Flow - rozszerzenie Perla do prostego budowania danych w oparciu o reguły
Name:		perl-Data-Flow
Version:	1.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa453ab013681206bccf43e8e267d63b
URL:		https://metacpan.org/dist/Data-Flow
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Flow - Perl extension for simple-minded recipe-controlled build
of data.

%description -l pl.UTF-8
Data::Flow - rozszerzenie Perla służące do prostego budowania danych
w oparciu o reguły.

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
%{_mandir}/man3/Data::Flow.3pm*
