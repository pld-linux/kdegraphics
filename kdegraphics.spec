# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.

%define		_state		stable
%define		_ver		3.2.3

Summary:	K Desktop Environment - Graphic Applications
Summary(es):	K Desktop Environment - aplicaciones gráficas
Summary(pl):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - Aplicações gráficas
Name:		kdegraphics
Version:	%{_ver}
Release:	1
Epoch:		9
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	af7092f2afc5a8565eb5017ecee6b67e
Patch100:	%{name}-branch.diff
Patch0:		%{name}-vcategories.patch
Patch1:		%{name}-gcc34.patch
BuildRequires:	ed
BuildRequires:	unsermake >= 040511
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	fontconfig-devel
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	gettext-devel
BuildRequires:	imlib-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libgphoto2-devel
BuildRequires:	libieee1284-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	lockdev-devel
BuildRequires:	sane-backends-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildConflicts:	kdegraphics-mrml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Graphic applications for the K Desktop Environment.

Included with this package are:

- Kamera - digital camera support
- KColorEdit - color palette editor
- KColorChooser - color chooser
- KDVI - displays TeX's device independent (.dvi) files,
- KFax - displays fax files,
- KFract - a fractal generator,
- KGhostview - displays postscript (.ps) files,
- KIconedit - icon editor,
- Kooka - a scanning tool
- KPaint - a simple drawing program,
- KRuler - a screen ruler
- KSnapshot - screen capture,
- KuickShow - an image viewer
- KView - displays numerous graphic file formats.

%description -l es
Aplicaciones gráficas para KDE.

Incluidos en este paquete:
- KDVI - visualiza archivos TeX's independientes de dispositivo,
- KFax - visualiza archivos de fax,
- KFract - creador de fractal
- KGhostview - visualiza archivos postscript (.ps),
- KPaint - un programa sencillo de dibujo,
- KView - visualiza numerosos formatos de archivos gráficos.

%description -l pl
Aplikacje graficzne dla KDE.

Pakiet zawiera programy:

- Kamera - obs³uga kamer cyfrowych
- KDVI - przegl±darka plików DVI,
- KColorEdit - edytor palety kolorów
- KColorChooser - wybór koloru
- KFax - program do wy¶wietlania faksów,
- KFract - generator fraktali,
- KGhostview - program do ogl±dania postscriptu (.ps),
- KIconedit - program do edycji ikon dla KDE,
- KPaint - prosty program do grafiki rastrowej,
- KRuler - linijka ekranowa
- KSnapshot - program do przechwytywania wygl±du ekranu,
- KuickShow - przegl±darka plików graficznych.
- KView - przegl±darka plików graficznych.

%description -l pt_BR
Aplicações gráficas para o KDE.

Incluídos neste pacote:
- KDVI - visualiza arquivos TeX's independentes de dispositivo,
- KFax - visualiza arquivos de fax,
- KFract - gerador de fractal,
- KGhostview - visualiza arquivos postscript (.ps),
- KPaint - um programa simples de desenho,
- KView - visualiza numerosos formatos de arquivos gráficos.

%package devel
Summary:	kdegraphics development files
Summary(pl):	Pliki dla programistów kdegraphics
Summary(pt_BR):	Arquivos de inclusão para compilação de aplicações com kdegraphics
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-kooka = %{epoch}:%{version}-%{release}
Requires:	%{name}-ksvg = %{epoch}:%{version}-%{release}
Requires:	%{name}-kview = %{epoch}:%{version}-%{release}

%description devel
kdegraphics development files.

%description devel -l pl
Pliki dla programistów kdegraphics.

%description devel -l pt_BR
Arquivos de inclusão para compilação de aplicações que usem as
bibliotecas do kdegraphics.

%package daemonwatcher
Summary:	KDED Daemon Watcher
Summary(pl):	Stra¿nik demona KDED
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdegraphics-mrml < 8:3.1-6

%description daemonwatcher
Starts daemons on demand and restarts them on failure.

%description daemonwatcher -l pl
Uruchamia demony na ¿±danie lub restartuje je po awarii.

%package kamera
Summary:	Digital camera support
Summary(pl):	Obs³uga kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kamera
kamera is an IO slave and a KControl panel module which allows you to
access folders and images within any digital camera supported by the
upcoming gPhoto2 libraries. If you have a supported camera, you can
start using it with most KDE applications in two easy steps: simply
configure your camera model and port type from a list in KControl,
then start accessing the camera contents with a kamera:/ URL.

%description kamera -l pl
Obs³uga kamer cyfrowych.

%package kcolorchooser
Summary:	Color chooser
Summary(pl):	Program do wybierania kolorów
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdegraphics

%description kcolorchooser
Color chooser.

%description kcolorchooser -l pl
Program do wybierania kolorów.

%package kcoloredit
Summary:	Color palette editor
Summary(pl):	Edytor palety kolorów
Summary(pt_BR):	Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kcoloredit
KColorEdit is a palette files editor. It can be used for editing color
palettes and for color choosing and naming.

%description kcoloredit -l pl
Edytor palety kolorów.

%description kcoloredit -l pt_BR
Editor de cores do KDE.

%package kdvi
Summary:	KDE DVI viewer
Summary(pl):	Przegl±darka plików DVI dla KDE
Summary(pt_BR):	Programa de exibição de DVIs
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-kview = %{epoch}:%{version}-%{release}
Obsoletes:	kdegraphics

%description kdvi
KDVI is a plugin for the KViewshell program which allows KViewshell to
display DVI-files (.dvi) which are produced by the TeX typesetting
system. KDVI supports many extensions of the DVI standard, for
instance the inclusion of PostScript graphics or hyperlinks.

%description kdvi -l pl
Program do przegl±dania plików DVI.

%description kdvi -l pt_BR
Programa de exibição de DVIs.

%package kfax
Summary:	KDE Fax viewer
Summary(pl):	Przegl±darka faksów dla KDE
Summary(pt_BR):	Programa de visualização de faxes (formato TIFF)
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-kview = %{epoch}:%{version}-%{release}
Obsoletes:	kdegraphics

%description kfax
KFax is a Fax file viewer capable of displaying and printing all
common fax file formats. In particular the fax files used by popular
the mgetty/sendfax and hylafx fax send and receive packages can be
displayed. The first (or only) page of a "PC-Research"-style (DigiFAX)
files produced by the ghostscript dfaxhigh or dfaxlow drivers can also
be displayed. (who is still using this format?) Input files using any
common fax encoding such as group 3 (1 and 2 dimensional) and group 4
can be displayed. KFax has built in native postscript printing
capabilities.

%description kfax -l pl
Program ten umo¿liwia przegl±danie plików faksowych (G3).

%description kfax -l pt_BR
Programa de visualização de faxes (formato TIFF).

%package kfile
Summary:	Graphic formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach graficznych
Group:		X11/Applications/Graphics
Requires:	konqueror >= %{version}
Obsoletes:	kdegraphics

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³a¶ciwo¶ci pliku" konquerora
dodatkow± zak³adkê z rozszerzonymi informacjami o pliku.

%package kgamma
Summary:	A monitor calibration tool
Summary(pl):	Narzêdzie do kalibracji monitora
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kgamma
A monitor calibration tool.

%description kgamma -l pl
Narzêdzie do kalibracji monitora.

%package kghostview
Summary:	KDE Postscript viewer
Summary(pl):	Przegl±darka postscriptu dla KDE
Summary(pt_BR):	Programa de visualização de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Requires:	ghostview
Obsoletes:	kdegraphics

%description kghostview
KGhostView displays and prints PostScript (.ps, .eps) and Portable
Document Format (.pdf) files. It a port to KDE of Tim Theisen's
Ghostview program which uses Alladin Ghostscript to view documents
prepared in Adobe's PostScript page description language. PostScript
is the major page description language for printing on UNIX systems
and this application can be used to preview material intended for
printing or for reading documents online.

%description kghostview -l pl
Program ten umo¿liwia przegl±danie plików postscriptowych (.ps).

%description kghostview -l pt_BR
Programa de visualização de arquivos Postscript e PDF.

%package kiconedit
Summary:	KDE Icon Editor
Summary(pl):	Edytor ikon dla ¶rodowiska KDE
Summary(pt_BR):	Editor de ícones
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kiconedit
KDE Icon editor.

%description kiconedit -l pl
Edytor ikon dla KDE.

%description kiconedit -l pt_BR
Editor de ícones, lida inclusive com arquivos .ICO.

%package kooka
Summary:	Scanning tool
Summary(pl):	Narzêdzie do skanowania
Summary(pt_BR):	Um programa de rasterização de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kooka
Kooka is a KDE application that enables easy scanning using SANE
libraries.

%description kooka -l pl
Narzêdzie do skanowania.

%description kooka -l pt_BR
Um programa de rasterização de imagens, baseado no SANE e libkscan.

%package kpaint
Summary:	KDE Painter
Summary(pl):	Program graficzny KDE
Summary(pt_BR):	Editor básico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kpaint
A (very) simple painting program for KDE.

%description kpaint -l pl
(Bardzo) prosty program do rysowania pod KDE.

%description kpaint -l pt_BR
Editor básico de imagens bitmap.

%package kpdf
Summary:	Kpdf is an xpdf wrapper for KDE
Summary(pl):	Kpdf - program udostêpniaj±cy mo¿liwo¶ci xpdf w KDE
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kpdf
Kpdf is an xpdf wrapper for KDE.

%description kpdf -l pl
Kpdf udostêpnia mo¿liwo¶ci xpdf w KDE.

%package kpovmodeler
Summary:	Povary Modeler
Summary(pl):	Modeler Povary
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Requires:	povray
Obsoletes:	kdegraphics

%description kpovmodeler
Modeler for POV-Ray scenes.

%description kpovmodeler -l pl
Modeler do scen POV-Raya.

%package kruler
Summary:	KRuler
Summary(pl):	Linijka dla KDE
Summary(pt_BR):	Régua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl
KRuler jest prost± aplikacj±, z tylko jednym celem w ¿yciu: mierzenie
odleg³o¶ci na ekranie.

%description kruler -l pt_BR
Régua de pixels para a tela.

%package ksnapshot
Summary:	KDE Snap Shot
Summary(pl):	Program do przechwytywania ekranu dla KDE
Summary(pt_BR):	Programa de captura de tela
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description ksnapshot
KSnapshot is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description ksnapshot -l pl
Program do przechwytywania ekranu dla KDE.

%description ksnapshot -l pt_BR
Programa de captura de tela.

%package ksvg
Summary:	Scalable Vector Graphics for KDE
Summary(pl):	Skalowalna grafika wektorowa (SVG) dla KDE
Group:		X11/Applications/Graphics
#Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics

%description ksvg
KSVG is a KDE implementation of the Scalable Vector Graphics
Specifications.

%description ksvg -l pl
KSVG stanowi implementacjê dla KDE specyfikacji skalowalnej grafiki
wektorowej (SVG - Scalable Vector Graphics).

%package kuickshow
Summary:	Image viewer/browser
Summary(pl):	Przegl±darka obrazków
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Provides:	kuickshow
Obsoletes:	kuickshow
Obsoletes:	kdegraphics

%description kuickshow
KuickShow is a comfortable image browser/viewer. It displays a
filebrowser where you can select images which are then shown. The
following image formats are supported: jpg, gif, tiff, png, bmp, psd,
xmp, xbm, eim. Images can be displayed either in their own window, as
large as the image, or fullscreen.


%description kuickshow -l pl
Przegl±darka obrazków.

%package kview
Summary:	KDE graphics file viewer
Summary(pl):	Przegl±darka plików graficznych dla KDE
Summary(pt_BR):	Visualizador de imagens
Group:		X11/Applications/Graphics
#Requires:	kdebase-core >= 9:%{version}
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdegraphics

%description kview
KView is an image viewer for the KDE desktop. You can view graphics of
many different formats such as PostScript, TIFF etc. By saving your
files in a different format than the original you can easily convert
images to other graphics formats. In addition, KView provides some
nice little features for doing simple image processing, like
stretching/shrinking, rotation and filtering. You can tile your images
directly onto the desktop as a background picture, or arrange them in
a little slideshow.

%description kview -l pl
Program ten umo¿liwia ogl±danie ró¿nych plików graficznych.

%description kview -l pt_BR
Visualizador de imagens poderoso para KDE.

%package kmrml
Summary:	Advanced Search
Summary(pl):	Zaawansowane wyszukiwanie
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-mrml

%description kmrml
This package provides graphics files advanced search with file
indexing.

%description kmrml -l pl
Ten pakiet umo¿liwia zaawansowane wyszukiwanie plików graficznych z
indeksowaniem plików.

%prep
%setup -q
%patch100 -p1
%patch0 -p1
%patch1 -p1

%build
cp -f %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/Peripherals/kamera.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	kooka		-p /sbin/ldconfig
%postun	kooka		-p /sbin/ldconfig

%post	ksvg		-p /sbin/ldconfig
%postun	ksvg		-p /sbin/ldconfig

%post	kview		-p /sbin/ldconfig
%postun	kview		-p /sbin/ldconfig


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkscan.so
%attr(755,root,root) %{_libdir}/libkmultipage.so
%attr(755,root,root) %{_libdir}/libkimageviewer.so
%attr(755,root,root) %{_libdir}/libksvg.so
%attr(755,root,root) %{_libdir}/libtext2path.so
%{_includedir}/*.h
%{_includedir}/dom/*
%{_includedir}/ksvg
%{_includedir}/libtext2path-0.1

%files daemonwatcher
%defattr(644,root,root,755)
%{_libdir}/kde3/kded_daemonwatcher.la
%attr(755,root,root) %{_libdir}/kde3/kded_daemonwatcher.so
%{_datadir}/services/kded/daemonwatcher.desktop

%files kamera
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kamera.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kamera.so
%{_libdir}/kde3/kio_kamera.la
%attr(755,root,root) %{_libdir}/kde3/kio_kamera.so
%{_datadir}/services/kamera.protocol
%{_desktopdir}/kde/kamera.desktop
%{_iconsdir}/*/*/*/camera*
%{_kdedocdir}/en/kamera

%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_desktopdir}/kde/kcolorchooser.desktop
%{_iconsdir}/crystalsvg/*/apps/kcolorchooser.png
%{_mandir}/man1/kcolorchooser.1*

%files kcoloredit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_datadir}/apps/kcoloredit
%{_desktopdir}/kde/kcoloredit.desktop
%{_iconsdir}/[!l]*/*/*/kcoloredit.*
%{_mandir}/man1/kcoloredit.1*
%{_kdedocdir}/en/kcoloredit

%files kdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdvi
%{_libdir}/kde3/kdvipart.la
%attr(755,root,root) %{_libdir}/kde3/kdvipart.so
%{_datadir}/apps/kdvi/
%{_desktopdir}/kde/kdvi.desktop
%{_iconsdir}/*/*/*/kdvi.*
%{_mandir}/man1/kdvi.1*
%{_kdedocdir}/en/kdvi

%files kfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%{_libdir}/kde3/kfaxpart.la
%attr(755,root,root) %{_libdir}/kde3/kfaxpart.so
%{_datadir}/apps/kfax/
%{_desktopdir}/kde/kfax.desktop
%{_iconsdir}/*/*/*/kfax.*
%{_mandir}/man1/kfax.1*

%files kfile
%defattr(644,root,root,755)
%{_libdir}/kde3/kfile_*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/kfile_*.desktop

%files kgamma
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xf86gammacfg
%{_libdir}/kde3/kcm_kgamma.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kgamma.so
%{_datadir}/apps/kgamma
%{_datadir}/applnk/.hidden/kgamma.desktop
%{_iconsdir}/*/*/apps/kgamma.png
%{_kdedocdir}/en/kgamma

%files kghostview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%{_libdir}/kde3/libkghostviewpart.la
%{_libdir}/libkghostviewlib.so.0.0.0
%{_libdir}/libkghostviewlib.la
%attr(755,root,root) %{_libdir}/kde3/libkghostviewpart.so
%{_datadir}/apps/kghostview
%{_desktopdir}/kde/kghostview.desktop
%{_iconsdir}/*/*/*/kghostview.*
%{_mandir}/man1/kghostview.1*
%{_kdedocdir}/en/kghostview

%files kiconedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_datadir}/apps/kiconedit
%{_desktopdir}/kde/kiconedit.desktop
%{_iconsdir}/*/*/*/kiconedit.*
%{_mandir}/man1/kiconedit.1*
%{_kdedocdir}/en/kiconedit

%files kooka
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kooka
%{_libdir}/libkscan.la
%attr(755,root,root) %{_libdir}/libkscan.so.*.*.*
%{_datadir}/apps/kooka
%{_datadir}/config/kookarc
%{_datadir}/services/scanservice.desktop
%{_desktopdir}/kde/kooka.desktop
%{_iconsdir}/*/*/actions/palette*
%{_mandir}/man1/kooka.1*
%{_kdedocdir}/en/kooka

%files kpaint
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpaint
%{_datadir}/apps/kpaint
%{_desktopdir}/kde/kpaint.desktop
%{_iconsdir}/*/*/*/kpaint.*
%{_mandir}/man1/kpaint.1*
%{_kdedocdir}/en/kpaint

%files kpdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpdf
%{_libdir}/kde3/libkpdfpart.la
%attr(755,root,root) %{_libdir}/kde3/libkpdfpart.so
%{_datadir}/apps/kpdf
%{_datadir}/apps/kpdfpart
%{_datadir}/services/kpdf_part.desktop
%{_desktopdir}/kde/kpdf.desktop
%{_iconsdir}/*/*/*/kpdf.png
%{_kdedocdir}/en/kpdf

%files kpovmodeler
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpovmodeler
%{_libdir}/libkpovmodeler.la
%attr(755,root,root) %{_libdir}/libkpovmodeler.so.*
%{_libdir}/kde3/libkpovmodelerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkpovmodelerpart.so*
%{_datadir}/apps/kpovmodeler
%{_desktopdir}/kde/kpovmodeler.desktop
%{_iconsdir}/[!l]*/*/*/kpovmodeler*
%{_mandir}/man1/kpovmodeler.1*
%{_kdedocdir}/en/kpovmodeler

%files kruler
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_desktopdir}/kde/kruler.desktop
%{_iconsdir}/*/*/apps/kruler.*
%{_mandir}/man1/kruler.1*
%{_kdedocdir}/en/kruler

%files ksnapshot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%{_desktopdir}/kde/ksnapshot.desktop
%{_iconsdir}/*/*/apps/ksnapshot.*
%{_mandir}/man1/ksnapshot.1*
%{_kdedocdir}/en/ksnapshot

%files ksvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/printnodetest
%attr(755,root,root) %{_bindir}/svgdisplay
%{_libdir}/libksvg.la
%attr(755,root,root) %{_libdir}/libksvg.so.*.*.*
%{_libdir}/libtext2path.la
%attr(755,root,root) %{_libdir}/libtext2path.so.*.*.*
%{_libdir}/kde3/libksvgplugin.la
%attr(755,root,root) %{_libdir}/kde3/libksvgplugin.so
%{_libdir}/kde3/libksvgrendererlibart.la
%attr(755,root,root) %{_libdir}/kde3/libksvgrendererlibart.so
%{_libdir}/kde3/svgthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/svgthumbnail.so
%{_datadir}/apps/ksvg
%{_datadir}/services/ksvglibartcanvas.desktop
%{_datadir}/services/ksvgplugin.desktop
%{_datadir}/services/svgthumbnail.desktop
%{_datadir}/servicetypes/ksvgrenderer.desktop

