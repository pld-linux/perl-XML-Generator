%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Generator
Summary:	XML::Generator perl module
Summary(pl):	Modu³ perla XML::Generator
Name:		perl-XML-Generator
Version:	0.93
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fd39d1143cf06174c872f56382c17b10
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Generator - module for generating XML.

%description -l pl
XML::Generator - modul do generowania XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Generator.pm
%dir %{perl_vendorlib}/XML/Generator
%{perl_vendorlib}/XML/Generator/DOM.pm
%{_mandir}/man3/*
