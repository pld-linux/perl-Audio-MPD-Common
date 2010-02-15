#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	MPD-Common
Summary:	Audio::MPD::Common - a bunch of common helper classes for mpd
Summary(pl.UTF-8):	Audio::MPD::Common - zwstaw wspólnych klas pomocniczych dla mpd
Name:		perl-Audio-MPD-Common
Version:	1.100430
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c173019821862717e603dd884f78074b
URL:		http://search.cpan.org/dist/Audio-MPD-Common/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Module-Build >= 1:0.3601
BuildRequires:	perl-MooseX-Has-Sugar
BuildRequires:	perl-Readonly
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Depending on whether you're using a POE-aware environment or not,
people wanting to tinker with mpd (Music Player Daemon) will use
either POE::Component::Client::MPD or Audio::MPD.

But even if the run-cores of those two modules differ completely, they
are using the exact same common classes to represent the various mpd
states and information. Therefore, those common classes have been
outsourced to Audio::MPD::Common.

%description -l pl.UTF-8
W zależności od korzystania ze środowiska POE osoby chcące manipulować
przy demonie mpd (Music Player Daemon) używają
POE::Component::Client::MPD lub Audio::MPD.

Ale nawet jeśli oba te moduły różnią się całkowicie sposobem
działania, używają dokładnie tych samych wspólnych klas
reprezentujących różne stany i informacje o mpd. W związku z tym
wspólne klasy zostały wydzielone do pakietu Audio::MPD::Common.

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
%dir %{perl_vendorlib}/Audio/MPD
%{perl_vendorlib}/Audio/MPD/*.pm
%{perl_vendorlib}/Audio/MPD/Common
%{_mandir}/man3/*
