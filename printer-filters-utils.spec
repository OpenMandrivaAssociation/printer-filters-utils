%define mainversion 2008
%define mainrelease %mkrel 2

%define debug 0

##### RPM PROBLEM WORKAROUNDS

# Suppress automatically generated Requires for Perl libraries.
#define _requires_exceptions perl\(.*\)

#define _unpackaged_files_terminate_build       0 
#define _missing_doc_files_terminate_build      0


Summary: Filter-style and IJS printer drivers, printer maintenance utilities
Name:		printer-filters-utils
Version:	%{mainversion}
Release:	%{mainrelease}
License:	GPL
Group:		Publishing
URL:		http://www.linuxprinting.org/

##### PRINTER FILTERS/UTILS BUILDREQUIRES

BuildRequires:	autoconf, libtiff-devel, glib-devel, libijs-devel
BuildRequires:	libjbig-devel, libusb-devel, libgmp-devel
BuildRequires:	lesstif-devel, automake1.4, gimp-devel
BuildRequires:	libnetpbm-devel
BuildRequires:	gtk2-devel
#BuildRequires:	liblcms-devel
BuildRequires:  ghostscript, cupsddk
%ifarch x86_64
BuildRequires:	cups-common >= 1.2.0-0.5361.0mdk
%else
BuildRequires:	cups-common
%endif

# automake 1.4 is needed for z42tool

##### PRINTER FILTERS SOURCES 

# Apple StyleWriter
Source50:	http://homepage.mac.com/monroe/styl/stylewriter.tar.bz2

# Canon CaPSL
Source51:	ftp://metalab.unc.edu/pub/Linux/system/printing/cjet089.tar.bz2

# Lexmark 1100
Source52:	http://www.linuxprinting.org/download/printing/lm1100/lm1100.1.0.2a.tar.bz2

# Lexmark 2070 colour
Source53:	http://www.kornblum.i-p.com/2070/Lexmark2070.html/c2070-0.99.tar.bz2

# Lexmark 2070 grayscale
Source54:	http://www.kornblum.i-p.com/2070/Lexmark2070.html/Lexmark2070.latest.tar.bz2

# Lexmark 7xxx, 57xx, Z51
Source55:	http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/lexmark7000linux-990516.tar.bz2

# Lexmark Z11
Source56:	http://sourceforge.net/projects/lz11/lz11-V2-1.2.tar.bz2
#Source56:	http://sourceforge.net/projects/lz11/lz11-cvs20030907.tar.bz2

# HP DeskJet PPA printers
Source62:	http://download.sourceforge.net/pnm2ppa/pnm2ppa-1.12.tar.bz2
Source63:	http://www.httptech.com/ppa/files/ppa-0.8.6.tar.bz2

# Lexmark 2050
Source64:	http://www.prato.linux.it/~mnencia/lexmark2050/c2050-0.4.tar.bz2

# Lexmark 2030
Source65:	pbm2l2030-1.4.tar.bz2

# Okipage 4w and compatible winprinters
Source66:	http://www.linuxprinting.org/download/printing/oki4linux-2.0.tar.bz2
Source67:	oki4w.startup.bz2
Source68:	oki4w_install.bz2

# Citizen Printiva 600C
Source69:	http://www.dcs.ed.ac.uk/home/jcb/ppmtocpva-1.0.tar.bz2

# CoStar and compatible label printers
Source70:	http://www.freelabs.com/~whitis/software/pbm2lwxl/pbm2lwxl.tar.bz2

# Driver for the Samsung ML-85G and QL-85G winprinters
Source71:	http://www.pragana.net/ml85p-0.2.0.tar.bz2

# Filter for the Lexmark Z42
Source73:	http://www.xs4all.nl/~pastolk/drv_z42-0.4.3.tar.bz2

# GhostScript wrapper for the Pentax PocketJet printers
Source74:	http://www.pragana.net/pentaxpj-1.0.0.tar.bz2

# Unix driver for MicroDry Printers
Source76:	http://www.dcs.ed.ac.uk/home/jcb/ppmtomd/ppmtomd-1.5.tar.bz2

# Driver for the HP LaserJet 1000
Source82:	http://www.linuxprinting.org/download/printing/pbmtozjs.c.bz2

# Driver for Zenographics-based printers (Minolta magicolor DL series, HP
# LaserJet 1000, 1005, 1018, 1020, 1022, Color LaserJet 1600, 2600)
Source83:	http://foo2zjs.rkkda.com/foo2zjs.tar.bz2
Source830:	foo2zjs-foomatic-data-20060608.tar.bz2

# Driver for Epson EPL "L" series
Source84:	http://cesnet.dl.sourceforge.net/sourceforge/epsonepl/epsoneplijs-0.4.0.tar.bz2
#Source84:	http://cesnet.dl.sourceforge.net/sourceforge/epsonepl/epsoneplijs-cvs20040128.tar.bz2

# Driver for Lexmark X125 (only printing)
Source1000:	http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-0.2.3.tar.bz2
Source1001:	http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-network-0.2.0.tar.bz2

# Driver for Canon LBP-460/660
Source1010:	http://www.boichat.ch/nicolas/lbp660/lbp660-0.2.4.tar.bz2

# Driver for Lexmark X74/X75
Source1020:	http://home.online.no/~enrio/lxx74-cups-0.8.4.1.tar.bz2

# Driver for Minolta magicolor 2300W
Source1030:	http://heanet.dl.sourceforge.net/sourceforge/m2300w/m2300w-0.51.tar.bz2

# Driver for Minolta PagePro 12xxW, 13xxW, and 14xxW
Source1035:	http://www.hinterbergen.de/mala/min12xxw/min12xxw-0.0.9.tar.bz2

# Driver for Casio USB label printers
Source1040:	http://www.tu-harburg.de/~soda0231/pegg/files/pegg-0.23.tar.bz2
Source1041:	http://www.tu-harburg.de/~soda0231/pegg/files/xbm2crw-0.4.tar.bz2
Source1042:	http://www.tu-harburg.de/~soda0231/pegg/files/cups2pegg-0.21a.tar.bz2
Source1043:	http://www.tu-harburg.de/~soda0231/pegg/files/pegg_el-0.11.tar.bz2

# Perl script to clean up Manufacturer entries in the PPD files, so that
# drivers are sorted by the printer Manufacturer in the graphical frontends
Source201: 	cleanppd.pl.bz2

# Drivers for the Konica Minolta magicolor DL series supplied by Konica
# Minolta
# Available on: http://printer.konicaminolta.com/support/index_ds.html
# (Choose printer model under "Color Laser", then choose "Linux" under
# "Drivers, PPDs, & Utilities")
Source1050:	magicolor2430DL-1.6.0.tar.bz2
Source1051:	magicolor5430DL-1.8.0.tar.bz2
Source1052:	magicolor5440DL-1.2.0.tar.bz2

# Driver for Canon LBP-810/1120
Source1060:	http://www.boichat.ch/nicolas/capt/capt-0.1.tar.bz2

# Driver for Brother P-Touch label printers
Source1070:  	http://www.diku.dk/~panic/P-touch/ptouch-driver-1.0.tar.bz2

# Driver for Kyocera GDI printers: Kyocera FS-1016MFP
Source1080:    http://sourceforge.net/projects/kyo-fs1016mfp/foo2kyo-0.1.0a.tar.bz2

# Driver for Samsung SPL2 printers
Source1090:	splix-0.0.1.tar.bz2

##### PRINTER FILTERS PATCHES

# Apple StyleWriter
Patch1040:	stylewriter-gcc4.patch

# Lexmark 1100
Patch50:	lexmark2ppm.pl.patch
Patch1002:	lm1100.1.0.2a-fix-compile-gcc-3.4.patch

# HP DeskJet PPA printers
Patch52:	pbm2ppa-20000205.diff

# Okipage 4w and compatible winprinters
Patch54:	http://www.linuxprinting.org/download/printing/oki4linux-2.0-daemon-patch
Patch55:	oki4linux-2.0-daemon-mdk-patch

# "-fPIC" for Epson EPL xxxxL driver (Gwenole)
Patch1001:	epsoneplijs-0.3.0-fPIC.patch

# Deactivate checks for installed Foomatic in "./configure" of "m2300w"
Patch1030:	m2300w-0.3-noppdbuild.patch
Patch1031:	m2300w-0.2-ppc-build-fix.patch

# Correct "Duplex" option in Foomatic data of "foo2zjs"
Patch1050:	foo2zjs-Duplex.patch
# Add support for Minolta magicolor 2430 to "foo2zjs"
Patch1051:	foo2zjs-foomatic-magicolor-2430-dl.patch

# Driver for Samsung SPL2 printers: correction for CUPS 1.2 compatibility
Patch1060:	splix-0.0.1-cups-1.2.patch


##### PRINTER UTILS

# Printer maintenance (All PJL and some Lexmark Optra)
#Source57:	http://pup.sourceforge.net/pup_1.1_src.tar.bz2

# Lexmark printer maintenance
Source58:	http://www.powerup.com.au/~pbwest/lexmark/lexmark.html/lxcontrol.tar.bz2
Source59:	lm1100maint.tar.bz2
Source60:	http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/changecartridge.bz2
Source61:	printutils.png.bz2

# Script to adjust margins and offsets of printed pages
Source75: 	alignmargins.bz2
Source175:	align.ps.bz2

# mtink - Graphical maintenance/ink monitoring tool for Epson inkjets
Source77:	http://xwtools.automatix.de/files/mtink-1.0.14.tar.gz
# mtink - Do not request koi8-ru, but koi8-r instead. Fixes mdv#25315
Patch70:	mtink-1.0.14-ru_font.patch

