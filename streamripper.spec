%define name	streamripper
%define version 1.64.6
%define release  4

Summary:	Audio stream recorder
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
URL:		https://sourceforge.net/projects/streamripper
License:	GPLv2+
Source0:	http://mesh.dl.sourceforge.net/sourceforge/streamripper/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	libglib2-devel
BuildRequires:	tre-devel
BuildRequires:	pkgconfig(mad)

%description
Streamripper records shoutcast compatible and live365 streams.
For shoutcast style streams it finds the "meta data" or track
separation data, and uses that as a marker for where the track
should be separated. For live365 streams it hits the website 
and finds when a track has changed. Either way, the MP3 data 
will be decoded and scanned for a silent point which is where 
tracks will be created.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README THANKS *.txt 
%_bindir/*
%_mandir/man1/*

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.64.6-2mdv2011.0
+ Revision: 614988
- the mass rebuild of 2010.1 packages

* Sat Dec 26 2009 Ahmad Samir <ahmadsamir@mandriva.org> 1.64.6-1mdv2010.1
+ Revision: 482388
- new version 1.64.6

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.64.5-2mdv2010.0
+ Revision: 445265
- rebuild

* Sun Mar 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.64.5-1mdv2009.1
+ Revision: 355550
- update to new version 1.64.5

* Fri Feb 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1.64.4-1mdv2009.1
+ Revision: 343497
- update to new version 1.64.4

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 1.64.3-1mdv2009.1
+ Revision: 330801
- 1.64.3

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 1.63.5-1mdv2009.1
+ Revision: 292801
- new version 1.63.5

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.63.0-4mdv2009.0
+ Revision: 269393
- rebuild early 2009.0 package (before pixel changes)

* Sun May 04 2008 Frederik Himpe <fhimpe@mandriva.org> 1.63.0-3mdv2009.0
+ Revision: 201127
- New version
- Adapt and fix BuildRequires
- Adapt to new license policy

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.61.18-3mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed May 03 2006 Austin Acton <austin@mandriva.org> 1.61.18-2mdk
- buildrequires ogg
- mkrel

* Mon Mar 13 2006 Austin Acton <austin@mandriva.org> 1.61.18-1mdk
- New release 1.61.18

* Mon Nov 14 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.61.16-1mdk
- 1.61.16

* Wed Aug 31 2005 Austin Acton <austin@mandriva.org> 1.61.11-1mdk
- New release 1.61.11

* Wed Apr 27 2005 Austin Acton <austin@mandriva.org> 1.61.8-1mdk
- 1.61.8

* Fri Mar 04 2005 Austin Acton <austin@mandrake.org> 1.61.4-1mdk
- 1.61.4
- source URL

* Wed Sep 22 2004 Austin Acton <austin@mandrake.org> 1.60.8-1mdk
- 1.60.8
- delint a bit

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.32-3mdk
- rebuild

