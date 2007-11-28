#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	MPD-Common
Summary:	Audio::MPD::Common - a bunch of common helper classes for mpd
#Summary(pl.UTF-8):	
Name:		perl-Audio-MPD-Common
Version:	0.1.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b49cb0d33d1c434defa8fec7282bfed7
URL:		http://search.cpan.org/dist/Audio-MPD-Common/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Readonly)
BuildRequires:	perl-Class-Accessor
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Depending on whether you're using a POE-aware environment or not, people
wanting to tinker with mpd (Music Player Daemon) will use either
POE::Component::Client::MPD or Audio::MPD.

But even if the run-cores of those two modules differ completely, they
are using the exact same common classes to represent the various mpd
states and information.

Therefore, those common classes have been outsourced to
Audio::MPD::Common.

This module does not export any methods, but the dist provides the
following classes that you can query with perldoc:

Note that those modules should not be of any use outside the two mpd
modules afore-mentioned.




# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/MPD/*.pm
%{perl_vendorlib}/Audio/MPD/Common
%{_mandir}/man3/*