# poster - Print big posters to be assambled out of many standard sized
#          (A4, Letter, A3, ...) sheets, also used by KDE Print.
Source78:	http://printing.kde.org/downloads/poster-1.0.1.tar.bz2

# Tool for uploading the firmware on the HP LaserJet 1000S
Source85:	http://www.linuxprinting.org/download/printing/hp1000fw.bz2
Source86:	udev-hp1000fw.rules.bz2

# Tools for reading USB device ID strings
Source87:	http://www.linuxprinting.org/download/printing/usb_id_test.c.bz2
Source88:	http://www.linuxprinting.org/download/printing/getusbprinterid.pl.bz2

# ppmtocpva & ppmtomd fixes
Patch100:	ppmtocpva-1.0-includes.patch
Patch101:	ppmtocpva-1.0-netpbm.patch
Patch102:	ppmtomd-1.3-netpbm.patch



##### BUILD ROOT

BuildRoot:	%_tmppath/%name-%version-%release-root

##### PACKAGE DESCRIPTIONS

##### PRINTER FILTERS

%package -n printer-filters
Summary: Filters to support additional printers
Group: 		Publishing
Requires(post):	ghostscript
Requires(post):	rpm-helper
Requires(preun):rpm-helper
# psutils, unzip, and mscompress needed by the foo2zjs driver
Requires:	psutils, unzip
%if %mdkversion >= 200700
Requires:	mscompress
%endif
# "convert" needed by "pegg"
Requires:	ImageMagick
Conflicts:	foomatic-db <= 3.0.1 cups-drivers < 2006
Conflicts:	printer-utils <= 2006-11mdk

# <mrl> Requires for the packages that are obsoleting this one.
Requires:	c2050
Requires:	c2070
Requires:	cjet
Requires:	cups-drivers-capt
Requires:	cups-drivers-foo2kyo
Requires:	cups-drivers-foo2zjs
Requires:	cups-drivers-lbp660
Requires:	cups-drivers-lz11
Requires:	cups-drivers-m2300w
Requires:	cups-drivers-pegg
Requires:	cups-drivers-ptouch
Requires:	drv_z42
Requires:	epsoneplijs
#Requires:	foomatic-db-foo2zjs
#Requires:	foomatic-db-m2300w
Requires:	lexmark2070
Requires:	lexmark7000linux
Requires:	lm1100
Requires:	min12xxw
Requires:	ml85p
Requires:	oki4linux
Requires:	pbm2l2030
Requires:	pbm2lwxl
Requires:	pbmtozjs
Requires:	pentaxpj
Requires:	pnm2ppa
Requires:	ppmtocpva
Requires:	ppmtomd
Requires:	printer-filters
Requires:	stylewriter
Requires:	x125

%package -n printer-filters-doc
Summary: Documentation for printer filters (to support additional printers)
Group: 		Publishing

##### PRINTER UTILS

%package -n printer-utils
Summary: Additional tools for configuring and maintaining printers
Group: 		Publishing
Obsoletes:	ghostscript-utils Lexmark-printer-maintenance
Provides:	ghostscript-utils Lexmark-printer-maintenance
Requires(post):	rpm-helper
Requires(preun):rpm-helper
Requires:	lesstif
Conflicts:	ghostscript < 8.15

# <mrl> Requires for the packages that are obsoleting this one.
Requires:	lm1100
Requires:	lxcontrol
Requires:	mtink
Requires:	poster
Requires:	printer-utils
Requires:	z42tool

%package -n cups-drivers
Summary:	Special CUPS printer drivers
Requires: 	cups >= 1.1, ghostscript >= 7.05
# "convert" needed by "pegg"
Requires:	ImageMagick
Conflicts:	printer-utils <= 1.0-142mdk printer-filters < 2006
%ifarch x86_64
Conflicts:	cups < 1.2.0-0.5361.0mdk
%endif
Group: 		Publishing

# <mrl> Requires for the packages that are obsoleting this one.
Requires:	cups-drivers-lxx74
Requires:	cups-drivers-magicolor2430dl
Requires:	cups-drivers-magicolor5430dl
Requires:	cups-drivers-magicolor5440dl
Requires:	cups-drivers-pegg
Requires:	cups-drivers-splix
Requires:	mtink

##### DESCRIPTION TEXTS

%description
This source RPM builds the printer-filters and printer-utils
packages. These two packages are built by one source RPM, as many
upstream source packages contain both a filter and a utility.

%description -n printer-filters
This package contains filters which transfer the raw bitmap of
GhostScript into the protocol of some additional printer models. There
are standalone filter executables which get GhostScripts bitmap output
as standard input via a pipe or IJS plug-ins for GhostScript.

Note: HPIJS and Gimp-Print are in separate packages.

%description -n printer-filters-doc
This package contains documentation about printer filters.

These filters transfer the raw bitmap of GhostScript into the protocol
of some additional printer models. There are standalone filter
executables which get GhostScripts bitmap output as standard input via
a pipe or IJS plug-ins for GhostScript.

%description -n printer-utils
Tools for printer maintenance: Setting default options for most laser
printers (PJL-capable printers), cartridge changing, head aligning,
ink level checking for inkjet printers. Printing big posters on many 
sheets of standard sized paper (A4, A3, Letter, ...) to be assambled
together (also used by KDE Print to print posters).

%description -n cups-drivers
This package contains special printer drivers to be used with CUPS and
their appropriate PPD files.


%prep
%setup -q -T -c
mkdir printer-filters
echo > printer-filters/debugfiles.list
exit 0

# remove old directory
rm -rf $RPM_BUILD_DIR/%{name}-%{mainversion}
mkdir $RPM_BUILD_DIR/%{name}-%{mainversion}

mkdir $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters

# Apple StyleWriter
%setup -q -T -D -a 50 -n %{name}-%{mainversion}/printer-filters
cd stylewriter
%patch1040 -p0
cd ..

# Canon CaPSL
%setup -q -T -D -a 51 -n %{name}-%{mainversion}/printer-filters

# Lexmark 1100
%setup -q -T -D -a 52 -n %{name}-%{mainversion}/printer-filters
# fix to make it compiling with gcc 2.96
# Patch to make LM 1100 printer emulator script to work
cd lm1100*
%patch50 -p0
%patch1002 -p0
cd ..

# Lexmark 2070 colour
%setup -q -T -D -a 53 -c -n %{name}-%{mainversion}/printer-filters/c2070-0.99

# Lexmark 2070 grayscale
%setup -q -T -D -a 54 -c -n %{name}-%{mainversion}/printer-filters/Lexmark2070.latest

# Lexmark 7xxx, 57xx, Z51
%setup -q -T -D -a 55 -n %{name}-%{mainversion}/printer-filters
# Fix Makefile
cd lexmark7000linux-990516
sed "s/-o root -g root//" Makefile > Makefile.new
chmod --reference=Makefile Makefile.new
mv -f Makefile.new Makefile
cd ..

# Lexmark Z11
%setup -q -T -D -a 56 -n %{name}-%{mainversion}/printer-filters
#setup -q -T -D -a 56 -n %{name}-%{mainversion}/printer-filters
#bzcat %SOURCE72 > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/LexZ11-distro/cZ11.c
perl -p -i -e "s/gcc/gcc $RPM_OPT_FLAGS/" lx11*/makefile

# Printer Utility Program
#setup -q -T -D -a 57 -n %{name}-%{mainversion}/printer-filters

# Lexmark printer maintenance
%setup -q -T -D -a 58 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 59 -n %{name}-%{mainversion}/printer-filters
bzcat %{SOURCE60} > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/changecartridge
#cp $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/pup_1.1/README \
#	$RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/README.LexmarkOptra40_45
mv $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/lxcontrol/README.Lexmark \
	$RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/lxcontrol/README.Lexmark5xxx_7xxx
mv $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/lm1100maint/README \
	$RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/lm1100maint/README.Lexmark1xxx

# Generate doc file for "changecartridge"
cat << EOF > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/README.changecartridge

changecartridge - a program for changing the ink cartridges
                  in the Lexmark 5xxx and 7xxx printers.

(C) 1999 Henryk Paluch, paluch@bimbo.fjfi.cvut.cz

To change the ink cartridges in a Lexmark printer you must move the
print head out of its parking corner, so that you can reach the
cartridges. Lexmark only provides a Windows program for doing this. To
not need to boot Windows for changing the cartridges there is this
script. Simply call it with:

   changecartridge

on the command line and follow the steps described on the screen.
The printer is assumed to be at the parallel port #1 (/dev/lp0), but
this setting can be changed by editing the definition of the PORT
variable in /usr/bin/changecartridge.



EOF
# Generate doc file for "README.Lexmark-Maintenance"
cat << EOF > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/README.Lexmark-Maintenance

Lexmark Printer Maintenance Tools
---------------------------------

Programs for maintanance of Lexmark inkjet printers: Moving out the print
head to change the cartridges, adjusting the print heads, cleaning the
nozzles ...

showcartridges
hidecartridges
headalign
headclean     - Command line programs for the Lexmark 5xxx and 7xxx

changecartridge - Another command line tool for changing the
                ink cartridges in the Lexmark 5xxx and 7xxx 

lm1100change,
lm1100back    - Command line tools for changing the cartridge in Lexmark
                1xxx printers

Since Lexmark will not release protocol specifications the authors had
to dissassemble the byte codes sent by their Windows printer maintenance
programs to create this.



EOF

