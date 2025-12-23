Name:           corners
Version:        0.1
Release:        1%?dist
Summary:        Simple wayland utility to draw rounded corners
License:        GPL-3.0-or-later

URL:            https://github.com/garaevdi/%{name}
Source0:        %{url}/archive/refs/heads/main.tar.gz
Source1:        https://gitlab.gnome.org/bugaevc/peel/-/archive/main/peel-main.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)

%description
%{summary}

%prep
%autosetup -n %{name}-main -p1
mkdir -p subprojects/peel
tar -C subprojects/peel --strip-components=1 -x -f %{SOURCE1}

%build
meson subprojects packagefiles --apply
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.MD

%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/com.github.garaevdi.corners.gschema.xml


%ghost %dir %{_libdir}/cmake/peel
%ghost %{_libdir}/cmake/peel/*
%ghost %{_libdir}/pkgconfig/peel.pc

%changelog
%autochagelog