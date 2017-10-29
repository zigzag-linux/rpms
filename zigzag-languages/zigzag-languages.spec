Name:           zigzag-languages
Version:        1.0.0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Install additional language packages
URL:            http://github.com/zigzag-linux
Source0:        install-languages.sh
Requires:       findutils
Requires:       sudo
Requires:       zypper
BuildArch:      noarch

%description
Automated script for installing translation packages

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/zigzag-languages

%files
%{_bindir}/zigzag-languages

%changelog