# Load menu icon
bzcat %{SOURCE61} > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/printutils.png

# HP DeskJet PPA printers
%setup -q -T -D -a 62 -n %{name}-%{mainversion}/printer-filters
# remove "version ERROR" line from pnm2ppa.conf
perl -n -i -e 'if ( !m/^\s*version\s*0\s*(|\#.*)$/ ) { print "$_";}' pnm2ppa-*/pnm2ppa.conf

# Generate README file
cat <<EOF >README.calibration

Colour calibration for PPA printers
-----------------------------------

If you have an HP DeskJet PPA printer (very cheap models: 710C, 712C,
720C, 722C, 820C, 1000C, or a newer printer which works with one of
these model entries) you can optionally do a colour correction. Do the
following:

Some of the printing modes offer optional colour correction. See the
option "Printing Mode" which is offered to you in the option window of
"printerdrake" and if you use CUPS also in "qtcups" or "kprinter"
("Properties" button, "Advanced" tab), "xpp" ("Options" button,
"Extra" tab), "kups" (right click on printer, "Configure printer" in
menu), or the WWW interface ("Configure printer" button) and if you
use PDQ in "xpdq" ("Driver options"). Choose a setting with "optional
colour correction" and save your settings. Read the file

   /usr/share/doc/printer-filters-1.0/HPDeskJetPPA/pnm2ppa/COLOR.txt

and follow the instructions there, but use the name

   /etc/pnm2ppa.gamma_normal

for the colour correction file for the "normal quality" modes and

   /etc/pnm2ppa.gamma_best

for the colour correction file for the "best quality" modes. So you
can do the colour correction independently in both normal and best
quality modes. The files are automatically taken into account by the
appropriate modes as soon as they are created.



EOF


# pbm2ppa source
%setup -q -T -D -a 63 -n %{name}-%{mainversion}/printer-filters
%patch52 -p0

# Lexmark 2050
%setup -q -T -D -a 64 -n %{name}-%{mainversion}/printer-filters

# Lexmark 2030
%setup -q -T -D -a 65 -c -n %{name}-%{mainversion}/printer-filters/pbm2l2030

# Okipage 4w and compatible winprinters
%setup -T -D -a 66 -n %{name}-%{mainversion}/printer-filters
cd oki4linux-2.0
%patch54 -p1
%patch55 -p1

# Do some small corrections in the daemon script:
# - The daemon crashes with "setlogsock('unix');"
# - Correct the path for the driver
cd src
mv oki4daemon oki4daemon.pre
sed "s/setlogsock('unix');/setlogsock('inet');/" oki4daemon.pre | sed "s:/usr/local/sbin/oki4drv:/usr/bin/oki4drv:" > oki4daemon
cd ../..
# Mandrivized startup script for the daemon
bzcat %{SOURCE67} > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/oki4daemon
%if 0
# Installer for a CUPS queue for an OKI winprinter
bzcat %{SOURCE68} > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/oki4w_install
# Generate doc file for "README.OKI-Winprinters"
cat << EOF > $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters/README.OKI-Winprinters

Driver for the OKI 4w and compatible winprinters
------------------------------------------------

These laser printers have neither memory nor a processor and therefore
they must get their data in an absolutely continuous stream (because
they cannot buffer data). This cannot be made sure by usual printing
spoolers (as CUPS or LPD). The only possibility is running a special
driver program which connects directly to the printer. But this is
very unconvenient, because many Linux applications can only print
through a spooler. To solve this, Grant Taylor has created a special
daemon acting between the printing program and the spooler, the
"oki4daemon". It provides a named pipe ("/dev/oki4drv") which accepts
PostScript and renders it for being understood by the printer.

Because "kups" and the web interface of CUPS cannot start an extra
daemon and also cannot set up a queue with "/dev/oki4drv" as
destination, you have to install your OKI printer with a special
installation program. Call it by entering

   oki4w_install

on the command line or by choosing "Configuration"/"Printing"/"Install
OKI 4w or compatible" in the desktop menues.

NOTE: These printers should not be used on machines which are often
under high loads (because of the timing requirements) or on machines
with high security demands (because of the additional daemon).



EOF
%endif

# CoStar and compatible label printers
%setup -q -T -D -a 70 -c -n %{name}-%{mainversion}/printer-filters/pbm2lwxl

# Citizen Printiva 600C
%setup -q -T -D -a 69 -n %{name}-%{mainversion}/printer-filters
cd ppmtocpva-*
%patch100 -p1
%patch101 -p1
cd ..

# Samsung ML-85G and QL-85G winprinters
%setup -q -T -D -a 71 -n %{name}-%{mainversion}/printer-filters
#patch58 -p0

# Filter for the Lexmark Z42
%setup -q -T -D -a 73 -n %{name}-%{mainversion}/printer-filters

# GhostScript wrapper for the Pentax PocketJet printers
%setup -q -T -D -a 74 -n %{name}-%{mainversion}/printer-filters

# Unix driver for MicroDry Printers
%setup -q -T -D -a 76 -n %{name}-%{mainversion}/printer-filters
cd ppmtomd-*
%patch102 -p1
cd ..

# Mtink - Printer maintenance/ink monitoring for Epson inkjets
%setup -q -T -D -a 77 -n %{name}-%{mainversion}/printer-filters
cd mtink-1*
%patch70 -p3
cd ..

# Poster - Poster-printing on stndard sized paper 
%setup -q -T -D -a 78 -n %{name}-%{mainversion}/printer-filters

# Driver for the HP LaserJet 1000
bzcat %{SOURCE82} > pbmtozjs.c

# Driver for Zenographics-based printers (Minolta magicolor DL series, HP
# LaserJet 1000, 1005, 1018, 1020, 1022, Color LaserJet 1600, 2600)
%setup -q -T -D -a 83 -n %{name}-%{mainversion}/printer-filters
cd foo2zjs*/foomatic-db
rm -rf *
%setup -q -T -D -a 830 -n %{name}-%{mainversion}/printer-filters/foo2zjs/foomatic-db
cd ../..
# Fit udev rules to stricter syntax of new udev
# (blino) don't try to rename the device,
#         it has already been renamed to the exact same name in 50-mdk.rules
#         so udev would skip the rule
perl -p -i -e 's:(KERNEL|BUS|SYSFS.*?)=([^=]):$1==$2:g;s{SYMLINK=}{SYMLINK+=}g;s{(?:NAME|MODE)=.*?,\s*}{}g' foo2zjs*/hplj10xx.rules

# Driver for Epson EPL "L" series
%setup -q -T -D -a 84 -n %{name}-%{mainversion}/printer-filters
cd epsonepl*
perl -p -i -e "s/-g -O2 -Wall -ansi -pedantic -Wmissing-prototypes/-fPIC/" Makefile.in
#patch1001 -p1 -b .fPIC
cd ..

# Driver for Lexmark X125 (only printing)
%setup -q -T -D -a 1000 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 1001 -n %{name}-%{mainversion}/printer-filters
perl -p -i -e "s/gcc/gcc $RPM_OPT_FLAGS/" drv_x125*/src/Makefile

%ifarch %{ix86}
# Driver for Canon LBP-460/660
%setup -q -T -D -a 1010 -n %{name}-%{mainversion}/printer-filters
perl -p -i -e "s/gcc/gcc $RPM_OPT_FLAGS/" lbp660*/Makefile
%endif

# Driver for Canon LBP-810/1120
%setup -q -T -D -a 1060 -n %{name}-%{mainversion}/printer-filters
perl -p -i -e "s/gcc/gcc $RPM_OPT_FLAGS/" cast*/Makefile

# Driver for Lexmark X74/X75
%setup -q -T -D -a 1020 -n %{name}-%{mainversion}/printer-filters
perl -p -i -e "s/gcc/gcc $RPM_OPT_FLAGS/" lxx74*/Makefile

# Driver for Minolta magicolor 2300W
%setup -q -T -D -a 1030 -n %{name}-%{mainversion}/printer-filters
cd m2300w*
# Deactivate checks for installed Foomatic in "./configure"
%patch1030 -p0
%patch1031 -p1 -b .ppc
cd ..

# Driver for Minolta PagePro 12xxW, 13xxW, and 14xxW
%setup -q -T -D -a 1035 -n %{name}-%{mainversion}/printer-filters
#perl -p -i -e "s/gcc/gcc $RPM_OPT_FLAGS/" min12xxw*/Makefile

# Driver for Casio USB label printers
%setup -q -T -D -a 1040 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 1041 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 1042 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 1043 -n %{name}-%{mainversion}/printer-filters

# Drivers for the Konica Minolta magicolor DL series supplied by Konica
# Minolta
%setup -q -T -D -a 1050 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 1051 -n %{name}-%{mainversion}/printer-filters
%setup -q -T -D -a 1052 -n %{name}-%{mainversion}/printer-filters
# Fix copy of CUPS headers in kmlf.h
perl -p -i -e 's:\bcups_strlcpy:_cups_strlcpy:g' magicolor????DL*/src/kmlf.h
# Remove asterisks from group names in PPD file
for d in magicolor????DL*; do
	cd $d*
	gzip -dc src/km_en.ppd.gz | perl -p -e 's/(Group:\s+)\*/$1/g' | gzip > src/km_en.tmp.ppd.gz && mv -f src/km_en.tmp.ppd.gz src/km_en.ppd.gz
	cd ..
done
# Determine the directory for the CUPS filters using the correct method
perl -p -i -e 's:(CUPS_SERVERBIN=)"\$libdir/cups":$1`cups-config --serverbin`:' magicolor????DL*/configure

# Driver for Brother P-Touch label printers
%setup -q -T -D -a 1070 -n %{name}-%{mainversion}/printer-filters

# Driver for Kyocera GDI printers: Kyocera FS-1016MFP
%setup -q -T -D -a 1080 -n %{name}-%{mainversion}/printer-filters
perl -p -i -e 's/Kyocera-Mita-FS-1016/Kyocera-FS-1016/g' foo2kyo*/foomatic-db/driver/foo2kyo.xml

# Driver for Samsung SPL2 printers
%setup -q -T -D -a 1090 -n %{name}-%{mainversion}/printer-filters
cd splix*
%patch1060 -p1 -b .cups12
cd ..


# Tool for uploading the firmware on the HP LaserJet 1000S
bzcat %{SOURCE85} > hp1000fw
bzcat %{SOURCE86} > udev-hp1000fw.rules

# Tools for reading USB device ID strings
bzcat %{SOURCE87} > usb_id_test.c
bzcat %{SOURCE88} > getusbprinterid



%build
exit 0

# Change compiler flags for debugging when in debug mode
%if %debug
export DONT_STRIP=1
export CFLAGS="`echo %optflags |sed -e 's/-O3/-g/' |sed -e 's/-O2/-g/'`"
export CXXFLAGS="`echo %optflags |sed -e 's/-O3/-g/' |sed -e 's/-O2/-g/'`"
export RPM_OPT_FLAGS="`echo %optflags |sed -e 's/-O3/-g/' |sed -e 's/-O2/-g/'`"
%endif

##### PRINTER FILTERS AND OTHER STUFF

cd $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters

# Apple StyleWriter
cd stylewriter
gcc ${CFLAGS:-%optflags} -o lpstyl lpstyl.c
cd ..

# Canon CaPSL
cd cjet089
%make
cd ..

# Lexmark 1100
cd lm1100*
# Correct "friend" declarations for gcc 3.1
perl -p -i -e 's/friend Lexmark/friend class Lexmark/' *.h
# Remove extra qualifications '<class>::<member>' on class members, to make
# code compiling with gcc 4.1.1.
perl -p -i -e 's/\b[^\s:]+:://' *.h
%make
cd ..

# Lexmark 2070 colour
cd c2070-0.99
%make
cd ..

# Lexmark 2070 grayscale
cd Lexmark2070.latest
%make
cd ..

# Lexmark 7xxx, 57xx, Z51
cd lexmark7000linux-990516
%make
cd ..

# Lexmark Z11
#cd LexZ11-distro
cd lz11*
%make
cd ..

# Printer Utility Program
#cd pup_1.1
#make CC="gcc $CFLAGS -Wall -O2 -I/usr/include/glib-1.2"
#cd ..

# HP DeskJet PPA printers
cd pnm2ppa*
make BINDIR=%{_bindir} CONFDIR=%{_sysconfdir} MANDIR=%{_mandir}/man1
cd ..
cd pbm2ppa-0.8.6
make
cd ..

# Lexmark 2050
cd c2050-0.4
%make
cd ..

# Lexmark 2030
cd pbm2l2030
%make
cd ..

# Okipage 4w and compatible winprinters
cd oki4linux-2.0/src
%make
cd ../..

# Citizen Printiva 600C
cd ppmtocpva-1.0
%make
cd ..

# CoStar and compatible label printers
cd pbm2lwxl
gcc $CFLAGS -o pbm2lwxl pbm2lwxl.c
cd ..

%ifarch %{ix86}
# Samsung ML-85G and QL-85G winprinters
cd ml85p*
make
[ -e printer-test.ps.gz ] && gunzip printer-test.ps.gz
cd ..
%endif

# Filter for the Lexmark Z42
cd drv_z42/src
gcc $CFLAGS -o z42_cmyk z42_cmyk.c
cd ../z42tool/
%configure
%make
cd ../..

# GhostScript wrapper for the Pentax PocketJet printers
cd pentaxpj
%make
cd ..

# Unix driver for MicroDry Printers
cd ppmtomd*
%make
cd ..

# Mtink - Printer maintenance/ink monitoring for Epson inkjets
cd mtink*
perl -p -i -e 's|(/usr/X11R6)/lib\b|\1/%{_lib}|g' Makefile.ORG
perl -p -i -e 's|(/usr)/lib\b|\1/%{_lib}|g' Makefile.ORG
perl -p -i -e 's|(/usr)/lib$|\1/%{_lib}|g' Configure
perl -p -i -e 's|(''/usr/)lib('')|$1%{_lib}$2|g' checkMotifVersion.sh
./Configure --no-suid --prefix /usr
%make
# Fix some small bugs
#perl -p -i -e "s/START_LEVEL=S99mtink/START_LEVEL=S59mtink/" etc/installInitScript.sh
#perl -p -i -e "s/STOP_LEVEL=K02mtink/START_LEVEL=K61mtink/" etc/installInitScript.sh
#perl -p -i -e "s/for d in 2 3 4 5/XXXXXXXXXX/" etc/installInitScript.sh
#perl -p -i -e "s/for d in 0 1 6/for d in 2 3 4 5/" etc/installInitScript.sh
#perl -p -i -e "s/XXXXXXXXXX/for d in 0 1 6/" etc/installInitScript.sh
#perl -p -i -e "s!cp mtink /etc/init.d!!" etc/installInitScript.sh
perl -p -i -e "s!chmod 744 /etc/init.d/mtink!!" etc/installInitScript.sh
perl -p -i -e "s!/dev/lp;!/dev/lp\*;!" etc/mtink
perl -p -i -e 's=(\#!/bin/sh)=$1\n\#   chkconfig: 2345 14 61
\#   description: The MTink daemon allows printing on Epson inkjets in
\#                in packet mode. This way simultaneas printing and
\#                ink level readout or scanning (on multi-function devices)
\#                is possible.=' etc/mtink
cd ..

# Poster - Poster-printing on stndard sized paper 
cd poster*
%make
cd ..

# HP LaserJet 1000
ln -s %{_libdir}/libjbig.a .
ln -s /usr/include/jbig.h .
gcc -O2 -W -o pbmtozjs pbmtozjs.c libjbig.a
head -34 pbmtozjs.c | tail -33 > pbmtozjs.txt

# Driver for Zenographics-based printers (Minolta magicolor DL series, HP
# LaserJet 1000, 1005, 1018, 1020, 1022, Color LaserJet 1600, 2600)
cd foo2zjs*
# Suppress generation of PDF doc file, it needs GhostScript and GhostScript
# is introduced by this package
#perl -p -i -e "s/all-icc2ps man doc/all-icc2ps man/" Makefile
%make
cd ..

# Driver for Epson EPL "L" series
cd epsonepl*
%configure2_5x
%make
cd ..

# Driver for Lexmark X125 (only printing)
cd drv_x125/src
%make
cd ../..
cd drv_x125_network/src
%make
cd ../..

%ifarch %{ix86}
# Driver for Canon LBP-460/660
cd lbp660*
%make
# Correct PPD files to pass "cupstestppd"
perl -p -i -e "s/DefaultNoReset/DefaultAlwaysReset/" ppd/*.ppd
# Do not generate a log file with fixed name, security problem!
perl -p -i -e "s:/tmp/lbp.60.log:/dev/null:" ppd/*.ppd
cd ..
%endif

# Driver for Canon LBP-810/1120
cd capt*
%make
# Correct PPD files to pass "cupstestppd"
perl -p -i -e "s/DefaultNoReset/DefaultAlwaysReset/g" ppd/*.ppd
# Do not generate a log file with fixed name, security problem!
perl -p -i -e "s:/tmp/capt.log:/dev/null:g" ppd/*.ppd
# Create PPD file for LBP-1120
cp ppd/Canon-LBP-810-capt.ppd ppd/Canon-LBP-1120-capt.ppd
perl -p -i -e "s:LBP-810:LBP-1120:g" ppd/Canon-LBP-1120-capt.ppd
perl -p -i -e "s:lbp810:lbp1120:g" ppd/Canon-LBP-1120-capt.ppd
cd ..

# Driver for Lexmark X74/X75
cd lxx74*
# The source tarball has already all the stuff compiled, but we want to have
# our Mandriva Linux optimizations
%make clean
%make
gunzip lxx74.ppd.gz
cp lxx74.ppd Compaq-IJ670-lxx74.ppd
perl -p -i -e 's/All In One/IJ670/gi' Compaq-IJ670-lxx74.ppd
cp lxx74.ppd Compaq-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet Printer/gi' Compaq-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/Lexmark/Compaq/gi' Compaq-*-lxx74.ppd
cp lxx74.ppd Lexmark-X74-lxx74.ppd
perl -p -i -e 's/All In One/X74/gi' Lexmark-X74-lxx74.ppd
cp lxx74.ppd Lexmark-X75-lxx74.ppd
perl -p -i -e 's/All In One/X75/gi' Lexmark-X75-lxx74.ppd
cp lxx74.ppd Lexmark-X76-lxx74.ppd
perl -p -i -e 's/All In One/X76/gi' Lexmark-X76-lxx74.ppd
cp lxx74.ppd Lexmark-Z13-lxx74.ppd
perl -p -i -e 's/All In One/Z13/gi' Lexmark-Z13-lxx74.ppd
cp lxx74.ppd Lexmark-Z14-lxx74.ppd
perl -p -i -e 's/All In One/Z14/gi' Lexmark-Z14-lxx74.ppd
cp lxx74.ppd Lexmark-Z23-lxx74.ppd
perl -p -i -e 's/All In One/Z23/gi' Lexmark-Z23-lxx74.ppd
cp lxx74.ppd Lexmark-Z33-lxx74.ppd
perl -p -i -e 's/All In One/Z33/gi' Lexmark-Z33-lxx74.ppd
cp lxx74.ppd Lexmark-Z24-lxx74.ppd
perl -p -i -e 's/All In One/Z24/gi' Lexmark-Z24-lxx74.ppd
cp lxx74.ppd Lexmark-Z34-lxx74.ppd
perl -p -i -e 's/All In One/Z34/gi' Lexmark-Z34-lxx74.ppd
cp lxx74.ppd Lexmark-Z25-lxx74.ppd
perl -p -i -e 's/All In One/Z25/gi' Lexmark-Z25-lxx74.ppd
cp lxx74.ppd Lexmark-Z35-lxx74.ppd
perl -p -i -e 's/All In One/Z35/gi' Lexmark-Z35-lxx74.ppd
cp lxx74.ppd Lexmark-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet Printer/gi' Lexmark-Inkjet_Printer-lxx74.ppd
cp lxx74.ppd Lexmark-InkJet_4104-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet 4104/gi' Lexmark-Inkjet_4104-lxx74.ppd
cp lxx74.ppd Samsung-MJC-940-lxx74.ppd
perl -p -i -e 's/All In One/MJC-940/gi' Samsung-MJC-940-lxx74.ppd
cp lxx74.ppd Samsung-MJC-950-lxx74.ppd
perl -p -i -e 's/All In One/MJC-950/gi' Samsung-MJC-950-lxx74.ppd
cp lxx74.ppd Samsung-MJC-2200-lxx74.ppd
perl -p -i -e 's/All In One/MJC-2200/gi' Samsung-MJC-2200-lxx74.ppd
cp lxx74.ppd Samsung-MJC-2130-lxx74.ppd
perl -p -i -e 's/All In One/MJC-2130/gi' Samsung-MJC-2130-lxx74.ppd
cp lxx74.ppd Samsung-MJC-530-lxx74.ppd
perl -p -i -e 's/All In One/MJC-530/gi' Samsung-MJC-530-lxx74.ppd
perl -p -i -e 's/Lexmark/Samsung/gi' Samsung-*-lxx74.ppd
gzip -9 *.ppd
cd ..

# Driver for Minolta magicolor 2300W
cd m2300w*
autoconf
%configure
# Omit the installation of the PPD in the Makefile, we use the Foomatic
# XML data
perl -p -i -e "s/src psfiles foomatic ppd/src psfiles/" Makefile
%make
cd ..

# Driver for Minolta PagePro 12xxW, 13xxW, and 14xxW
cd min12xxw*
%configure
%make
cd ..

# Driver for Casio USB label printers
cd pegg-*
%make
cd ..
cd pegg_el-*/src
%make
cd ../..
cd xbm2crw*
# Nothing to be done
cd ..
cd cups2pegg*/src
# Suppress logging in cups2pegg backend
perl -p -i -e "s:/var/log/cups/cups2pegg.log:/dev/null:" cups2pegg
# Fix PPD file
perl -p -i -e 's/^(\*ModelName:).*$/$1 "CASIO Computer CO. LTD. EL-700 EL-5000W"/' ppd/casio_el.ppd
perl -p -i -e 's/^(\*ShortNickName:).*$/$1 "CASIO EL-700 EL-5000W"/' ppd/casio_el.ppd
perl -p -i -e 's/^(\*ModelName:).*$/$1 "CASIO Computer CO. LTD. KL-P1000 KL-E11"/' ppd/casio_kl.ppd
perl -p -i -e 's/^(\*ShortNickName:).*$/$1 "CASIO KL-P1000 KL-E11"/' ppd/casio_kl.ppd
perl -p -i -e 's/: Letter/: 128_64/' ppd/casio_kl.ppd
perl -p -i -e 's/^(\*ModelName:).*$/$1 "CASIO Computer CO. LTD. KP-C10 KP-C50"/' ppd/casio_kp.ppd
perl -p -i -e 's/^(\*ShortNickName:).*$/$1 "CASIO KP-C10 KP-C50"/' ppd/casio_kp.ppd
perl -p -i -e 's/: Letter/: 512_64/' ppd/casio_kp.ppd
cd ../..

# Drivers for the Konica Minolta magicolor DL series supplied by Konica
# Minolta
for d in magicolor????DL*; do
	cd $d
	%configure
	%make
	cd ..
done
# Add support for the magicolor 2300 DL
cd magicolor2430DL*
gzip -dc src/km_en.ppd.gz | perl -p -e 's:2430(\s*DL):2300$1:g' | gzip > src/km2300dl.ppd.gz
cd ..

# Driver for Brother P-Touch label printers
cd ptouch-driver*
%configure
%make
cd ..

# Driver for Kyocera GDI printers: Kyocera FS-1016MFP
cd foo2kyo*
%make
cd ..

# Driver for Samsung SPL2 printers
cd splix*
%make
# Generate PPD files for each supported printer
cd ppd
for ext in '' 'fr'; do
  cp ml1710$ext.ppd Samsung-SPL2-ml1510$ext.ppd
  perl -p -i -e 's/(ml-?)1710/${1}1510/gi' Samsung-SPL2-ml1510$ext.ppd
  cp ml1710$ext.ppd Samsung-SPL2-ml1520$ext.ppd
  perl -p -i -e 's/(ml-?)1710/${1}1520/gi' Samsung-SPL2-ml1520$ext.ppd
  cp ml1710$ext.ppd Samsung-SPL2-ml1610$ext.ppd
  perl -p -i -e 's/(ml-?)1710/${1}1610/gi' Samsung-SPL2-ml1610$ext.ppd
  cp ml1710$ext.ppd Samsung-SPL2-ml1740$ext.ppd
  perl -p -i -e 's/(ml-?)1710/${1}1740/gi' Samsung-SPL2-ml1740$ext.ppd
  cp ml1710$ext.ppd Samsung-SPL2-ml1750$ext.ppd
  perl -p -i -e 's/(ml-?)1710/${1}1750/gi' Samsung-SPL2-ml1750$ext.ppd
  cp ml2250$ext.ppd Samsung-SPL2-ml2150$ext.ppd
  perl -p -i -e 's/(ml-?)2250/${1}2150/gi' Samsung-SPL2-ml2150$ext.ppd
  cp ml2250$ext.ppd Samsung-SPL2-ml2550$ext.ppd
  perl -p -i -e 's/(ml-?)2250/${1}2550/gi' Samsung-SPL2-ml2550$ext.ppd
  mv ml1710$ext.ppd Samsung-SPL2-ml1710$ext.ppd
  mv ml2010$ext.ppd Samsung-SPL2-ml2010$ext.ppd
  mv ml2250$ext.ppd Samsung-SPL2-ml2250$ext.ppd
done
# Add driver name to NickName in the PPDs
perl -p -i -e 's/(\*NickName:\s*\"[^\,]+)(\,\s*.*?)?/$1, CUPS + SpliX$2/i' *.ppd
cd ..
cd ..


# Tool for reading USB device ID strings
gcc -o usb_id_test usb_id_test.c



%install

rm -rf %{buildroot}
mkdir -p %{buildroot}
exit 0

# Change compiler flags for debugging when in debug mode
%if %debug
export DONT_STRIP=1
export CFLAGS="`echo %optflags |sed -e 's/-O3/-g/' |sed -e 's/-O2/-g/'`"
export CXXFLAGS="`echo %optflags |sed -e 's/-O3/-g/' |sed -e 's/-O2/-g/'`"
export RPM_OPT_FLAGS="`echo %optflags |sed -e 's/-O3/-g/' |sed -e 's/-O2/-g/'`"
%endif


# Make directories
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_libdir}/gimp/2.0/plug-ins
install -d %{buildroot}%{_prefix}/lib/cups/filter
install -d %{buildroot}%{_prefix}/lib/cups/backend
install -d %{buildroot}%{_datadir}/cups/data
install -d %{buildroot}%{_datadir}/cups/model
install -d %{buildroot}%{_sysconfdir}/cups
install -d %{buildroot}%{_datadir}/foomatic/db/source/printer
install -d %{buildroot}%{_datadir}/foomatic/db/source/driver
install -d %{buildroot}%{_datadir}/foomatic/db/source/opt


##### PRINTER FILTERS AND OTHER STUFF

cd $RPM_BUILD_DIR/%{name}-%{mainversion}/printer-filters

# Apple StyleWriter
cd stylewriter
# Program files
install -m 755 lpstyl %{buildroot}%{_bindir}
# Documentation
chmod -R a+rX *
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/AppleStyleWriter
cp -ax scripts Makefile.atalk README* adsp.* printcap.* styl.ppd \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/AppleStyleWriter
cd ..

# Canon CaPSL
cd cjet089
# Program files
install -m 755 cjet %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CanonCaPSL
cp -ax README INSTALL COPYING TODO ChangeLog samples \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CanonCaPSL
cd ..

# Lexmark 1100
cd lm1100*
# Executables (filter for usage with CUPS and printer emulator script for
# development and debugging (also debugging this RPM w/o Lexmark 1100).
install -m 0755 lm1100 %{buildroot}%{_bindir}
install -m 0755 lexmark2ppm.pl %{buildroot}%{_bindir}
install -m 0755 byteutil.pl %{buildroot}%{_bindir}
# LPD support
install -d %{buildroot}%{_libdir}/rhs/rhs-printfilters
[ -e ps-to-lm1100.fpi ] || mv ps-to-printer.fpi ps-to-lm1100.fpi # file name conflict
install -m 0755 ps-to-lm1100.fpi %{buildroot}%{_libdir}/rhs/rhs-printfilters
ln -s %{_bindir}/lm1100 \
	%{buildroot}%{_libdir}/rhs/rhs-printfilters
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark1100
install -m 0644 LICENSE %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark1100
install -m 0644 README %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark1100
install -m 0644 RELEASE.txt %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark1100
install -m 0644 cmy.txt %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark1100
cd ..

# Lexmark 2070 colour
cd c2070-0.99
# Program files
install -m 755 c2070 %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2070colour
cp -ax README LICENSE \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2070colour
cd ..

# Lexmark 2070 grayscale
cd Lexmark2070.latest
# Program files
install -m 755 Lexmark2070 %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2070gray
cp -ax README LICENSE \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2070gray
cd ..

# Lexmark 7xxx, 57xx, Z51
cd lexmark7000linux-990516
# Program and data files
%old_makeinstall
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 CHANGES %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 README %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 lexmark5700-filter %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 lexmark7000-filter %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 lexmark7000linux-990516.lsm %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 lexmarkprotocol.txt %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
install -m 0644 *.p?? %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark7xxx_57xx_Z51
cd ..

# Lexmark Z11
cd lz11*
# Program and data files
install -m 755 cZ11-V2 %{buildroot}%{_bindir}
install -m 755 cZ11 %{buildroot}%{_bindir}
#ln -s %{_bindir}/cZ11-V2 %{buildroot}%{_bindir}/cZ11
install -m 755 cZ11-bit* %{buildroot}%{_bindir}
install -m 755 lz11.[^c]* %{buildroot}%{_bindir}
install -d %{buildroot}/etc/LexmarkZ11/
install -m 644 lz11.conf %{buildroot}/etc/LexmarkZ11/
install -m 644 *.ppd %{buildroot}%{_datadir}/cups/model/
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkZ11
cp -ax README ChangeLog INSTALL \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkZ11
cd ..

# Printer Utility Program
# Program file
#install -m 755 pup_1.1/pup %{buildroot}%{_bindir}
# Documentation
#install -d %{buildroot}%{_docdir}/printer-utils-%{mainversion}/
#install -d %{buildroot}%{_docdir}/printer-utils-%{mainversion}/PUP
#cp -ax pup_1.1/README \
#	%{buildroot}%{_docdir}/printer-utils-%{mainversion}/PUP

# Lexmark printer maintenance
# Program and data files
install -m 755 lxcontrol/lx.control %{buildroot}%{_bindir}
install -m 755 lm1100maint/lm1100change %{buildroot}%{_bindir}
install -m 755 lm1100maint/lm1100back %{buildroot}%{_bindir}
install -m 755 changecartridge %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/lxcontrol
cp -f lxcontrol/*.out %{buildroot}%{_datadir}/lxcontrol/
( cd %{buildroot}%{_bindir}
  ln -s lx.control headclean
  ln -s lx.control headalign
  ln -s lx.control showcartridges
  ln -s lx.control hidecartridges
)
mkdir -p %{buildroot}%{_datadir}/lm1100maint
cp -f lm1100maint/lexmark* \
	%{buildroot}%{_datadir}/lm1100maint/
# Documentation
install -d %{buildroot}%{_docdir}/printer-utils-%{mainversion}/
install -d %{buildroot}%{_docdir}/printer-utils-%{mainversion}/LexmarkMaintenance
cp -ax lxcontrol/README.* lm1100maint/README.* \
	README.changecartridge README.Lexmark-Maintenance \
	%{buildroot}%{_docdir}/printer-utils-%{mainversion}/LexmarkMaintenance

# Install margin and offset adjustment script in /usr/sbin
bzcat %{SOURCE75} > %{buildroot}%{_sbindir}/alignmargins
# Adjust path to improved align.ps 
perl -p -i -e 's:/usr/share/ghostscript/\*/lib/align.ps:%{_datadir}/alignmargins/align.ps:' %{buildroot}%{_sbindir}/alignmargins
# Install improved align.ps
install -d %{buildroot}%{_datadir}/alignmargins/
bzcat %{SOURCE175} > %{buildroot}%{_datadir}/alignmargins/align.ps

# Install a script to display the test page on the screen for colour
# adjustment
cat <<EOF > %{buildroot}%{_bindir}/displaytestpage
#!/bin/sh
ps2img="gs -dQUIET -dNOPAUSE -dBATCH -sDEVICE=pnm -r75x75 -sOUTPUTFILE=- -"
testpage=/usr/share/cups/data/testprint.ps

TMPFILE=~/.displaytestpage.pnm
if [ -x /usr/bin/kview ]; then
  cat \$testpage | \$ps2img > \$TMPFILE 
  /usr/bin/kview \$TMPFILE
elif [ -x /usr/bin/ee ]; then
  cat \$testpage | \$ps2img > \$TMPFILE 
  /usr/bin/ee \$TMPFILE
elif [ -x /usr/bin/gqview ]; then
  cat \$testpage | \$ps2img > \$TMPFILE 
  /usr/bin/gqview \$TMPFILE
elif [ -x /usr/bin/xv ]; then
  cat \$testpage | \$ps2img | /usr/bin/xv -
elif [ -x /usr/bin/kghostview ]; then
  /usr/bin/kghostview \$testpage
elif [ -x /usr/X11R6/bin/gv ]; then
  /usr/X11R6/bin/gv \$testpage
elif [ -x /usr/X11R6/bin/ghostview ]; then
  /usr/X11R6/bin/ghostview \$testpage
else
  xmessage "No suitable program for viewing PostScript found, install GhostView, gv, or similar."
  exit 1
fi
rm \$TMPFILE
EOF
chmod a+rx %{buildroot}/usr/bin/displaytestpage

# Menu entries for printer-utils package
# Menu icon
mkdir -p %{buildroot}%{_datadir}/icons/locolor/16x16/apps/
install -m 644 printutils.png %{buildroot}%{_datadir}/icons/locolor/16x16/apps/
# Menu entries

%if %mdkversion <= 200700
mkdir -p %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/printer-utils
?package(printer-utils): needs=X11 \
section=Configuration/Printing \
title="Mtink - Epson Inkjet Printer Tools" \
longtitle="Epson inkjet printer maintenance (Head cleaning and alignment, ink level display, cartridge change, ...)" \
command="/usr/bin/mtink" \
%if %mdkversion == 200700
xdg=true \
%endif
icon="/usr/share/icons/locolor/16x16/apps/printutils.png" \
?package(printer-utils): needs=X11 \
section=Applications/Monitoring \
title="Mtink - Epson Inkjet Printer Tools" \
longtitle="Epson inkjet printer maintenance (Head cleaning and alignment, ink level display, cartridge change, ...)" \
command="/usr/bin/mtink" \
%if %mdkversion == 200700
xdg=true \
%endif
icon="/usr/share/icons/locolor/16x16/apps/printutils.png"
EOF
%endif

%if %mdkversion >= 200700
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-mtink.desktop << EOF
[Desktop Entry]
Name=Mtink - Epson Inkjet Printer Tools
Comment=Epson inkjet printer maintenance (Head cleaning and alignment, ink level display, cartridge change, ...)
Exec=/usr/bin/mtink
Icon=printutils
Terminal=false
Type=Application
%if %mdkversion >= 200800
Categories=System;Monitor;
%else
Categories=X-MandrivaLinux-System-Configuration-Printing;Settings;HardwareSettings;X-MandrivaLinux-System-Monitoring;System;Monitor;
%endif
EOF
%endif

# HP DeskJet PPA printers
cd pnm2ppa-*
install -m 0644  docs/en/pnm2ppa.1 %{buildroot}%{_mandir}/man1
%old_makeinstall BINDIR=%{buildroot}%{_bindir} CONFDIR=%{buildroot}%{_sysconfdir} MANDIR=%{buildroot}%{_mandir}/man1
install -m 0755 utils/Linux/detect_ppa %{buildroot}%{_bindir}
install -m 0755 utils/Linux/test_ppa %{buildroot}%{_bindir}
install -d  %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pnm2ppa
install -m 0644 *.ps %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pnm2ppa
cd docs/en
for file in * ; do
  if  [ -f $file ] ; then
     install -m 0644  $file %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pnm2ppa
  fi
done
rm -f %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pnm2ppa/pnm2ppa.1
cd ../..
cp -ax ppa_protocol rhs-printfilters sample_scripts README.security Changelog %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pnm2ppa
cd ..
cd pbm2ppa-0.8.6
install -m 0755 pbm2ppa  %{buildroot}%{_bindir}
install -m 0755 pbmtpg   %{buildroot}%{_bindir}
install -m 0644 pbm2ppa.conf   %{buildroot}%{_sysconfdir}
install -m 0644 pbm2ppa.1   %{buildroot}%{_mandir}/man1
install -d  %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pbm2ppa
for file in CALIBRATION CREDITS INSTALL INSTALL-MORE LICENSE README ; do
  if [ -f $file ] ; then
    install -m 0644  $file %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA/pbm2ppa
  fi
done
cd ..
install -m 0644 README.calibration %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPDeskJetPPA

# Lexmark 2050
cd c2050-0.4
# Program file
install -m 0755 c2050 %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2050
cp -ax README COPYING ps2lexmark \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2050
cd ..

# Lexmark 2030
cd pbm2l2030
# Program file
install -m 0755 pbm2l2030 %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2030
cp -ax README.TXT LICENSE \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/Lexmark2030
cd ..

