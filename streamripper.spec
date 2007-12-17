%define name	streamripper
%define version 1.61.18
%define release %mkrel 3

Summary:	Audio stream recorder
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
URL:		http://sourceforge.net/projects/streamripper
License:	GPL

Source0:	http://mesh.dl.sourceforge.net/sourceforge/streamripper/%{name}-%{version}.tar.bz2
BuildRequires:	libogg-devel
BuildRequires:  libvorbis-devel

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
mkdir -p $RPM_BUILD_ROOT/%_bindir
%makeinstall

%files
%defattr(-,root,root)
%doc README THANKS *.txt 
%_bindir/*
%_mandir/man1/*

%clean
rm -rf $RPM_BUILD_ROOT



