
%define plugin	kvdrmon
%define name	vdr-plugin-%plugin
%define version	0.6
%define rel	15

Summary:	VDR plugin: kvdrmon support plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr-statusleds.sourceforge.net/kvdrmon/
Source:		http://prdownloads.sourceforge.net/vdr-statusleds/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows monitoring VDR activity. There exists a co-project
kvdrmon. This KDE kicker applet talks with the vdrmon plugin and shows
the VDR status.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# port number to listen in
var=LISTEN_PORT
param="-p LISTEN_PORT"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README


