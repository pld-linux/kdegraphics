# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.
#

%define		_state		stable
%define		_ver		3.1.5

Summary:	K Desktop Environment - graphic applications
Summary(es):	K Desktop Environment - aplicaciones gr�ficas
Summary(pl):	K Desktop Environment - aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - aplica��es gr�ficas
Name:		kdegraphics
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ba16a4a71381d57928325bc55ce7fe4c
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	00f1a8965389d1fab25fa6feba809d63
Source2:	%{name}-extra_icons.tar.bz2
# Source2-md5:	b7b2fcb2871a40b413041b59fa77ee3b
Patch0:		%{name}-no_glut.patch
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	gettext-devel
BuildRequires:	gphoto2
BuildRequires:	imlib-devel
BuildRequires:	kdelibs-devel >= 8:%{version}
BuildRequires:	libgphoto2-devel
BuildRequires:	libieee1284-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	sane-backends-devel
BuildRequires:	textutils
BuildRequires:	zlib-devel
Requires:	kdelibs >= 8:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

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
Aplicaciones gr�ficas para KDE.

Incluidos en este paquete:
- KDVI - visualiza archivos TeX's independientes de dispositivo,
- KFax - visualiza archivos de fax,
- KFract - creador de fractal
- KGhostview - visualiza archivos postscript (.ps),
- KPaint - un programa sencillo de dibujo,
- KView - visualiza numerosos formatos de archivos gr�ficos.

%description -l pl
Aplikacje graficzne dla KDE.

Pakiet zawiera:

- Kamera - obs�uga kamer cyfrowych
- KDVI - przegl�darka plik�w DVI,
- KColorEdit - edytor palety kolor�w
- KColorChooser - wyb�r koloru
- KFax - program do wy�wietlania faks�w,
- KFract - generator fraktali,
- KGhostview - program do ogl�dania postscriptu (.ps),
- KIconedit - program do edycji ikon dla KDE,
- KPaint - prosty program do grafiki rastrowej,
- KRuler - linijka ekranowa
- KSnapshot - program do przechwytywania wygl�du ekranu,
- KuickShow - przegl�darka plik�w graficznych.
- KView - przegl�darka plik�w graficznych.

%description -l pt_BR
Aplica��es gr�ficas para o KDE.

Inclu�dos neste pacote:
- KDVI - visualiza arquivos TeX's independentes de dispositivo,
- KFax - visualiza arquivos de fax,
- KFract - gerador de fractal,
- KGhostview - visualiza arquivos postscript (.ps),
- KPaint - um programa simples de desenho,
- KView - visualiza numerosos formatos de arquivos gr�ficos.

%package devel
Summary:	kdegraphics development files
Summary(pl):	Pliki dla programist�w kdegraphics
Summary(pt_BR):	Arquivos de inclus�o para compila��o de aplica��es com kdegraphics
Group:		X11/Development/Libraries
Requires:	%{name}-kooka = %{epoch}:%{version}
Requires:	%{name}-kview = %{epoch}:%{version}
Obsoletes:	kdegraphics

%description devel
kdegraphics development files.

%description devel -l pl
Pliki dla programist�w kdegraphics.

%description devel -l pt_BR
Arquivos de inclus�o para compila��o de aplica��es que usem as
bibliotecas do kdegraphics.

%package daemonwatcher
Summary:	KDED daemon watcher
Summary(pl):	Stra�nik demona KDED
Group:		X11/Applications
Requires:	%{name}-kmrml-messages
Requires:	kdelibs >= 8:%{version}
#Obsoletes:	%{name}-mrml < 3.1-6
Obsoletes:	kdegraphics

%description daemonwatcher
Starts daemons on demand and restarts them on failure.

%description daemonwatcher -l pl
Uruchamia demony na ��danie lub restartuje je po awarii.

%package kamera
Summary:	Digital camera support
Summary(pl):	Obs�uga kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Requires:	kdebase-core >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kamera
Digital camera support.

%description kamera -l pl
Obs�uga kamer cyfrowych.

%package kcolorchooser
Summary:	Color chooser
Summary(pl):	Program do wybierania kolor�w
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kcolorchooser
Color chooser.

%description kcolorchooser -l pl
Program do wybierania kolor�w.

%package kcoloredit
Summary:	Color palette editor
Summary(pl):	Edytor palety kolor�w
Summary(pt_BR):	Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kcoloredit
Color palette editor.

%description kcoloredit -l pl
Edytor palety kolor�w.

%description kcoloredit -l pt_BR
Editor de cores do KDE.

%package kdvi
Summary:	KDE DVI viewer
Summary(pl):	Przegl�darka plik�w DVI dla KDE
Summary(pt_BR):	Programa de exibi��o de DVIs
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kdvi
A tool for viewing DVI files generated by TeX system.

%description kdvi -l pl
Program do przegl�dania plik�w DVI.

%description kdvi -l pt_BR
Programa de exibi��o de DVIs.

%package kfax
Summary:	KDE fax viewer
Summary(pl):	Przegl�darka faks�w dla KDE
Summary(pt_BR):	Programa de visualiza��o de faxes (formato TIFF)
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kfax
A Fax viewer for KDE.

%description kfax -l pl
Program ten umo�liwia przegl�danie plik�w faksowych (G3).

%description kfax -l pt_BR
Programa de visualiza��o de faxes (formato TIFF).

%package kfile
Summary:	Graphic formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach graficznych
Group:		X11/Development/Libraries
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kfile
This package adds a fold to konqueror "file properties"
dialog window with file enhanced informations.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w�a�ciwo�ci pliku"
konquerora dodatkow� zak�adk� z rozszerzonymi informacjami
o pliku.

%package kghostview
Summary:	KDE postscript viewer
Summary(pl):	Przegl�darka postscriptu dla KDE
Summary(pt_BR):	Programa de visualiza��o de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kghostview
Postscript files (.ps) viewer for KDE.

%description kghostview -l pl
Program ten umo�liwia przegl�danie plik�w postscriptowych (.ps).

%description kghostview -l pt_BR
Programa de visualiza��o de arquivos Postscript e PDF.

%package kiconedit
Summary:	KDE icon editor
Summary(pl):	Edytor ikon w �rodowisku KDE
Summary(pt_BR):	Editor de �cones
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kiconedit
KDE Icon editor.

%description kiconedit -l pl
Edytor ikon dla KDE.

%description kiconedit -l pt_BR
Editor de �cones, lida inclusive com arquivos .ICO .

%package kmrml-messages
Summary:	International files for daemonwatcher and mrml
Summary(pl):	Pliki z t�umaczeniami dla daemonwatchera i mrmla
Group:		X11/Applications/Graphics
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract
Obsoletes:	kdegraphics-kmrml

%description kmrml-messages
International files for daemonwatcher and mrml.

%description kmrml-messages -l pl
Pliki z t�umaczeniami dla daemonwatchera i mrmla.

%package kooka
Summary:	Scanning tool
Summary(pl):	Narz�dzie do skanowania
Summary(pt_BR):	Um programa de rasteriza��o de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kooka
Scanning tool.

%description kooka -l pl
Narz�dzie do skanowania.

%description kooka -l pt_BR
Um programa de rasteriza��o de imagens, baseado no SANE e libkscan.

%package kpaint
Summary:	KDE painter
Summary(pl):	Program graficzny KDE
Summary(pt_BR):	Editor b�sico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kpaint
A (very) simple painting program for KDE.

%description kpaint -l pl
(Bardzo) prosty program do rysowania pod KDE.

%description kpaint -l pt_BR
Editor b�sico de imagens bitmap.

%package kpovmodeler
Summary:	Povary modeler
Summary(pl):	Modeler Povary
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Requires:	povray
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kpovmodeler
Modeler for POV-Ray scenes.

%description kpovmodeler -l pl
Modeler do scen POV-Raya.

%package kruler
Summary:	KRuler
Summary(pl):	Linijka dla KDE
Summary(pt_BR):	R�gua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl
KRuler jest prost� aplikacj�, z tylko jednym celem w �yciu: mierzenie
odleg�o�ci na ekranie.

%description kruler -l pt_BR
R�gua de pixels para a tela.

%package ksnapshot
Summary:	KDE snapshot
Summary(pl):	Program do przechwytywania ekranu dla KDE
Summary(pt_BR):	Programa de captura de tela
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description ksnapshot
Snapshot program for KDE.

%description ksnapshot -l pl
Program do przechwytywania ekranu dla KDE.

%description ksnapshot -l pt_BR
Programa de captura de tela.

%package kuickshow
Summary:	Image viewer/browser
Summary(pl):	Przegl�darka obrazk�w
Group:		X11/Applications/Graphics
Requires:	kdelibs >= 8:%{version}
Provides:	kuickshow
Obsoletes:	kuickshow
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kuickshow
Image viewer/browser.

%description kuickshow -l pl
Przegl�darka obrazk�w.

%package kview
Summary:	KDE graphics file viewer
Summary(pl):	Przegl�darka plik�w graficznych dla KDE
Summary(pt_BR):	Visualizador de imagens
Group:		X11/Applications/Graphics
Requires:	%{name}-kview = %{epoch}:%{version}
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kview
A graphics files viewer for KDE.

%description kview -l pl
Program, kt�ry umo�liwia ogl�danie r�nych plik�w graficznych.

%description kview -l pt_BR
Visualizador de imagens poderoso para KDE.

%package mrml
Summary:	Advanced search
Summary(pl):	Zaawansowane wyszukiwanie
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= 8:%{version}
Requires:	%{name}-kmrml-messages
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description mrml
Provides graphics files advanced search with file indexing.

%description mrml -l pl
Umo�liwia zaawansowane wyszukiwanie plik�w graficznych
z indeksowaniem plik�w.

%prep
%setup -q
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%{__make} -f admin/Makefile.common cvs

for plik in `find . -name \*.desktop -o -name \*rc | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $plik 2>/dev/null
done

%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Graphics/Viewers,Settings/KDE,Utilities} \
	$RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	RUN_KAPPFINDER=no

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv $ALD/{Settings/[!K]*,Settings/KDE}
mv $ALD/{Graphics/More/*.desktop,Graphics}
mv $ALD/{Graphics/{kdvi,kfax,kghostview,kuickshow,kview}.desktop,Graphics/Viewers}
mv $ALD/{Graphics/{kcolorchooser,kruler}.desktop,Utilities}

cd $ALD/Utilities
cat kcolorchooser.desktop |sed -e 's/Icon=[^$]\+/Icon=colors/' \
	> kcolorchooser.desktop.tmp
mv -f kcolorchooser.desktop.tmp kcolorchooser.desktop
cd -

cd $ALD/Settings/KDE/Peripherals
cat kamera.desktop |sed -e 's/Peripherals[/]kamera/kamera/' \
	> kamera.desktop.tmp
mv -f kamera.desktop.tmp kamera.desktop
cd -

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}
for i in {kdvi,kfax,kghostview,kiconedit,kpaint,kruler,ksnapshot,kview}.png; do
	ln -s crystalsvg/48x48/apps/$i $RPM_BUILD_ROOT%{_pixmapsdir}/$i
done

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

%find_lang	kamera			--with-kde
%find_lang	kcmkamera		--with-kde
cat kcmkamera.lang >> kamera.lang
%find_lang	kcoloredit		--with-kde
%find_lang	kdvi			--with-kde
%find_lang	kfax			--with-kde
%find_lang	kfile_bmp		--with-kde
#%find_lang	kfile_gif		--with-kde
%find_lang	kfile_ico		--with-kde
%find_lang	kfile_jpeg		--with-kde
%find_lang	kfile_pdf		--with-kde
%find_lang	kfile_png		--with-kde
%find_lang	kfile_ps		--with-kde
%find_lang	kfile_tga		--with-kde
%find_lang	kfile_tiff		--with-kde
%find_lang	kfile_xbm		--with-kde
cat kfile_{bmp,ico,jpeg,pdf,png,ps,tga,tiff,xbm}.lang > kfile.lang
%find_lang	kghostview		--with-kde
%find_lang	kiconedit		--with-kde
%find_lang	kooka			--with-kde
%find_lang	libkscan		--with-kde
cat libkscan.lang >> kooka.lang
%find_lang	kpaint			--with-kde
%find_lang	kpovmodeler		--with-kde
%find_lang	kruler			--with-kde
%find_lang	ksnapshot		--with-kde
%find_lang	kuickshow		--with-kde
%find_lang	kview			--with-kde
#%find_lang	kview_scale		--with-kde
#%find_lang	kviewtemplateplugin	--with-kde
%find_lang	kviewbrowserplugin	--with-kde
%find_lang	kviewpresenterplugin	--with-kde
%find_lang	kviewscannerplugin	--with-kde
cat kview{brows,present,scann}erplugin.lang >> kview.lang
%find_lang	kviewshell		--with-kde
cat kviewshell.lang >> kview.lang

# kmrml.mo is used by both: mrml and daemonwatcher
%find_lang 	kmrml			--with-kde

# kcoloredit.mo is used by both: kcoloredit and kcolorchooser
%find_lang	kcoloredit
mv -f kcoloredit.lang kcolorchooser.lang
%find_lang	kcoloredit		--with-kde

# probably should be in another package
#%find_lang	kpixmap2bitmap		--with-kde

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             DEVEL
#################################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/libkscan.so
%{_libdir}/libkmultipage.so
%{_libdir}/libkviewsupport.so

#################################################
#             DAEMONWATCHER
#################################################
%files daemonwatcher -f daemonwatcher.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kded_daemonwatcher.la
%attr(755,root,root) %{_libdir}/kde3/kded_daemonwatcher.so
%{_datadir}/services/kded/daemonwatcher.desktop

#################################################
#             KAMERA
#################################################
%files kamera -f kamera.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kamera.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kamera.so
%{_libdir}/kde3/kio_kamera.la
%attr(755,root,root) %{_libdir}/kde3/kio_kamera.so
%{_datadir}/services/kamera.protocol
%{_applnkdir}/Settings/KDE/Peripherals/kamera.desktop
%{_pixmapsdir}/*/*/*/camera*.png
%{_pixmapsdir}/camera.png

#################################################
#             KCOLORCHOOSER
#################################################
%files kcolorchooser -f kcolorchooser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_applnkdir}/Utilities/kcolorchooser.desktop
%{_mandir}/man1/kcolorchooser.*

#################################################
#             KCOLOREDIT
#################################################
%files kcoloredit -f kcoloredit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_datadir}/apps/kcoloredit
%{_applnkdir}/Graphics/kcoloredit.desktop
%{_pixmapsdir}/[!l]*/*/*/kcoloredit.png
%{_pixmapsdir}/kcoloredit.png
%{_mandir}/man1/kcoloredit.*

#################################################
#             KDVI
#################################################
%files kdvi -f kdvi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdvi
%{_libdir}/kde3/kdvipart.la
%attr(755,root,root) %{_libdir}/kde3/kdvipart.so
%{_datadir}/apps/kdvi/
%{_applnkdir}/Graphics/Viewers/kdvi.desktop
%{_pixmapsdir}/*/*/*/kdvi.png
%{_pixmapsdir}/kdvi.png
%{_mandir}/man1/kdvi.*

#################################################
#             KFAX
#################################################
%files kfax -f kfax.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%{_libdir}/kde3/kfaxpart.la
%attr(755,root,root) %{_libdir}/kde3/kfaxpart.so
%{_datadir}/apps/kfax/
%{_applnkdir}/Graphics/Viewers/kfax.desktop
%{_pixmapsdir}/*/*/*/kfax.png
%{_pixmapsdir}/kfax.png
%{_mandir}/man1/kfax.*

#################################################
#             KFILE
#################################################
%files kfile -f kfile.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kfile_*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/kfile_*.desktop

#################################################
#             KGHOSTVIEW
#################################################
%files kghostview -f kghostview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%{_libdir}/kde3/libkghostviewpart.la
%attr(755,root,root) %{_libdir}/kde3/libkghostviewpart.so
%{_datadir}/apps/kghostview
%{_applnkdir}/Graphics/Viewers/kghostview.desktop
%{_pixmapsdir}/*/*/*/kghostview.png
%{_pixmapsdir}/kghostview.png
%{_mandir}/man1/kghostview.*

#################################################
#             KICONEDIT
#################################################
%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_datadir}/apps/kiconedit
%{_applnkdir}/Graphics/kiconedit.desktop
%{_pixmapsdir}/*/*/*/kiconedit.png
%{_pixmapsdir}/kiconedit.png
%{_mandir}/man1/kiconedit.*

#################################################
#             KMRML-MESSAGES
#################################################
%files kmrml-messages -f kmrml.lang
%defattr(644,root,root,755)

#################################################
#             KOOKA
#################################################
%files kooka -f kooka.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kooka
%{_libdir}/libkscan.la
%attr(755,root,root) %{_libdir}/libkscan.so.*
%{_datadir}/apps/kooka
%{_datadir}/config/kookarc
%{_datadir}/services/scanservice.desktop
%{_applnkdir}/Graphics/kooka.desktop
%{_pixmapsdir}/*/*/actions/palette*
%{_mandir}/man1/kooka.*

#################################################
#             KPAINT
#################################################
%files kpaint -f kpaint.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpaint
%{_datadir}/apps/kpaint
%{_applnkdir}/Graphics/kpaint.desktop
%{_pixmapsdir}/*/*/*/kpaint.png
%{_pixmapsdir}/kpaint.png
%{_mandir}/man1/kpaint.*

#################################################
#             KPOVMODELER
#################################################
%files kpovmodeler -f kpovmodeler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpovmodeler
%{_libdir}/kde3/libkpovmodelerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkpovmodelerpart.so
%{_datadir}/apps/kpovmodeler
%{_applnkdir}/Graphics/kpovmodeler.desktop
%{_pixmapsdir}/[!l]*/*/*/kpovmodeler*.png
%{_pixmapsdir}/kpovmodeler.png
%{_mandir}/man1/kpovmodeler.*

#################################################
#             KRULER
#################################################
%files kruler -f kruler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_applnkdir}/Utilities/kruler.desktop
%{_pixmapsdir}/*/*/apps/kruler.png
%{_pixmapsdir}/kruler.png
%{_mandir}/man1/kruler.*

#################################################
#             KSNAPSHOT
#################################################
%files ksnapshot -f ksnapshot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%{_applnkdir}/Graphics/ksnapshot.desktop
%{_pixmapsdir}/*/*/apps/ksnapshot.png
%{_pixmapsdir}/ksnapshot.png
%{_mandir}/man1/ksnapshot.*

#################################################
#             KUICKSHOW
#################################################
%files kuickshow -f kuickshow.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%{_libdir}/kuickshow.la
%attr(755,root,root) %{_libdir}/kuickshow.so
%{_datadir}/apps/kuickshow
%{_applnkdir}/Graphics/Viewers/kuickshow.desktop
%{_pixmapsdir}/[!l]*/*/*/kuickshow.png
%{_pixmapsdir}/kuickshow.png
%{_mandir}/man1/kuickshow.*

#################################################
#             KVIEW
#################################################
%files kview -f kview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kview
%attr(755,root,root) %{_bindir}/kviewshell
%{_libdir}/kview.la
%attr(755,root,root) %{_libdir}/kview.so
%{_libdir}/libkmultipage.la
%attr(755,root,root) %{_libdir}/libkmultipage.so.*
%{_libdir}/libkpagetest.la
%attr(755,root,root) %{_libdir}/libkpagetest.so
%{_libdir}/libkviewsupport.la
%attr(755,root,root) %{_libdir}/libkviewsupport.so.*
%{_libdir}/kde3/kview*.la
%attr(755,root,root) %{_libdir}/kde3/kview*.so
%{_libdir}/kde3/libkview*.la
%attr(755,root,root) %{_libdir}/kde3/libkview*.so
%{_datadir}/apps/kview*
%{_datadir}/services/kview*
%{_datadir}/servicetypes/kimageviewer*
%{_applnkdir}/Graphics/Viewers/kview.desktop
%{_pixmapsdir}/*/*/*/kview*.png
%{_pixmapsdir}/kview.png
%{_mandir}/man1/kview*

#################################################
#             MRML
#################################################
%files mrml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mrmlsearch
%attr(755,root,root) %{_libdir}/mrmlsearch.*
%{_libdir}/kde3/kcm_kmrml.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmrml.so
%{_libdir}/kde3/kio_mrml.la
%attr(755,root,root) %{_libdir}/kde3/kio_mrml.so
%{_libdir}/kde3/libkmrmlpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmrmlpart.so
%{_datadir}/mimelnk/text/mrml.desktop
%{_datadir}/services/mrml.protocol
%{_datadir}/services/mrml_part.desktop
%{_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{_applnkdir}/Settings/KDE/System/kcmkmrml.desktop
