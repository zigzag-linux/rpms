Name:           libgnomesu-stub
Version:        1.0.0
Release:        0
Summary:        Stubbed gnomesu for lxqt-sudo
License:        GPL-3.0
Group:          System/GUI/GNOME
Url:            https://github.com/zigzag-linux
Source0:        gnomesu-stub.sh
Requires:       lxqt-sudo
BuildArch:      noarch

Supplements:    packageand(xdg-utils:gnome-session)
Provides:       libgnomesu = %{version}
Conflicts:      otherproviders(libgnomesu)

%description
This is the stubbed out version of gnomesu which supports sudo and locked root accounts
It uses lxqt-sudo and provides primitive abstraction for xdg-su to use

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/gnomesu

%files
%{_bindir}/gnomesu

%changelog
