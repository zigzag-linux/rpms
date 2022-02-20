Name:           plasma5-defaults-zigzag
Version:        0
Release:        0
License:        GPL-3.0
Group:          System/GUI/KDE
Summary:        Configuration of Plasma Desktop

URL:            http://github.com/zigzag-linux
Source0:        %{name}-%{version}.tar.gz
Conflicts:      plasma5-defaults-openSUSE
BuildArch:      noarch
BuildRequires:  kf5-filesystem

%prep
%autosetup

%description
This package contains standard configuration of Plasma Desktop for Zigzag

%build

%install
install -d %{buildroot}
cp -a %{name}/* %{buildroot}

%files
%doc LICENSE
%dir %{_sysconfdir}/skel/.config/gtk-3.0
%config %{_sysconfdir}/skel/.config/gtk-3.0/settings.ini
%config %{_kf5_configdir}/*
%dir %{_datadir}/icons/default/
%{_datadir}/icons/default/index.theme
%dir %{_kf5_plasmadir}/look-and-feel
%{_kf5_plasmadir}/look-and-feel/*

%changelog
