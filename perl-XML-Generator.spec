%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Generator
Summary:	XML::Generator perl module
Summary(pl):	Modu³ perla XML::Generator
Name:		perl-XML-Generator
Version:	0.91
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Generator - module for generating XML.

%description -l pl
XML::Generator - modul do generowania XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/XML/Generator.pm
%{_mandir}/man3/*
