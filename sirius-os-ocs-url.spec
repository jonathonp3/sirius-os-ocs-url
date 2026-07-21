%define debug_package %{nil}

Name:           os-ocs-url
Version:        3.1.0
Release:        1%{?dist}
Summary:        OCS-URL handler for OpenDesktop.org
License:        GPLv3
URL:            https://www.opendesktop.org
Source0:        ocs-url-3.1.0.tar.xz

Requires:       qt5-qtbase
Requires:       qt5-qtsvg
Requires:       qt5-qtdeclarative
Requires:       libproxy
Requires:       openssl

%description
A specialized URL handler for the OpenCollaboration Services (OCS) protocol.
Repackaged for Sirius-OS and Wolf-OS Atomic desktops to enable seamless 
installation of desktop assets from OpenDesktop.org.

%prep
%setup -q -n ocs-url-3.1.0

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/

%files
%{_bindir}/ocs-url
%{_datadir}/applications/ocs-url.desktop
%{_datadir}/icons/hicolor/scalable/apps/ocs-url.svg

%changelog
* Tue Jul 21 2026 Jonathon <jonathon@sirius-os> - 3.1.0-1
- Initial F44 repackage for Sirius-OS