# Okipage 4w and compatible winprinters
cd oki4linux-2.0/src
# Program files
install -m 0755 oki4drv %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -m 0755 oki4daemon %{buildroot}%{_sbindir}
cd ../..
install -d %{buildroot}%{_initrddir}
install -m 0755 oki4daemon %{buildroot}%{_initrddir}
#install -m 0755 oki4w_install %{buildroot}%{_sbindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/OKI-Winprinters
#cp -ax README.OKI-Winprinters \
#	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/OKI-Winprinters
cd oki4linux-2.0
cp -ax COPYING ChangeLog README crack doc samples \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/OKI-Winprinters
cd src
cp -ax README.oki4daemon align.ps oki4daemon.init \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/OKI-Winprinters
install -m 0644 oki4drv.man %{buildroot}%{_mandir}/man1/oki4drv.1
cd ../..

# Citizen Printiva 600C
cd ppmtocpva-1.0
# Program files
install -m 0755 ppmtocpva %{buildroot}%{_bindir}
install -m 0755 cpva-colour %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CitizenPrintiva600C
cp -ax README \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CitizenPrintiva600C
cd ..

# CoStar and compatible label printers
cd pbm2lwxl
# Program file
install -m 0755 *2lwxl %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/DymoCoStarAvery-LabelPrinters
cp -ax README *.html \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/DymoCoStarAvery-LabelPrinters
cd ..

%ifarch %{ix86}
# Samsung ML-85G and QL-85G winprinters
cd ml85p-*
# Program file
install -m 4750 ml85p %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/SamsungML-85G
cp -ax COPYING NEWS README THANKS ml85-print ml85-test ml85p-*.lsm \
	printcap \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/SamsungML-85G
cd ..
%endif

# Filter for the Lexmark Z42
cd drv_z42/src
# Program file
install -s -m 755 z42_cmyk %{buildroot}%{_bindir}
cd ../z42tool/
%makeinstall
cd ..
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkZ42
cp -ax COPYING README FAQ ChangeLog \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkZ42
cp -ax z42tool/README \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkZ42/README.z42tool
cd ..

# GhostScript wrapper for the Pentax PocketJet printers
cd pentaxpj
# Program files
install -d %{buildroot}%{_libdir}/pentaxpj
cp -a BWidget-1.3.1 pentaxpj pentaxsetup pentax.xpm test-page.ps.gz\
	%{buildroot}%{_libdir}/pentaxpj
ln -s %{_libdir}/pentaxpj/pentaxsetup %{buildroot}%{_sbindir}
ln -s %{_libdir}/pentaxpj/pentaxpj %{buildroot}%{_bindir}
cat > %{buildroot}%{_sysconfdir}/pentaxpj.conf <<EOF
#
set settings(driverpath) %{_libdir}/pentaxpj
EOF
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/PentaxPocketJet
cp -ax README \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/PentaxPocketJet
cd ..

# Unix driver for MicroDry Printers
cd ppmtomd*
# Program files
install -m 0755 ppmtomd %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/MicroDryPrinters
cp -ax LICENCE \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/MicroDryPrinters
cp ppmtomd.man %{buildroot}%{_mandir}/man1/ppmtomd.1
cd ..

# Mtink - Printer maintenance/ink monitoring for Epson inkjets
cd mtink*
# Program files
install -d %{buildroot}%{_prefix}/lib/cups/backend
install -m 0755 mtink %{buildroot}%{_bindir}
install -m 0755 ttink %{buildroot}%{_bindir}
install -m 0755 mtinkc %{buildroot}%{_bindir}
install -m 0755 mtinkd %{buildroot}%{_sbindir}
install -m 0755 etc/mtink %{buildroot}%{_initrddir}
install -m 0755 etc/installInitScript.sh %{buildroot}%{_sbindir}/mtink-installInitScript
install -m 0755 detect/askPrinter %{buildroot}%{_sbindir}
install -m 0755 etc/mtink-cups %{buildroot}%{_prefix}/lib/cups/backend/mtink
install -m 0755 gimp-mtink %{buildroot}%{_libdir}/gimp/2.0/plug-ins/
install -d %{buildroot}/var/mtink
# Documentation
install -d %{buildroot}%{_docdir}/printer-utils-%{mainversion}/EpsonInkjetMaintenance
cp -ax CHANGE.LOG doc/* \
	%{buildroot}%{_docdir}/printer-utils-%{mainversion}/EpsonInkjetMaintenance
cp -ax etc/readme %{buildroot}%{_docdir}/printer-utils-%{mainversion}/EpsonInkjetMaintenance/README.mtinkd.startup
cd ..

# Poster - Poster-printing on stndard sized paper 
cd poster*
# Program files
install -m 0755 poster %{buildroot}%{_bindir}
# Documentation
cp poster.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_docdir}/printer-utils-%{mainversion}/PosterPrinting
cp -ax ChangeLog README COPYING \
	%{buildroot}%{_docdir}/printer-utils-%{mainversion}/PosterPrinting
cd ..

# Driver for HP LaserJet 1000

# Program files
install -m 0755 pbmtozjs %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPLaserJet1000
cp -ax pbmtozjs.txt \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/HPLaserJet1000

# Driver for Zenographics-based printers (Minolta magicolor DL series, HP
# LaserJet 1000, 1005, 1018, 1020, 1022, Color LaserJet 1600, 2600)
cd foo2zjs*
# Program files
install -m 0755 foo2zjs %{buildroot}%{_bindir}
install -m 0755 foo2zjs-wrapper %{buildroot}%{_bindir}
install -m 0755 foo2hp %{buildroot}%{_bindir}
install -m 0755 foo2hp2600-wrapper %{buildroot}%{_bindir}
install -m 0755 zjsdecode %{buildroot}%{_bindir}
install -m 0755 arm2hpdl %{buildroot}%{_bindir}
install -m 0755 okidecode %{buildroot}%{_bindir}
%if %mdkversion < 200700
install -m 0755 msexpand %{buildroot}%{_bindir}
%endif
#install -m 0755 jbg2pbm %{buildroot}%{_bindir}
install -m 0755 getweb %{buildroot}%{_bindir}/foo2zjs-getweb
install -m 0755 icc2ps/foo2zjs-icc2ps %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/foo2zjs
install -d %{buildroot}%{_datadir}/foo2hp
install -d %{buildroot}%{_datadir}/foo2zjs/crd
install -d %{buildroot}%{_datadir}/foo2hp/psfiles
install -m 0644 gamma*.ps %{buildroot}%{_datadir}/foo2zjs
cp crd/*.* %{buildroot}%{_datadir}/foo2zjs/crd
cp crd/*.ps %{buildroot}%{_datadir}/foo2hp/psfiles
install -m 0755 usb_printerid %{buildroot}%{_sbindir}
install -m 0755 hplj1000 %{buildroot}%{_sbindir}
perl -p -i -e 's:\./(getweb):foo2zjs-$1:g' %{buildroot}%{_sbindir}/hplj1000
perl -p -i -e 's:/bin(/usb_printerid):%{_sbindir}$1:g' %{buildroot}%{_sbindir}/hplj1000
ln -s %{_sbindir}/hplj1000 %{buildroot}%{_sbindir}/hplj1005
ln -s %{_sbindir}/hplj1000 %{buildroot}%{_sbindir}/hplj1018
ln -s %{_sbindir}/hplj1000 %{buildroot}%{_sbindir}/hplj1020
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
install -m 0644 hplj10xx.rules %{buildroot}%{_sysconfdir}/udev/rules.d/70-hplj10xx.rules
perl -p -i -e 's:/etc/hotplug/usb:%{_sbindir}:' %{buildroot}%{_sysconfdir}/udev/rules.d/70-hplj10xx.rules
for dir in driver opt; do \
install -c -m 644 foomatic-db/$dir/foo2[hz]*.xml \
	%{buildroot}%{_datadir}/foomatic/db/source/$dir/; \
done
install -d %{buildroot}%{_datadir}/foo2zjs/icm
install -d %{buildroot}%{_datadir}/foo2hp/icm
ln -s /etc/printer %{buildroot}%{_datadir}/foo2zjs/firmware
ln -s /etc/printer %{buildroot}%{_datadir}/firmware
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/foo2zjs
cp -ax COPYING ChangeLog INSTALL INSTALL.usb README \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/foo2zjs
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/foo2zjs/icc2ps
cp -ax icc2ps/[ACR]* \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/foo2zjs/icc2ps
cp foo2[hz]*.1 zjs*.1 %{buildroot}%{_mandir}/man1/
cd ..

# Driver for Epson EPL "L" series
cd epsonepl*
# Program files
%makeinstall
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/EpsonEPL_L_Series
cp -ax ChangeLog epl_docs FAQ LIMITATIONS README \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/EpsonEPL_L_Series
cd ..

# Driver for Lexmark X125 (only printing)
# Program files
install -m 0755 drv_x125/src/x125_cmyk %{buildroot}%{_bindir}
install -m 0755 drv_x125/src/x125_cmyk_print.sh %{buildroot}%{_bindir}
install -m 0755 drv_x125_network/src/x125_network %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkX125
cd drv_x125
cp -ax ChangeLog FAQ INSTALL LICENSE README src/*.ps \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkX125
cd ..
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkX125/drv_x125_network
cd drv_x125_network
cp -ax ChangeLog FAQ INSTALL LICENSE README \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/LexmarkX125/drv_x125_network
cd ..

%ifarch %{ix86}
# Driver for Canon LBP-460/660
cd lbp660*
# Program files
install -m 0755 lbp660 %{buildroot}%{_bindir}
install -m 0755 lbp[46]60-* %{buildroot}%{_bindir}
# PPD files
install -d %{buildroot}%{_datadir}/cups/model/lbp660
cp ppd/*.ppd %{buildroot}%{_datadir}/cups/model/lbp660
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CanonLBP-460-660
cp -ax COPYING NEWS README THANKS TODO \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CanonLBP-460-660
cd ..
%endif

# Driver for Canon LBP-810/1120
cd capt*
# Program files
install -m 0755 capt %{buildroot}%{_bindir}
install -m 0755 capt-* %{buildroot}%{_bindir}
# PPD files
install -d %{buildroot}%{_datadir}/cups/model/capt
cp ppd/*.ppd %{buildroot}%{_datadir}/cups/model/capt
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CanonLBP-810-1120
cp -ax COPYING NEWS README SPECS THANKS TODO \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CanonLBP-810-1120
cd ..

# Driver for Lexmark X74/X75
cd lxx74*
# Program files
install -m 0755 rastertolxx74 %{buildroot}%{_prefix}/lib/cups/filter/rastertolxx74.bin
install -m 0644 self-portrait.out.gz %{buildroot}%{_datadir}/cups/data/self-portrait.out.gz
cat << EOF > %{buildroot}%{_prefix}/lib/cups/filter/rastertolxx74
#!/bin/bash
export self_portrait="%{_datadir}/cups/data/self-portrait.out.gz"
exec %{_prefix}/lib/cups/filter/rastertolxx74.bin "\$@"
EOF
chmod 755 %{buildroot}%{_prefix}/lib/cups/filter/rastertolxx74
install -m 0644 lxx74.types %{buildroot}%{_sysconfdir}/cups
install -m 0644 lxx74.convs %{buildroot}%{_sysconfdir}/cups
# PPD files
install -d %{buildroot}%{_datadir}/cups/model/lxx74
cp *.ppd* %{buildroot}%{_datadir}/cups/model/lxx74
# Documentation
#install -d %{buildroot}%{_docdir}/cups-drivers-%{mainversion}/LexmarkX74X75
#cp -ax INSTALL LICENSE README lpoptions \
#	%{buildroot}%{_docdir}/cups-drivers-%{mainversion}/LexmarkX74X75
cd ..

# Driver for Minolta magicolor 2300W
cd m2300w*
%makeinstall INSTROOT=%{buildroot}
for dir in driver opt; do \
install -c -m 644 foomatic/$dir/*.xml \
	%{buildroot}%{_datadir}/foomatic/db/source/$dir/; \
done
# Move documentation to the correct place
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/
mv %{buildroot}%{_docdir}/m2300w* %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/MinoltaMagicolor2300W
cd ..

# Driver for Minolta PagePro 12xxW, 13xxW, and 14xxW
cd min12xxw*
# Program files
install -m 0755 min12xxw %{buildroot}%{_bindir}
install -m 0755 esc-m %{buildroot}%{_bindir}
# Documentation
install -m 0644 min12xxw.1* %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/MinoltaPagePro12xxW_13xxW_14xxW
cp -ax COPYING README ChangeLog FAQ INSTALL NEWS format.txt usblogs \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/MinoltaPagePro12xxW_13xxW_14xxW
cd ..

# Driver for Casio USB label printers
cd pegg-*
# Program files
install -m 0755 pegg %{buildroot}%{_bindir}
# Documentation
install -m 0644 pegg.1.gz %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CasioUSBLabelPrinters/pegg
cp -ax LICENSE README CHANGELOG INSTALL test_raw \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CasioUSBLabelPrinters/pegg
cd ..
cd pegg_el-*/src
# Program files
install -m 0755 pegg_el %{buildroot}%{_bindir}
# Documentation
install -m 0644 pegg_el.1.gz %{buildroot}%{_mandir}/man1
cd ..
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CasioUSBLabelPrinters/pegg_el
cp -ax TODO LICENSE README INSTALL src/test_raw \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CasioUSBLabelPrinters/pegg_el
cd ..
cd xbm2crw*
# Program files
install -m 0755 xbm2crw %{buildroot}%{_bindir}
#install -m 0755 html2crw.sh %{buildroot}%{_bindir}
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CasioUSBLabelPrinters/xbm2crw
cp -ax LICENSE README template.xbm \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/CasioUSBLabelPrinters/xbm2crw
cd ..
cd cups2pegg*/src
# Program files
install -m 0755 cups2pegg %{buildroot}%{_prefix}/lib/cups/backend
# PPD files
install -d %{buildroot}%{_datadir}/cups/model/pegg
cp ppd/*.ppd* %{buildroot}%{_datadir}/cups/model/pegg
cd ..
# Documentation
install -d %{buildroot}%{_docdir}/cups-drivers-%{mainversion}/CasioUSBLabelPrinters/cups2pegg
cp -ax LICENSE *.html *.png \
	%{buildroot}%{_docdir}/cups-drivers-%{mainversion}/CasioUSBLabelPrinters/cups2pegg
cd ..

# Drivers for the Konica Minolta magicolor DL series supplied by Konica
# Minolta
for d in magicolor????DL*; do
	cd $d
	# Program files
	make DESTDIR=%{buildroot} install
	# Documentation
	n=`echo $d | perl -e '$s = <>; $s =~ /magicolor(\d+)DL/i; print "$1"'`
	install -d %{buildroot}%{_docdir}/cups-drivers-%{mainversion}/KonicaMinoltaMagicolor${n}DL
	cp -ax AUTHORS COPYING ChangeLog kmlf.spec \
	%{buildroot}%{_docdir}/cups-drivers-%{mainversion}/KonicaMinoltaMagicolor${n}DL
	cd ..
done
rm -f %{buildroot}%{_datadir}/KONICA_MINOLTA/*/COPYING
install -m 644 magicolor2430DL*/src/km2300dl.ppd.gz %{buildroot}%{_datadir}/cups/model/KONICA_MINOLTA

