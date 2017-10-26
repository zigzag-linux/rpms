Name:           libgnomesu-stub
Version:        1.0.0
Release:        1
Summary:        Stubbed gnomesu for lxqt-sudo
License:        GPL-3.0
Group:          System/GUI/GNOME
Url:            https://github.com/mkrawiec/gekon
Source0:         gnomesu-stub.sh
Requires:       lxqt-sudo

Supplements:    packageand(xdg-utils:gnome-session)
Provides:       libgnomesu = %{version}
Conflicts:		otherproviders(libgnomesu)

%description
This is the stubbed out version of gnomesu which supports sudo and locked root accounts
It uses lxqt-sudo and provides primitive abstraction for xdg-su to use

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/gnomesu

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/gnomesu

%changelog
