Name:           calamares-module-zigzag
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Postinstall module for calamares
URL:            https://github.com/zigzag-linux
Source0:        module.desc
Source1:        main.py
BuildArch:      noarch

%description
Postinstall module for calamares, contains Zigzag-specific scripts

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_libdir}/calamares/modules/zigzag/module.desc
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_libdir}/calamares/modules/zigzag/main.py

%files
%dir %{_libdir}/calamares/
%dir %{_libdir}/calamares/modules
%{_libdir}/calamares/modules/zigzag

%changelog
