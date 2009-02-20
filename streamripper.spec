%define name	streamripper
%define version 1.64.4
%define release %mkrel 1

Summary:	Audio stream recorder
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
URL:		http://sourceforge.net/projects/streamripper
License:	GPLv2+

Source0:	http://mesh.dl.sourceforge.net/sourceforge/streamripper/%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libglib2-devel
BuildRequires:	tre-devel
BuildRequires:	libmad-devel

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



