Name:           zigzag-live-service
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Live media systemd service
URL:            http://github.com/zigzag-linux
Source0:        zigzag-live.service
Requires:       zigzag-configuration
BuildArch:      noarch

%description
Systemd service for zigzag live media additions

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_unitdir}/zigzag-live.service

%post
%service_add_post zigzag-live.service

%preun
%service_del_preun zigzag-live.service

%postun
%service_del_postun zigzag-live.service

%files
%{_unitdir}/zigzag-live.service

%changelog
