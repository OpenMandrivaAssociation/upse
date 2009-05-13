%define name upse
%define version 1.0.0
%define release %mkrel 2

%define major 2.0.0
%define libname %mklibname upse %major
%define develname %mklibname -d upse

Summary: Playstation sound emulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://distfiles.atheme.org/%{name}-%{version}.tbz2
License: GPLv2
Group: Sound
Url: http://nenolod.net/upse
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libaudacious-devel >= 5:1.4
BuildRequires: libao-devel

%description
UPSE is a work in progress Playstation sound emulator. Unlike other
emulators (SexyPSF), UPSE supports playing back most (a few replayers
seem to have bugs or are dependent on some undocumented feature) PS1
module formats.

%package -n %libname
Summary: Playstation sound emulator library
Group: System/Libraries
%description -n %libname
UPSE is a work in progress Playstation sound emulator. Unlike other
emulators (SexyPSF), UPSE supports playing back most (a few replayers
seem to have bugs or are dependent on some undocumented feature) PS1
module formats.

%package -n %develname
Summary: Playstation sound emulator library
Group: Development/C
Requires: %libname = %version
Provides: libupse-devel = %version-%release

%description -n %develname
UPSE is a work in progress Playstation sound emulator. Unlike other
emulators (SexyPSF), UPSE supports playing back most (a few replayers
seem to have bugs or are dependent on some undocumented feature) PS1
module formats.

%package -n audacious-upse
Summary: Playstation sound emulator plugin for Audacious
Group: Sound
Requires: audacious

%description -n audacious-upse
UPSE is a work in progress Playstation sound emulator. Unlike other
emulators (SexyPSF), UPSE supports playing back most (a few replayers
seem to have bugs or are dependent on some undocumented feature) PS1
module formats.

This adds Playstation sound emulation to the Audacious Media Player.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc NEWS  THANKS  TODO AUTHORS
%_bindir/upse123
%_mandir/man1/upse123.1*

%files -n %libname
%defattr(-,root,root)
%_libdir/libupse.so.%major
%_libdir/libupse.so.2

%files -n %develname
%defattr(-,root,root)
%_includedir/*
%_libdir/libupse.so

%files -n audacious-upse
%defattr(-,root,root)
%_libdir/audacious/Input/upse-audacious.so


