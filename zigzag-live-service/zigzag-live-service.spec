Name:           zigzag-live-service
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Live media systemd service
URL:            http://github.com/zigzag-linux
Source0:        zigzag-live.service
BuildRequires:  pkgconfig(systemd)
Requires:       zigzag-configuration
BuildArch:      noarch

%description
Systemd service for zigzag live media additions

%prep

%build

%pre
%service_add_pre zigzag-live.service

%install
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rczigzag-live
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_unitdir}/zigzag-live.service

%post
%service_add_post zigzag-live.service

%preun
%service_del_preun zigzag-live.service

%postun
%service_del_postun zigzag-live.service

%files
%{_unitdir}/zigzag-live.service
%{_sbindir}/rczigzag-live

%changelog
