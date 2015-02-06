%define name upse
%define version 1.0.0
%define release 7

%define major 2.0.0
%define libname %mklibname upse %major
%define develname %mklibname -d upse

Summary: Playstation sound emulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://distfiles.atheme.org/%{name}-%{version}.tbz2
Patch0: upse-1.0.0-new-audacious.patch
Patch1: upse-disable-audacious.patch
License: GPLv2
Group: Sound
Url: http://nenolod.net/upse
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libao-devel
BuildRequires: zlib-devel

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

%if 0
BuildRequires: libaudacious-devel >= 5:1.4
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
%endif

%prep
%setup -q
%apply_patches

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

%if 0
%files -n audacious-upse
%defattr(-,root,root)
%_libdir/audacious/Input/upse-audacious.so
%endif




%changelog
* Sat Mar 31 2012 Götz Waschk <waschk@mandriva.org> 1.0.0-6mdv2012.0
+ Revision: 788423
- yearly rebuild

* Wed Mar 30 2011 Götz Waschk <waschk@mandriva.org> 1.0.0-5
+ Revision: 649099
- really disable audacious plugin
- update build deps
- disable audacious build

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 1.0.0-4mdv2010.1
+ Revision: 528374
- rebuild

* Wed Feb 03 2010 Götz Waschk <waschk@mandriva.org> 1.0.0-3mdv2010.1
+ Revision: 499937
- patch for new audacious

* Wed May 13 2009 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdv2010.0
+ Revision: 375249
- rebuild for new audacious

* Mon Jul 21 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 239403
- new version
- new major

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdv2008.1
+ Revision: 171210
- rebuild for new libmcs

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 165055
- new version

* Thu Jan 24 2008 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2008.1
+ Revision: 157481
- import upse


* Thu Jan 24 2008 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2008.1
- initial package
