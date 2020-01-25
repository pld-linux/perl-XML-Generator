#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Generator
Summary:	XML::Generator - Perl extension for generating XML
Summary(pl.UTF-8):	XML::Generator - rozszerzenie Perla do generowania XML-a
Name:		perl-XML-Generator
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ea1e239bdf3fd6f762c484753776626
URL:		http://search.cpan.org/dist/XML-Generator/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Generator - module for generating XML.

%description -l pl.UTF-8
XML::Generator - moduł do generowania XML-a.

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
%doc Changes README
%{perl_vendorlib}/XML/Generator.pm
%dir %{perl_vendorlib}/XML/Generator
%{perl_vendorlib}/XML/Generator/DOM.pm
%{_mandir}/man3/*
