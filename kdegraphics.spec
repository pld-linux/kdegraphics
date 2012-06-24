# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.

%define         _state          unstable
%define         _kdever         kde-3.1-rc7

Summary:	K Desktop Environment - Graphic Applications
Summary(es):	K Desktop Environment - aplicaciones gr�ficas
Summary(pl):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - Aplica��es gr�ficas
Name:		kdegraphics
Version:	3.1
Release:	4
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	gettext-devel
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
BuildRequires:	sed
BuildRequires:	textutils
BuildRequires:	zlib-devel
Requires:	kdelibs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
- KColorChooser - wyb�e koloru
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
Requires:	%{name}-kooka = %{version}
Requires:	%{name}-kview = %{version}

%description devel
kdegraphics development files.

%description devel -l pl
Pliki dla programist�w kdegraphics.

%description devel -l pt_BR
Arquivos de inclus�o para compila��o de aplica��es que usem as
bibliotecas do kdegraphics.

%package kamera
Summary:	Digital camera support
Summary(pl):	Obs�uga kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kamera
Digital camera support.

%description kamera -l pl
Obs�uga kamer cyfrowych.

%package kcolorchooser
Summary:	Color chooser
Summary(pl):	Wybieracz kolr�w
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kcolorchooser
Color chooser

%description kcolorchooser -l pl
Wybieracz kolor�w.

%package kcoloredit
Summary:	Color palette editor
Summary(pl):	Edytor palety kolor�w
Summary(pt_BR):	Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
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
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kdvi
A tool for viewing DVI files generated by TeX system.

%description kdvi -l pl
Program do przegl�dania plik�w DVI.

%description kdvi -l pt_BR
Programa de exibi��o de DVIs.

%package kfax
Summary:	KDE Fax viewer
Summary(pl):	Przegl�darka faks�w dla KDE
Summary(pt_BR):	Programa de visualiza��o de faxes (formato TIFF)
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kfax
A Fax viewer for KDE.

%description kfax -l pl
Program ten umo�liwia przegl�danie plik�w faksowych (G3)

%description kfax -l pt_BR
Programa de visualiza��o de faxes (formato TIFF).

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
Ten pakiet dodaje do okna dialogowego "w�asciwo�ci pliku" 
konquerora dodatkow� zak�adk� z rozszerzonymi informacjami
o pliku.

%package kghostview
Summary:	KDE Postscript viewer
Summary(pl):	Przegl�darka postscriptu dla KDE
Summary(pt_BR):	Programa de visualiza��o de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kghostview
Postscript files (.ps) viewer for KDE

%description kghostview -l pl
Program ten umo�liwia przegl�danie plik�w postscriptowych (.ps)

%description kghostview -l pt_BR
Programa de visualiza��o de arquivos Postscript e PDF.

%package kiconedit
Summary:	KDE Icon Editor
Summary(pl):	Edytor ikon w �rodowisku KDE
Summary(pt_BR):	Editor de �cones
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kiconedit
KDE Icon editor.

%description kiconedit -l pl
Edytor ikon dla KDE.

%description kiconedit -l pt_BR
Editor de �cones, lida inclusive com arquivos .ICO.

%package kooka
Summary:	Scanning tool
Summary(pl):	Narz�dzie do skanowania
Summary(pt_BR):	Um programa de rasteriza��o de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kooka
Scanning tool.

%description kooka -l pl
Narz�dzie do skanowania.

%description kooka -l pt_BR
Um programa de rasteriza��o de imagens, baseado no SANE e libkscan.

%package kpaint
Summary:	KDE Painter
Summary(pl):	Program graficzny KDE
Summary(pt_BR):	Editor b�sico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kpaint
A (very) simple painting program for KDE.

%description kpaint -l pl
(Bardzo) prosty program do rysowania pod KDE.

%description kpaint -l pt_BR
Editor b�sico de imagens bitmap.

%package kpovmodeler
Summary:	Povary Modeler
Summary(pl):	Povary Modeler
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kpovmodeler
Modeler for POV-Ray scenes.

%description kpovmodeler -l pl
Modeler for POV-Ray scenes.

%package kruler
Summary:	KRuler
Summary(pl):	Linijka dla KDE
Summary(pt_BR):	R�gua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl
KRuler jest prost� aplikacj�, z tylko jednym celem w �yciu: mierzenie
odleg�o�ci na twoim ekranie.

