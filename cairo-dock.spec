Summary:	A light and eye-candy dock to launch your programs easily
Name:     	cairo-dock
Version:	1.6.2.3
Release:	%mkrel 1
License:	GPLv3+
Group:		Graphical desktop/Other
Source0: 	http://download.berlios.de/cairo-dock/%name-%version.tar.bz2
Patch0:		cairo-dock-1.6.1.2-use-correct-xdg-menu-dir.patch
URL:		http://www.cairo-dock.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	librsvg-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxtst-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glitz-devel
BuildRequires:	intltool
BuildRequires:	ImageMagick
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
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_liconsdir}/%name.png

#---------------------------------------------------------------------
%package devel
Summary: Development files for cairo-dock
Group: Development/Other
Requires: %name = %version

%description devel
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the include files and library for cairo-dock functions.

%files devel
%defattr(-, root, root)
%{_includedir}/%name
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

mkdir -p %buildroot%_datadir/applications/
cat > %buildroot%_datadir/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=Cairo Dock
Comment=A light and eye-candy dock
Exec=cairo-dock
Icon=cairo-dock
Terminal=false
Type=Application
Categories=GTK;Utility;
EOF

mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
convert data/cairo-dock.svg -resize 48x48 %buildroot%_liconsdir/%name.png
convert data/cairo-dock.svg -resize 16x16 %buildroot%_miconsdir/%name.png
convert data/cairo-dock.svg -resize 32x32 %buildroot%_iconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT
