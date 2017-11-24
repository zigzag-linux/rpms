Name:           zigzag-tools
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Additional tools for Zigzag
URL:            http://github.com/zigzag-linux
Source0:        %{name}-%{version}.tar.gz

Requires:       findutils
Requires:       sudo
Requires:       zypper
BuildArch:      noarch

%description
This package contains additional maintenance utilities:
- zigzag-languages command, for installing locale packages
- zigzag-languages service for periodically instaling locale packages
- zigzag-autoupdate service for periodically installing distro updates

%prep
%autosetup

%build

%install
install -D -m 0755 zigzag-languages.sh %{buildroot}%{_bindir}/zigzag-languages
install -d %{buildroot}%{_unitdir}
install -D -m 0644 *.{service,timer} %{buildroot}%{_unitdir}

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rczigzag-languages
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rczigzag-autoupdate

%pre
%service_add_pre zigzag-autoupdate.service zigzag-autoupdate.timer
%service_add_pre zigzag-languages.service zigzag-languages.timer

%post
%service_add_post zigzag-autoupdate.service zigzag-autoupdate.timer
%service_add_post zigzag-languages.service zigzag-languages.timer

%preun
%service_del_preun zigzag-autoupdate.service zigzag-autoupdate.timer
%service_del_preun zigzag-languages.service zigzag-languages.timer

%postun
%service_del_postun zigzag-autoupdate.service zigzag-autoupdate.timer
%service_del_postun zigzag-languages.service zigzag-languages.timer

%files
%{_bindir}/zigzag-languages
%{_bindir}/rczigzag-languages
%{_bindir}/rczigzag-autoupdate
%{_unitdir}/zigzag-*

%changelog