# Driver for Brother P-Touch label printers
cd ptouch-driver*
# Program files
install -m 0755 rastertoptch %{buildroot}%{_bindir}
# Foomatic data
for dir in driver opt; do \
install -c -m 644 $dir/*.xml \
	%{buildroot}%{_datadir}/foomatic/db/source/$dir/; \
done
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/BrotherPTouch
cp AUTHORS ChangeLog COPYING INSTALL NEWS README %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/BrotherPTouch
cd ..

# Driver for Kyocera GDI printers: Kyocera FS-1016MFP
cd foo2kyo*
# Program files
install -m 0755 foo2kyo %{buildroot}%{_bindir}
install -m 0755 foo2kyo-wrapper %{buildroot}%{_bindir}
for dir in driver opt; do \
install -c -m 644 foomatic-db/$dir/foo2kyo*.xml \
	%{buildroot}%{_datadir}/foomatic/db/source/$dir/; \
done
# Documentation
install -d %{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/foo2kyo
cp -ax COPYING jbig.doc \
	%{buildroot}%{_docdir}/printer-filters-doc-%{mainversion}/foo2kyo
cd ..

# Driver for Samsung SPL2 printers
cd splix*
# Program files
install -m 755 -s src/rastertospl2 %{buildroot}%{_prefix}/lib/cups/filter/
# PPD files
install -d %{buildroot}%{_datadir}/cups/model/samsung
cp ppd/*.ppd* %{buildroot}%{_datadir}/cups/model/samsung
# Documentation
install -d %{buildroot}%{_docdir}/cups-drivers-%{mainversion}/SamsungSPL2
cp -ax AUTHORS ChangeLog COPYING INSTALL README TODO \
	%{buildroot}%{_docdir}/cups-drivers-%{mainversion}/SamsungSPL2
cd ..


# Tool for uploading the firmware on the HP LaserJet 1000S
install -m 0755 hp1000fw %{buildroot}%{_bindir}
# Make hp1000fw called by udev
#mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
#install -m 0644 udev-hp1000fw.rules %{buildroot}%{_sysconfdir}/udev/rules.d/70-hp1000fw.rules

install -d %{buildroot}%{_sysconfdir}/printer
# Tools for reading USB device ID strings
install -m 0755 usb_id_test %{buildroot}%{_bindir}
install -m 0755 getusbprinterid %{buildroot}%{_bindir}



##### GENERAL STUFF

# Correct permissions of PPD file directory
chmod -R u+w,a+rX %{buildroot}%{_datadir}/cups/model

# "cleanppd.pl" removes unwished PPD files fixes broken manufacturer
# entries, and cleans lines which contain only spaces and tabs.

# Uncompress Perl script for cleaning up the PPD files
bzcat %{SOURCE201} > ./cleanppd.pl
chmod a+rx ./cleanppd.pl
# Do the clean-up
find %{buildroot}%{_datadir}/cups/model -name "*.ppd" -exec ./cleanppd.pl '{}' \;
# Remove PPDs which are not Adobe-compliant and therefore not working with
# CUPS 1.1.20
for ppd in `find %{buildroot}%{_datadir}/cups/model -name "*.ppd.gz" -print`; do cupstestppd -q $ppd || (rm -f $ppd && echo "$ppd not Adobe-compliant. Deleted."); done

# Correct permissions for all documentation files
chmod -R a+rX %{buildroot}%{_docdir}
chmod -R go-w %{buildroot}%{_docdir}
chmod -R u+w %{buildroot}%{_docdir}



##### FILES

%files -n printer-filters

%files -n printer-filters-doc

%files -n printer-utils

%files -n cups-drivers

%clean
rm -rf %{buildroot}


