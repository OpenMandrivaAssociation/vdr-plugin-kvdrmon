
%define plugin	kvdrmon
%define name	vdr-plugin-%plugin
%define version	0.6
%define rel	17

Summary:	VDR plugin: kvdrmon support plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr-statusleds.sourceforge.net/kvdrmon/
Source:		http://prdownloads.sourceforge.net/vdr-statusleds/vdr-%plugin-%version.tar.bz2
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.6-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.6-15mdv2009.1
+ Revision: 359329
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.6-14mdv2009.0
+ Revision: 197941
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.6-13mdv2009.0
+ Revision: 197683
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.6-12mdv2008.1
+ Revision: 145106
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.6-11mdv2008.1
+ Revision: 103146
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.6-10mdv2008.0
+ Revision: 50011
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.6-9mdv2008.0
+ Revision: 42097
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.6-8mdv2008.0
+ Revision: 22741
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.6-7mdv2007.0
+ Revision: 90935
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.6-6mdv2007.1
+ Revision: 74033
- rebuild for new vdr
- Import vdr-plugin-kvdrmon

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.6-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.6-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.6-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.6-2mdv2007.0
- rebuild for new vdr

* Thu Jul 13 2006 Anssi Hannula <anssi@mandriva.org> 0.6-1mdv2007.0
- initial Mandriva release

