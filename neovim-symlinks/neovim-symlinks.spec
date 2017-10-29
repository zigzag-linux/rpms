Name:           neovim-symlinks
Version:        1.0.0
Release:        0
Summary:        System-wide: Runs neovim if vi or vim is invoked
License:        MIT
Group:          System/X11/Utilities
Url:            https://build.opensuse.org/package/show/home:mkrwc/neovim-symlinks

BuildArch:      noarch
BuildRequires:	neovim
Requires:		neovim
Conflicts:		otherproviders(vim)
Provides:		vim
Provides:		vi

%description
System-wide: Runs neovim if vi or vim is invoked

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin

_link_names=(edit ex rview rvim vedit vi view vim)
for link in "${_link_names[@]}"; do
	ln -s nvim "$RPM_BUILD_ROOT/usr/bin/$link"
done

%files
%defattr(-,root,root)
%{_bindir}/edit
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/rvim
%{_bindir}/vedit
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/vim
