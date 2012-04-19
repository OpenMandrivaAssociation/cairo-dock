Summary:	A light and eye-candy dock to launch your programs easily
Name:     	cairo-dock
Version:	3.0.0
Release:	%mkrel 1
License:	GPLv3+
Group:		Graphical desktop/Other
Source:		http://launchpad.net/cairo-dock-core/3.0/%{version}/+download/cairo-dock-%{version}.tar.gz
URL:		https://launchpad.net/cairo-dock-core
Patch0:		cairo-dock-2.4.0~2-mga-fix-glib-include.patch
Patch1:		cairo-dock-3.0.0-link.patch
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangox)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xtst)
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	cmake
Suggests:	cairo-dock-plugins = %version
Suggests:	cairo-dock-themes

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_mandir}/man1/cairo-dock.1.*

#---------------------------------------------------------------------
%define major 3
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
%{_includedir}/%name
%{_libdir}/libgldi.so
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------------
%prep
%setup -qn %name-%version
%patch0 -p1
%patch1 -p0

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build

%{find_lang} %{name}
