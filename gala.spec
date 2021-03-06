
%define major 0
%define libname %mklibname gala %{major}
%define devname %mklibname -d gala

%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

%global commitdate  20201219

Name:           gala
Summary:        Gala window manager
Version:        3.3.2
Release:        0.git%{commitdate}.1
License:        GPLv3+
URL:            https://github.com/elementary/gala
Source0:        https://github.com/elementary/gala/archive/%{name}/%{name}-%{version}.tar.gz

#use git to pull support for mutter-7/gnome3.38


BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  meson >= 0.48.0
BuildRequires:  vala >= 0.28.0
BuildRequires:  egl-devel
BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 3.15.2
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(mutter-clutter-7)
BuildRequires:  pkgconfig(mutter-cogl-7)
BuildRequires:  pkgconfig(mutter-cogl-pango-7)
BuildRequires:  pkgconfig(plank) >= 0.11.0

Requires:	%{libname} = %{version}-%{release}

# gala provides a generic icon (apps/multitasking-view)
Requires:       hicolor-icon-theme

# gala's multitasking view is activated via dbus
Requires:       dbus-tools

# gala relies on the new notification server
Requires:       elementary-notifications

%description
Gala is Pantheon's Window Manager, part of the elementary project.

%package -n %{libname}
Summary:        Gala window manager libraries

%description -n %{libname}
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the shared libraries.


%package -n %{devname}
Summary:        Gala window manager development files
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the development headers.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang gala


%files -f gala.lang
%doc AUTHORS README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/autostart/gala-daemon.desktop
%{_bindir}/gala
%{_bindir}/gala-daemon
%{_libdir}/gala/plugins/*
%{_datadir}/applications/gala*.desktop
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%files -n %{libname}
%doc AUTHORS README.md
%license COPYING
%dir %{_libdir}/gala
%dir %{_libdir}/gala/plugins
%{_libdir}/libgala.so.%{major}*

%files -n %{devname}
%doc AUTHORS README.md
%license COPYING
%{_includedir}/gala/
%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc
%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi
