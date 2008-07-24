Summary:	A light and eye-candy dock to launch your programs easily
Name:     	cairo-dock
Version:	1.6.1.2
Release:	%mkrel 1
License:	GPLv3+
Group:		Graphical desktop/Other
Source0: 	http://download.berlios.de/cairo-dock/%name-%version.tar.bz2
URL:		http://www.cairo-dock.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	librsvg-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxtst-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glitz-devel
BuildRequires:	intltool

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name

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

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT
