Name:           calamares-branding-zigzag
Version:        0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Zigzag branding for Calamares installer
URL:            https://calamares.io
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Provides:       calamares-branding = %{version}
Conflicts:      otherproviders(calamares-branding)
Requires:       calamares = %{version}

%description
Calamares is an installer framework. By design it is very customizable,
in order to satisfy a wide variety of needs and use cases.

This package provides Zigzag branding for %{name}.

%prep
%setup

%build

%install
install -d %{buildroot}%{_datadir}/calamares
install -Dpm 0644 calamares-branding/settings.conf \
  %{buildroot}%{_datadir}/calamares/settings.conf

cp -a calamares-branding/{branding,modules} %{buildroot}%{_datadir}/calamares

%files
%dir %{_datadir}/calamares/
%{_datadir}/calamares/settings.conf
%{_datadir}/calamares/modules/
%{_datadir}/calamares/branding/

%changelog
