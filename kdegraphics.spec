# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.
#

%define         _state          stable
%define         _ver		3.1.1

Summary:	K Desktop Environment - Graphic Applications
Summary(es):	K Desktop Environment - aplicaciones gráficas
Summary(pl):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - Aplicações gráficas
Name:		kdegraphics
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	gettext-devel
BuildRequires:	glut-devel
BuildRequires:	imlib-devel
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	sane-backends-devel
BuildRequires:	sed >= 4.0
BuildRequires:	textutils
BuildRequires:	zlib-devel
BuildRequires:	libieee1284-devel
Requires:	kdelibs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

%description
Graphic applications for the K Desktop Environment.

Included with this package are:

- Kamera - digital camera support
- KColorEdit - color calette editor
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

Pakiet zawiera:

- Kamera - obs³uga kamer cyfrowych
- KDVI - przegl±darka plików DVI,
- KColorEdit - edytor palety kolorów
- KColorChooser - wybóe koloru
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
Requires:	%{name}-kooka = %{version}
Requires:	%{name}-kview = %{version}

%description devel
kdegraphics development files.

%description devel -l pl
Pliki dla programistów kdegraphics.

%description devel -l pt_BR
Arquivos de inclusão para compilação de aplicações que usem as
bibliotecas do kdegraphics.

%package daemonwatcher
Summary:	KDED Daemon Watcher
Summary(pl):	Stra¼nik demona KDED
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-mrml < 3.1-6 

%description daemonwatcher
Starts daemons on demand and restarts them on failure.

%description daemonwatcher -l pl
Uruchamia demony na ¿±danie lub restartuje je po awarii.

%package kamera
Summary:	Digital camera support
Summary(pl):	Obs³uga kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kamera
Digital camera support.

%description kamera -l pl
Obs³uga kamer cyfrowych.

%package kcolorchooser
Summary:	Color chooser
Summary(pl):	Wybieracz kolrów
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kcolorchooser
Color chooser

%description kcolorchooser -l pl
Wybieracz kolorów.

%package kcoloredit
Summary:	Color palette editor
Summary(pl):	Edytor palety kolorów
Summary(pt_BR):	Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kcoloredit
Color palette editor.

%description kcoloredit -l pl
Edytor palety kolorów.

%description kcoloredit -l pt_BR
Editor de cores do KDE.

%package kdvi
Summary:	KDE DVI viewer
Summary(pl):	Przegl±darka plików DVI dla KDE
Summary(pt_BR):	Programa de exibição de DVIs
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kdvi
A tool for viewing DVI files generated by TeX system.

%description kdvi -l pl
Program do przegl±dania plików DVI.

%description kdvi -l pt_BR
Programa de exibição de DVIs.

%package kfax
Summary:	KDE Fax viewer
Summary(pl):	Przegl±darka faksów dla KDE
Summary(pt_BR):	Programa de visualização de faxes (formato TIFF)
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kfax
A Fax viewer for KDE.

%description kfax -l pl
Program ten umo¿liwia przegl±danie plików faksowych (G3)

%description kfax -l pt_BR
Programa de visualização de faxes (formato TIFF).

%package kfile
Summary:	Graphic formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach graficznych
Group:		X11/Development/Libraries
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kfile
This package adds a fold to konqueror "file properities"
dialog window with file enhanced informations. 

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³asciwo¶ci pliku" 
konquerora dodatkow± zak³adkê z rozszerzonymi informacjami
o pliku.

%package kghostview
Summary:	KDE Postscript viewer
Summary(pl):	Przegl±darka postscriptu dla KDE
Summary(pt_BR):	Programa de visualização de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kghostview
Postscript files (.ps) viewer for KDE

%description kghostview -l pl
Program ten umo¿liwia przegl±danie plików postscriptowych (.ps)

%description kghostview -l pt_BR
Programa de visualização de arquivos Postscript e PDF.

%package kiconedit
Summary:	KDE Icon Editor
Summary(pl):	Edytor ikon w ¶rodowisku KDE
Summary(pt_BR):	Editor de ícones
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

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
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kooka
Scanning tool.

%description kooka -l pl
Narzêdzie do skanowania.

%description kooka -l pt_BR
Um programa de rasterização de imagens, baseado no SANE e libkscan.

%package kpaint
Summary:	KDE Painter
Summary(pl):	Program graficzny KDE
Summary(pt_BR):	Editor básico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kpaint
A (very) simple painting program for KDE.

%description kpaint -l pl
(Bardzo) prosty program do rysowania pod KDE.

%description kpaint -l pt_BR
Editor básico de imagens bitmap.

%package kpovmodeler
Summary:	Povary Modeler
Summary(pl):	Povary Modeler
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Requires:	povray
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kpovmodeler
Modeler for POV-Ray scenes.

%description kpovmodeler -l pl
Modeler for POV-Ray scenes.

%package kruler
Summary:	KRuler
Summary(pl):	Linijka dla KDE
Summary(pt_BR):	Régua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl
KRuler jest prost± aplikacj±, z tylko jednym celem w ¿yciu: mierzenie
odleg³o¶ci na twoim ekranie.

%description kruler -l pt_BR
Régua de pixels para a tela.

%package ksnapshot
Summary:	KDE Snap Shot
Summary(pl):	Program do przechwytywania ekranu dla KDE
Summary(pt_BR):	Programa de captura de tela
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
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
Summary(pl):	Przegl±darka obrazków
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Provides:	kuickshow
Obsoletes:	kuickshow
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kuickshow
Image viewer/browser.

%description kuickshow -l pl
Przegl±darka obrazków.

%package kview
Summary:	KDE graphics file viewer
Summary(pl):	Przegl±darka plików graficznych dla KDE
Summary(pt_BR):	Visualizador de imagens
Group:		X11/Applications/Graphics
Requires:	%{name}-kview = %{version}
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kview
A graphics files viewer for KDE.

%description kview -l pl
Program ten umo¿liwia ogl±danie ró¿nych plików graficznych (G3).

%description kview -l pt_BR
Visualizador de imagens poderoso para KDE.

%package mrml
Summary:	Advanced Search
Summary(pl):	Zaawansowane wyszukiwanie
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description mrml
Provides graphics files advanced search with file indexing.

%description mrml -l pl
Umo¿liwia zaawansowane wyszukiwanie plików graficznych
z indeksowaniem plików.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop` ; do
	if [ -d $plik ]; then
	echo $plik
	sed -ie 's/\[nb\]/\[no\]/g' $plik
	fi
done
				

%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/{Graphics/Viewers,Settings/KDE,Utilities}

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

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#%find_lang kcmkamera		--with-kde
%find_lang kamera		--with-kde
%find_lang kcoloredit		--with-kde
%find_lang kdvi			--with-kde
#%find_lang kfax		--with-kde
#%find_lang kfile_pdf		--with-kde
#%find_lang kfile_png		--with-kde
#%find_lang kfile_ps		--with-kde
#%find_lang kpixmap2bitmap	--with-kde
#cat kpixmap2bitmap.lang kfile_pdf.lang kfile_png.lang kfile_ps.lang \
#    >> %{name}.lang
#%find_lang kfract		--with-kde
%find_lang kghostview		--with-kde
%find_lang kiconedit		--with-kde
%find_lang kooka		--with-kde
#%find_lang libkscan		--with-kde
#cat libkscan.lang >> kooka.lang
%find_lang kpaint		--with-kde
%find_lang kpovmodeler		--with-kde
%find_lang kruler		--with-kde
%find_lang ksnapshot		--with-kde
%find_lang kuickshow		--with-kde
%find_lang kview		--with-kde
#%find_lang kviewshell		--with-kde
#cat kviewshell.lang >> kview.lang

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
%files daemonwatcher
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
%{_pixmapsdir}/*/*/*/camera*

#################################################
#             KCOLORCHOOSER
#################################################
%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_applnkdir}/Utilities/kcolorchooser.desktop

#################################################
#             KCOLOREDIT
#################################################
%files kcoloredit -f kcoloredit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_datadir}/apps/kcoloredit
%{_applnkdir}/Graphics/kcoloredit.desktop
%{_pixmapsdir}/[!l]*/*/*/kcoloredit.*

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
%{_pixmapsdir}/*/*/*/kdvi.*

#################################################
#             KFAX
#################################################
#%files kfax -f kfax.lang
%files kfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%{_libdir}/kde3/kfaxpart.la
%attr(755,root,root) %{_libdir}/kde3/kfaxpart.so
%{_datadir}/apps/kfax/
%{_applnkdir}/Graphics/Viewers/kfax.desktop
%{_pixmapsdir}/*/*/*/kfax.*

#################################################
#             KFILE
#################################################
%files kfile
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
%{_pixmapsdir}/*/*/*/kghostview.*

#################################################
#             KICONEDIT
#################################################
%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_datadir}/apps/kiconedit
%{_applnkdir}/Graphics/kiconedit.desktop
%{_pixmapsdir}/*/*/*/kiconedit.*

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

#################################################
#             KPAINT
#################################################
%files kpaint -f kpaint.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpaint
%{_datadir}/apps/kpaint
%{_applnkdir}/Graphics/kpaint.desktop
%{_pixmapsdir}/*/*/*/kpaint.*

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
%{_pixmapsdir}/[!l]*/*/*/kpovmodeler*

#################################################
#             KRULER
#################################################
%files kruler -f kruler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_applnkdir}/Utilities/kruler.desktop
%{_pixmapsdir}/*/*/apps/kruler.*

#################################################
#             KSNAPSHOT
#################################################
%files ksnapshot -f ksnapshot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%{_applnkdir}/Graphics/ksnapshot.desktop
%{_pixmapsdir}/*/*/apps/ksnapshot.*

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
%{_pixmapsdir}/[!l]*/*/*/kuickshow.*

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
%{_pixmapsdir}/*/*/*/kview*

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