%files kuickshow
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%{_libdir}/libkdeinit_kuickshow.la
%attr(755,root,root) %{_libdir}/libkdeinit_kuickshow.so
%{_libdir}/kde3/kuickshow.la
%attr(755,root,root) %{_libdir}/kde3/kuickshow.so
%{_datadir}/apps/kuickshow
%{_desktopdir}/kde/kuickshow.desktop
%{_iconsdir}/[!l]*/*/*/kuickshow.*
%{_mandir}/man1/kuickshow.1*
%{_kdedocdir}/en/kuickshow

%files kview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kview
%attr(755,root,root) %{_bindir}/kviewshell
%{_libdir}/libkdeinit_kview.la
%attr(755,root,root) %{_libdir}/libkdeinit_kview.so
%{_libdir}/libkmultipage.la
%attr(755,root,root) %{_libdir}/libkmultipage.so.*.*.*
%{_libdir}/libkimageviewer.la
%attr(755,root,root) %{_libdir}/libkimageviewer.so.*.*.*
%{_libdir}/kde3/kcm_kviewcanvasconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewcanvasconfig.so
%{_libdir}/kde3/kcm_kviewgeneralconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewgeneralconfig.so
%{_libdir}/kde3/kcm_kviewpluginsconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewpluginsconfig.so
%{_libdir}/kde3/kcm_kviewpresenterconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewpresenterconfig.so
%{_libdir}/kde3/kcm_kviewviewerpluginsconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewviewerpluginsconfig.so
%{_libdir}/kde3/kview.la
%attr(755,root,root) %{_libdir}/kde3/kview.so
%{_libdir}/kde3/kview_browserplugin.la
%attr(755,root,root) %{_libdir}/kde3/kview_browserplugin.so
%{_libdir}/kde3/kview_effectsplugin.la
%attr(755,root,root) %{_libdir}/kde3/kview_effectsplugin.so
%{_libdir}/kde3/kview_presenterplugin.la
%attr(755,root,root) %{_libdir}/kde3/kview_presenterplugin.so
%{_libdir}/kde3/kview_scannerplugin.la
%attr(755,root,root) %{_libdir}/kde3/kview_scannerplugin.so
%{_libdir}/kde3/kviewerpart.la
%attr(755,root,root) %{_libdir}/kde3/kviewerpart.so
%{_libdir}/kde3/libkviewcanvas.la
%attr(755,root,root) %{_libdir}/kde3/libkviewcanvas.so
%{_libdir}/kde3/libkviewviewer.la
%attr(755,root,root) %{_libdir}/kde3/libkviewviewer.so
%{_datadir}/apps/kview
%{_datadir}/apps/kviewerpart
%{_datadir}/apps/kviewshell
%{_datadir}/apps/kviewviewer
%{_datadir}/services/kconfiguredialog/kviewcanvasconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewgeneralconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewpluginsconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewpresenterconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewviewerpluginsconfig.desktop
%{_datadir}/services/kviewcanvas.desktop
%{_datadir}/services/kviewviewer.desktop
%{_datadir}/servicetypes/kimageviewer.desktop
%{_datadir}/servicetypes/kimageviewercanvas.desktop
%{_desktopdir}/kde/kview.desktop
%{_iconsdir}/*/*/*/kview*.png
%{_mandir}/man1/kview.1*
%{_mandir}/man1/kviewshell.1*
%{_kdedocdir}/en/kview

%files kmrml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mrmlsearch
%{_libdir}/libkdeinit_mrmlsearch.la
%attr(755,root,root) %{_libdir}/libkdeinit_mrmlsearch.so
%{_libdir}/kde3/kcm_kmrml.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmrml.so
%{_libdir}/kde3/kio_mrml.la
%attr(755,root,root) %{_libdir}/kde3/kio_mrml.so
%{_libdir}/kde3/libkmrmlpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmrmlpart.so
%{_libdir}/kde3/mrmlsearch.la
%attr(755,root,root) %{_libdir}/kde3/mrmlsearch.so
%{_datadir}/mimelnk/text/mrml.desktop
%{_datadir}/services/mrml.protocol
%{_datadir}/services/mrml_part.desktop
%{_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{_desktopdir}/kde/kcmkmrml.desktop
