%define debug_package %{nil}

Name:           ocs-url
Version:        3.1.0
Release:        2%{?dist}
Summary:        OCS-URL handler for OpenDesktop.org
License:        GPLv3
URL:            https://www.opendesktop.org
Source0:        ocs-url-3.1.0.tar.xz

# Runtime dependencies to fix the "QtQuick.Controls not installed" error
Requires:       qt5-qtbase
Requires:       qt5-qtsvg
Requires:       qt5-qtdeclarative
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
Requires:       libproxy
Requires:       openssl

%description
A specialized URL handler for the OpenCollaboration Services (OCS) protocol.
Repackaged for Sirius-OS to enable seamless installation of desktop assets.

%prep
# Ensure this matches the folder name inside your tarball
%setup -q -n ocs-url-3.1.0

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/

# ATOMIC MIME FIX: Force registration without needing %post scripts
# This tells the XDG Desktop Portal that ocs-url is the owner of ocs:// links
mkdir -p %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/ocs-url-mime.list
[Default Applications]
x-scheme-handler/ocs=ocs-url.desktop
x-scheme-handler/ocss=ocs-url.desktop
EOF

%files
%{_bindir}/ocs-url
%{_datadir}/applications/ocs-url.desktop
%{_datadir}/applications/ocs-url-mime.list
%{_datadir}/icons/hicolor/scalable/apps/ocs-url.svg

%changelog
* Wed Jul 22 2026 Jonathon <jonathon@sirius-os> - 3.1.0-2
- Fix: Added qt5-qtquickcontrols to resolve QML engine failure
- Fix: Added declarative MIME list for Flatpak/Portal compatibility
- Refactor: Reverted package name to ocs-url