%description kruler -l pt_BR
R�gua de pixels para a tela.

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
Summary(pl):	Przegl�darka obrazk�w
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{version}
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
Requires:	kdelibs >= %{version}
Obsoletes:	kdegraphics
Obsoletes:	kdegraphics-kfract

%description kview
A graphics files viewer for KDE.

%description kview -l pl
Program ten umo�liwia ogl�danie r�nych plik�w graficznych (G3).

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
Umo�liwia zaawansowane wyszukiwanie plik�w graficznych
z indeksowaniem plik�w.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

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

%post   kcolorchooser -p /sbin/ldconfig
%postun kcolorchooser -p /sbin/ldconfig

%post   kdvi -p /sbin/ldconfig
%postun kdvi -p /sbin/ldconfig

%post   kfax -p /sbin/ldconfig
%postun kfax -p /sbin/ldconfig

%post   kghostview -p /sbin/ldconfig
%postun kghostview -p /sbin/ldconfig

%post   kooka -p /sbin/ldconfig
%postun kooka -p /sbin/ldconfig

%post   kview -p /sbin/ldconfig
%postun kview -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             DEVEL
#################################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libkscan.so
%attr(755,root,root) %{_libdir}/libkviewsupport.so

#################################################
#             KAMERA
#################################################
%files kamera -f kamera.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kcm_kamera.*
%attr(755,root,root) %{_libdir}/kde3/kio_kamera.*
%{_datadir}/services/kamera.protocol
%{_applnkdir}/Settings/KDE/Peripherals/kamera.desktop
%{_pixmapsdir}/*/*/*/camera*

#################################################
#             KCOLORCHOOSER
#################################################
%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
#%attr(755,root,root) %{_libdir}/kcolorchooser.??
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
%attr(755,root,root) %{_libdir}/kde3/kdvipart.*
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
%attr(755,root,root) %{_libdir}/kde3/kfaxpart.*
%{_datadir}/apps/kfax/
%{_applnkdir}/Graphics/Viewers/kfax.desktop
%{_pixmapsdir}/*/*/*/kfax.*

#################################################
#             KFILE
#################################################
%files kfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kfile_*.??
%{_datadir}/services/kfile_*.desktop

#################################################
#             KFRACT
#################################################
#%files kfract -f kfract.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kfract
#%{_datadir}/apps/kfract/
#%{_applnkdir}/Graphics/kfract.desktop
#%{_pixmapsdir}/*/*/apps/kfract.*

#################################################
#             KGHOSTVIEW
#################################################
%files kghostview -f kghostview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%attr(755,root,root) %{_libdir}/kde3/libkghostviewpart.*
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
%attr(755,root,root) %{_libdir}/libkscan.so.*
%attr(755,root,root) %{_libdir}/libkscan.la
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
%attr(755,root,root) %{_libdir}/kde3/libkpovmodelerpart.*
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
%attr(755,root,root) %{_libdir}/kuickshow.??
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
%attr(755,root,root) %{_libdir}/kview.*
%attr(755,root,root) %{_libdir}/libkmultipage.*
%attr(755,root,root) %{_libdir}/libkpagetest.*
%attr(755,root,root) %{_libdir}/libkviewsupport.la
%attr(755,root,root) %{_libdir}/libkviewsupport.so.*
%attr(755,root,root) %{_libdir}/kde3/kview_browserplugin.*
%attr(755,root,root) %{_libdir}/kde3/kview_presenterplugin.*
%attr(755,root,root) %{_libdir}/kde3/kview_scannerplugin.*
%attr(755,root,root) %{_libdir}/kde3/kviewerpart.*
%attr(755,root,root) %{_libdir}/kde3/libkviewcanvas.*
%attr(755,root,root) %{_libdir}/kde3/libkviewviewer.*
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
%attr(755,root,root) %{_libdir}/kde3/kcm_kmrml.*
# ???
%attr(755,root,root) %{_libdir}/kde3/kded_daemonwatcher.*
%attr(755,root,root) %{_libdir}/kde3/kio_mrml.*
%attr(755,root,root) %{_libdir}/kde3/libkmrmlpart.*
%{_datadir}/mimelnk/text/mrml.desktop
# ???
%{_datadir}/services/kded/daemonwatcher.desktop
%{_datadir}/services/mrml.protocol
%{_datadir}/services/mrml_part.desktop
%{_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{_applnkdir}/Settings/KDE/System/kcmkmrml.desktop
