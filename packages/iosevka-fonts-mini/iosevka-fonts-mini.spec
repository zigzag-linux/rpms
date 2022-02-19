#
# spec file for package iosevka-fonts-mini
#
# Copyright (c) 2020 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:     iosevka-fonts-mini
Version:  13.3.1
Release:  0
License:  OFL-1.1
Summary:  Spatial efficient monospace font family for programming (minimal install)
Url:      https://typeof.net/Iosevka

Group:    System/X11/Fonts
Source1:  https://github.com/be5invis/Iosevka/releases/download/v%{version}/ttf-iosevka-%{version}.zip
Source2:  https://github.com/be5invis/Iosevka/releases/download/v%{version}/ttf-iosevka-term-%{version}.zip
Source3:  https://github.com/be5invis/Iosevka/releases/download/v%{version}/ttf-iosevka-fixed-%{version}.zip
Source30: https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md
Source31: https://raw.githubusercontent.com/be5invis/Iosevka/master/README.md

BuildRequires:  unzip
BuildRequires:  fontpackages-devel
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
%reconfigure_fonts_prereq

%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and preparing
technical documents.

%prep
%{__unzip} %{S:1}
%{__unzip} %{S:2}
%{__unzip} %{S:3}
%{__cp} %{S:30} %{S:31} .

%build
declare -A family=( \
    [iosevka]=Iosevka \
    [iosevka-term]=IosevkaTerm \
    [iosevka-fixed]=IosevkaFixed \
    )

declare -A variant=( \
    [regular]=Regular \
    [bold]=Bold \
    )

mkdir selected/

for f in ${!family[@]};
do
  for v in ${!variant[@]};
  do
    cp $f-$v.ttf selected/${family[$f]}-${variant[$v]}.ttf
  done
done

%install
%{__install} -d %{buildroot}%{_ttfontsdir}
%{__install} -m0644 selected/*.ttf %{buildroot}%{_ttfontsdir}
%reconfigure_fonts_scriptlets

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE.md
%{_ttfontsdir}

