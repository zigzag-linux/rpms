Name:           zigzag-artwork
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/GUI/Other
Summary:        Zigzag themes and artwork
URL:            http://github.com/zigzag-linux
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Aggregate package for all zigzag artwork assets

%package -n zigzag-wallpapers
Summary:        Wallpapers and background images for Zigzag
Group:          System/GUI/Other

%description -n zigzag-wallpapers
The default set of Zigzag Linux wallpapers

%prep
%autosetup

%build

%install
install -d %{buildroot}%{_datadir}/wallpapers/zigzag

cp wallpapers/*.jpg %{buildroot}%{_datadir}/wallpapers/zigzag
cp wallpapers/AUTHORS .

%files -n zigzag-wallpapers
%defattr(-,root,root)
%doc AUTHORS
%dir %{_datadir}/wallpapers
%dir %{_datadir}/wallpapers/zigzag
%{_datadir}/wallpapers/zigzag/*.jpg

%changelog
