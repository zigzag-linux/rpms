Name:           neovim-symlinks
Version:        1.0.0
Release:        0
Summary:        Runs neovim when vi or vim is invoked
License:        GPL-3.0
Group:          System/X11/Utilities
Url:            https://build.opensuse.org/package/show/home:mkrwc/neovim-symlinks

BuildArch:      noarch
BuildRequires:  neovim
Requires:       neovim
Conflicts:      otherproviders(vim)
Provides:       vim
Provides:       vi

%description
Creates system-wide symlinks to run Neovim when vi or vim is invoked

%prep

%build

%install
install -d %{buildroot}%{_bindir}

_link_names=(edit ex rview rvim vedit vi view vim)
for link in "${_link_names[@]}"; do
  ln -s nvim "%{buildroot}%{_bindir}/$link"
done

%files
%{_bindir}/edit
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/rvim
%{_bindir}/vedit
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/vim

%changelog
