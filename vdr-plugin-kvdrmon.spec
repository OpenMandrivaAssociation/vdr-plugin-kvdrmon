%define plugin	kvdrmon

Summary:	VDR plugin: kvdrmon support plugin
Name:		vdr-plugin-%plugin
Version:	0.6
Release:	18
Group:		Video
License:	GPL
URL:		http://vdr-statusleds.sourceforge.net/kvdrmon/
Source:		http://prdownloads.sourceforge.net/vdr-statusleds/vdr-%plugin-%{version}.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows monitoring VDR activity. There exists a co-project
kvdrmon. This KDE kicker applet talks with the vdrmon plugin and shows
the VDR status.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# port number to listen in
var=LISTEN_PORT
param="-p LISTEN_PORT"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README




