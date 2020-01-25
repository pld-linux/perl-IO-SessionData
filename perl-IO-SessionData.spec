#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	SessionData
Summary:	Supporting module for SOAP::Lite
#Summary(pl.UTF-8):	
Name:		perl-IO-SessionData
Version:	1.03
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	790f9e05465c774cf9a6299500463104
URL:		http://search.cpan.org/dist/IO-SessionData/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supporting module for SOAP::Lite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/*.pm
