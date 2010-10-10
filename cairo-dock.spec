Summary:	A light and eye-candy dock to launch your programs easily
Name:     	cairo-dock
Version:	2.2.0
Release:	%mkrel 1
License:	GPLv3+
Group:		Graphical desktop/Other
Source:		http://launchpadlibrarian.net/56954298/cairo-dock-%{version}-4.tar.gz
Patch0:		cairo-dock-2.2.0-fix-str-fmt.patch
URL:		https://launchpad.net/cairo-dock-core
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	librsvg-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxtst-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtkglext-devel
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxrender-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	cmake
Suggests:	cairo-dock-plugins
Suggests:	cairo-dock-themes

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_mandir}/man1/cairo-dock.1.*
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_liconsdir}/%name.png

#---------------------------------------------------------------------
%define major 2
%define libname %mklibname gldi %{major}
%package -n %libname
Summary: Library files for cairo-dock
Group: System/Libraries

%description -n %libname
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the libraries for cairo-dock functions.

%files  -n %libname
%defattr(-, root, root)
%{_libdir}/libgldi.so.%{major}
%{_libdir}/libgldi.so.%{major}.*

#---------------------------------------------------------------------
%package devel
Summary: Development files for cairo-dock
Group: Development/Other
Requires: %name = %version
Requires: %libname = %version

%description devel
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the include files and library for cairo-dock functions.

%files devel
%defattr(-, root, root)
%{_includedir}/%name
%{_libdir}/libgldi.so
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------------
%prep
%setup -qn %name-%version-4
%patch0 -p0

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%{find_lang} %{name}

mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
convert data/cairo-dock.svg -resize 48x48 %buildroot%_liconsdir/%name.png
convert data/cairo-dock.svg -resize 16x16 %buildroot%_miconsdir/%name.png
convert data/cairo-dock.svg -resize 32x32 %buildroot%_iconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT
