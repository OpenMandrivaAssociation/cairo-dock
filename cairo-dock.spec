# Needed to build help plugin
%define _disable_ld_no_undefined 1

Summary:	A light and eye-candy dock to launch your programs easily
Name:		cairo-dock
Version:	3.4.1
Release:	2
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		https://launchpad.net/cairo-dock-core
Source0:	http://launchpad.net/cairo-dock-core/3.2/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pangox)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	fontconfig
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	cmake
Suggests:	cairo-dock-plugins = %{version}
Suggests:	cairo-dock-help = %{EVRD}
Suggests:	cairo-dock-themes

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/plug-ins
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_mandir}/man1/cairo-dock.1.*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

#---------------------------------------------------------------------
%define major 3
%define libname %mklibname gldi %{major}

%package -n %{libname}
Summary:	Library files for cairo-dock
Group:		System/Libraries

%description -n %{libname}
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the libraries for cairo-dock functions.

%files  -n %{libname}
%{_libdir}/libgldi.so.%{major}*

#---------------------------------------------------------------------
%package devel
Summary:	Development files for cairo-dock
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description devel
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the include files and library for cairo-dock functions.

%files devel
%{_includedir}/%{name}
%{_libdir}/libgldi.so
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------------

%package help
Summary:	This package provides plugin "help"
Group:		Graphical desktop/Other
Requires:	%{name} = %{EVRD}

%description help
This package provides plugin "help".

%files help
%{_libdir}/%{name}/libcd-Help.so
%{_datadir}/%{name}/plug-ins/Help

#---------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_LIBDIR=lib
%make

%install
%makeinstall_std -C build
chmod 755 %{buildroot}%{_libdir}/libgldi.so.*

%find_lang %{name}

mkdir -p %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert data/cairo-dock.svg -resize 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert data/cairo-dock.svg -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert data/cairo-dock.svg -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
