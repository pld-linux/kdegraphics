# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.
#

%define         _state          snapshots
%define         _ver		3.2
%define		_snap		030509

Summary:	K Desktop Environment - Graphic Applications
Summary(es):	K Desktop Environment - aplicaciones gráficas
Summary(pl):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - Aplicações gráficas
Name:		kdegraphics
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-vcategories.patch
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

%define		_htmldir	%{_docdir}/kde/HTML

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
Summary(pl):	Stra¿nik demona KDED
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
Requires:	kdebase-core >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kamera
Digital camera support.

%description kamera -l pl
Obs³uga kamer cyfrowych.

%package kcolorchooser
Summary:	Color chooser
Summary(pl):	Program do wybierania kolorów
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kcolorchooser
Color chooser.

%description kcolorchooser -l pl
Program do wybierania kolorów.

%package kcoloredit
Summary:	Color palette editor
Summary(pl):	Edytor palety kolorów
Summary(pt_BR):	Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{version}
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
Requires:	%{name}-kview = %{version}-%{release}
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
Requires:	%{name}-kview = %{version}-%{release}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kfax
A Fax viewer for KDE.

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
Obsoletes:	kdegraphics-kfract

%description kfile
This package adds a fold to konqueror "file properties"
dialog window with file enhanced informations. 

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³a¶ciwo¶ci pliku" 
konquerora dodatkow± zak³adkê z rozszerzonymi informacjami
o pliku.

%package kgamma
Summary:	A monitor calibration tool
Summary(pl):	Narzêdzie do kalibracji monitora
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kgamma
A monitor calibration tool.

%description kgamma -l pl
Narzêdzie do kalibracji monitora.

%package kghostview
Summary:	KDE Postscript viewer
Summary(pl):	Przegl±darka postscriptu dla KDE
Summary(pt_BR):	Programa de visualização de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kghostview
Postscript files (.ps) viewer for KDE.

%description kghostview -l pl
Program ten umo¿liwia przegl±danie plików postscriptowych (.ps).

%description kghostview -l pt_BR
Programa de visualização de arquivos Postscript e PDF.

%package kiconedit
Summary:	KDE Icon Editor
Summary(pl):	Edytor ikon w ¶rodowisku KDE
Summary(pt_BR):	Editor de ícones
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{version}
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
Requires:	kdebase-core >= %{version}
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
Requires:	kdebase-core >= %{version}
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
Summary(pl):	Modeler Povary
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{version}
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
Summary(pt_BR):	Régua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{version}
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
Requires:	kdebase-core >= %{version}
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
Requires:	kdebase-core >= %{version}
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
Requires:	kdebase-core >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kview
A graphics files viewer for KDE.

%description kview -l pl
Program ten umo¿liwia ogl±danie ró¿nych plików graficznych.

%description kview -l pt_BR
Visualizador de imagens poderoso para KDE.

%package mrml
Summary:	Advanced Search
Summary(pl):	Zaawansowane wyszukiwanie
Group:		X11/Applications/Graphics
Requires:	konqueror >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description mrml
Provides graphics files advanced search with file indexing.

%description mrml -l pl
Umo¿liwia zaawansowane wyszukiwanie plików graficznych
z indeksowaniem plików.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings,KDE-Settings}

cd $RPM_BUILD_ROOT%{_desktopdir}
cat kcolorchooser.desktop |sed -e 's/Icon=[^$]\+/Icon=colors/' \
    > kcolorchooser.desktop.tmp
mv -f kcolorchooser.desktop.tmp kcolorchooser.desktop
cd -

%find_lang kamera		--with-kde
%find_lang kcoloredit		--with-kde
%find_lang kgamma		--with-kde
%find_lang kdvi			--with-kde
%find_lang kghostview		--with-kde
%find_lang kiconedit		--with-kde
%find_lang kooka		--with-kde
%find_lang kpaint		--with-kde
%find_lang kpovmodeler		--with-kde
%find_lang kruler		--with-kde
%find_lang ksnapshot		--with-kde
%find_lang kuickshow		--with-kde
%find_lang kview		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kooka		-p /sbin/ldconfig
%postun	kooka		-p /sbin/ldconfig

%post	kview		-p /sbin/ldconfig
%postun	kview		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/libkscan.so
%{_libdir}/libkmultipage.so
%{_libdir}/libkimageviewer.so

%files daemonwatcher
%defattr(644,root,root,755)
%{_libdir}/kde3/kded_daemonwatcher.la
%attr(755,root,root) %{_libdir}/kde3/kded_daemonwatcher.so
%{_datadir}/services/kded/daemonwatcher.desktop

%files kamera -f kamera.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kamera.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kamera.so
%{_libdir}/kde3/kio_kamera.la
%attr(755,root,root) %{_libdir}/kde3/kio_kamera.so
%{_datadir}/services/kamera.protocol
%{_applnkdir}/KDE-Settings/Peripherals/kamera.desktop
%{_pixmapsdir}/*/*/*/camera*

%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_desktopdir}/kcolorchooser.desktop

%files kcoloredit -f kcoloredit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_datadir}/apps/kcoloredit
%{_desktopdir}/kcoloredit.desktop
%{_pixmapsdir}/[!l]*/*/*/kcoloredit.*

%files kdvi -f kdvi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdvi
%{_libdir}/kde3/kdvipart.la
%attr(755,root,root) %{_libdir}/kde3/kdvipart.so
%{_datadir}/apps/kdvi/
%{_desktopdir}/kdvi.desktop
%{_pixmapsdir}/*/*/*/kdvi.*

%files kfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%{_libdir}/kde3/kfaxpart.la
%attr(755,root,root) %{_libdir}/kde3/kfaxpart.so
%{_datadir}/apps/kfax/
%{_desktopdir}/kfax.desktop
%{_pixmapsdir}/*/*/*/kfax.*

%files kfile
%defattr(644,root,root,755)
%{_libdir}/kde3/kfile_*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/kfile_*.desktop

%files kgamma -f kgamma.lang 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xf86gammacfg
%{_libdir}/kde3/libkcm_kgamma.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kgamma.so
%{_datadir}/apps/kgamma
%{_applnkdir}/KDE-Settings/Peripherals/kgamma.desktop
%{_pixmapsdir}/*/*/apps/kgamma_red.png

%files kghostview -f kghostview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%{_libdir}/kde3/libkghostviewpart.la
%attr(755,root,root) %{_libdir}/kde3/libkghostviewpart.so
%{_datadir}/apps/kghostview
%{_desktopdir}/kghostview.desktop
%{_pixmapsdir}/*/*/*/kghostview.*

%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_datadir}/apps/kiconedit
%{_desktopdir}/kiconedit.desktop
%{_pixmapsdir}/*/*/*/kiconedit.*

%files kooka -f kooka.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kooka
%{_libdir}/libkscan.la
%attr(755,root,root) %{_libdir}/libkscan.so.*.*.*
%{_datadir}/apps/kooka
%{_datadir}/config/kookarc
%{_datadir}/services/scanservice.desktop
%{_desktopdir}/kooka.desktop
%{_pixmapsdir}/*/*/actions/palette*

%files kpaint -f kpaint.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpaint
%{_datadir}/apps/kpaint
%{_desktopdir}/kpaint.desktop
%{_pixmapsdir}/*/*/*/kpaint.*

%files kpovmodeler -f kpovmodeler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpovmodeler
%{_libdir}/kde3/libkpovmodelerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkpovmodelerpart.so
%{_datadir}/apps/kpovmodeler
%{_desktopdir}/kpovmodeler.desktop
%{_pixmapsdir}/[!l]*/*/*/kpovmodeler*

%files kruler -f kruler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_desktopdir}/kruler.desktop
%{_pixmapsdir}/*/*/apps/kruler.*

%files ksnapshot -f ksnapshot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%{_desktopdir}/ksnapshot.desktop
%{_pixmapsdir}/*/*/apps/ksnapshot.*

%files kuickshow -f kuickshow.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%{_libdir}/kuickshow.la
%attr(755,root,root) %{_libdir}/kuickshow.so
%{_datadir}/apps/kuickshow
%{_desktopdir}/kuickshow.desktop
%{_pixmapsdir}/[!l]*/*/*/kuickshow.*

%files kview -f kview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kview
%attr(755,root,root) %{_bindir}/kviewshell
%{_libdir}/kview.la
%attr(755,root,root) %{_libdir}/kview.so
%{_libdir}/libkmultipage.la
%attr(755,root,root) %{_libdir}/libkmultipage.so.*.*.*
%{_libdir}/libkimageviewer.la
%attr(755,root,root) %{_libdir}/libkimageviewer.so.*.*.*
%{_libdir}/kde3/kview*.la
%attr(755,root,root) %{_libdir}/kde3/kview*.so
%{_libdir}/kde3/libkview*.la
%attr(755,root,root) %{_libdir}/kde3/libkview*.so
%{_datadir}/apps/kview*
%{_datadir}/services/kview*
%{_datadir}/servicetypes/kimageviewer*
%{_desktopdir}/kview.desktop
%{_pixmapsdir}/*/*/*/kview*

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
%{_applnkdir}/KDE-Settings/System/kcmkmrml.desktop
