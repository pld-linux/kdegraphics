#
# Conditional build:
%bcond_without	kuickshow		# do not build kuickshow app (omit imlib req)
%bcond_with	protections		# protections against fair use (printing and copying)
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden'
					# & '--fvisibility-inlines-hidden'
					# to g++
#
%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	K Desktop Environment - Graphic Applications
Summary(es.UTF-8):   K Desktop Environment - aplicaciones gráficas
Summary(pl.UTF-8):   K Desktop Environment - Aplikacje graficzne
Summary(pt_BR.UTF-8):   K Desktop Environment - Aplicações gráficas
Name:		kdegraphics
Version:	3.5.6
Release:	3
Epoch:		9
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	79a1ffb7ae89bede1410411a30be3210
#Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-allowprint.patch
Patch2:		kde-ac260-lt.patch
Patch3:		%{name}-kuickshow-imlib.patch
BuildRequires:	OpenEXR-devel >= 1.1.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	ed
BuildRequires:	fribidi-devel >= 0.10.4
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
%{?with_kuickshow:BuildRequires:	imlib-devel}
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	kpathsea
BuildRequires:	lcms-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libieee1284-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	poppler-qt-devel
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sane-backends-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildConflicts:	kdegraphics-mrml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es.UTF-8
Aplicaciones gráficas para KDE.

Incluidos en este paquete:
- KDVI - visualiza archivos TeX's independientes de dispositivo,
- KFax - visualiza archivos de fax,
- KFract - creador de fractal
- KGhostview - visualiza archivos postscript (.ps),
- KPaint - un programa sencillo de dibujo,
- KView - visualiza numerosos formatos de archivos gráficos.

%description -l pl.UTF-8
Aplikacje graficzne dla KDE.

Pakiet zawiera programy:

- Kamera - obsługa kamer cyfrowych
- KDVI - przeglądarka plików DVI,
- KColorEdit - edytor palety kolorów
- KColorChooser - wybór koloru
- KFax - program do wyświetlania faksów,
- KFract - generator fraktali,
- KGhostview - program do oglądania postscriptu (.ps),
- KIconedit - program do edycji ikon dla KDE,
- KPaint - prosty program do grafiki rastrowej,
- KRuler - linijka ekranowa
- KSnapshot - program do przechwytywania wyglądu ekranu,
- KuickShow - przeglądarka plików graficznych.
- KView - przeglądarka plików graficznych.

%description -l pt_BR.UTF-8
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
Summary(pl.UTF-8):   Pliki dla programistów kdegraphics
Summary(pt_BR.UTF-8):   Arquivos de inclusão para compilação de aplicações com kdegraphics
Group:		X11/Development/Libraries
Requires:	%{name}-kghostview = %{epoch}:%{version}-%{release}
Requires:	%{name}-kooka = %{epoch}:%{version}-%{release}
Requires:	%{name}-ksvg = %{epoch}:%{version}-%{release}
Requires:	%{name}-kview = %{epoch}:%{version}-%{release}
Requires:	%{name}-kviewshell = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}

%description devel
kdegraphics development files.

%description devel -l pl.UTF-8
Pliki dla programistów kdegraphics.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para compilação de aplicações que usem as
bibliotecas do kdegraphics.

%package daemonwatcher
Summary:	KDED Daemon Watcher
Summary(pl.UTF-8):   Strażnik demona KDED
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Conflicts:	kdegraphics-mrml < 8:3.1-6

%description daemonwatcher
Starts daemons on demand and restarts them on failure.

%description daemonwatcher -l pl.UTF-8
Uruchamia demony na żądanie lub restartuje je po awarii.

%package kamera
Summary:	Digital camera support
Summary(pl.UTF-8):   Obsługa kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kamera
kamera is an IO slave and a KControl panel module which allows you to
access folders and images within any digital camera supported by the
upcoming gPhoto2 libraries. If you have a supported camera, you can
start using it with most KDE applications in two easy steps: simply
configure your camera model and port type from a list in KControl,
then start accessing the camera contents with a kamera:/ URL.

%description kamera -l pl.UTF-8
kamera to moduł IO slave oraz panelu KControl umożliwiający dostęp do
folderów i zdjęć w dowolnym aparacie cyfrowym obsługiwanym przez
biblioteki gPhoto2. Jeśli mamy obsługiwany aparat, można zacząć używać
go w większości aplikacji KDE w dwóch krokach: wybrać model i port
aparatu z listy w KControl, a następnie odwoływać się do zawartości
aparatu przez URL kamera:/.

%package kcolorchooser
Summary:	Color chooser
Summary(pl.UTF-8):   Program do wybierania kolorów
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{_minlibsevr}

%description kcolorchooser
Color chooser.

%description kcolorchooser -l pl.UTF-8
Program do wybierania kolorów.

%package kcoloredit
Summary:	Color palette editor
Summary(pl.UTF-8):   Edytor palety kolorów
Summary(pt_BR.UTF-8):   Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kcoloredit
KColorEdit is a palette files editor. It can be used for editing color
palettes and for color choosing and naming.

%description kcoloredit -l pl.UTF-8
KColorEdit to edytor plików palety kolorów. Może być używany do edycji
palet kolorów oraz wybierania i nazywania kolorów.

%description kcoloredit -l pt_BR.UTF-8
Editor de cores do KDE.

%package kdvi
Summary:	KDE DVI viewer
Summary(pl.UTF-8):   Przeglądarka plików DVI dla KDE
Summary(pt_BR.UTF-8):   Programa de exibição de DVIs
Group:		X11/Applications/Graphics
Requires:	%{name}-kviewshell = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kdvi
KDVI is a plugin for the KViewshell program which allows KViewshell to
display DVI-files (.dvi) which are produced by the TeX typesetting
system. KDVI supports many extensions of the DVI standard, for
instance the inclusion of PostScript graphics or hyperlinks.

%description kdvi -l pl.UTF-8
KDVI to wtyczka dla programu KViewshell umożliwiająca mu oglądanie
plików DVI (.dvi) stworzonych przez system składu TeX. KDVI obsługuje
wiele rozszerzeń standardu DVI, na przykład dołączanie grafiki
postscriptowej i hiperłącza.

%description kdvi -l pt_BR.UTF-8
Programa de exibição de DVIs.

%package kfax
Summary:	KDE Fax viewer
Summary(pl.UTF-8):   Przeglądarka faksów dla KDE
Summary(pt_BR.UTF-8):   Programa de visualização de faxes (formato TIFF)
Group:		X11/Applications/Graphics
Requires:	%{name}-kviewshell = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kfax
KFax is a Fax file viewer capable of displaying and printing all
common fax file formats. In particular the fax files used by popular
the mgetty/sendfax and hylafax fax send and receive packages can be
displayed. The first (or only) page of a "PC-Research"-style (DigiFAX)
files produced by the ghostscript dfaxhigh or dfaxlow drivers can also
be displayed. (who is still using this format?) Input files using any
common fax encoding such as group 3 (1 and 2 dimensional) and group 4
can be displayed. KFax has built in native postscript printing
capabilities.

%description kfax -l pl.UTF-8
KFax to przeglądarka plików faksowych potrafiąca wyświetlać i drukować
wszystkie popularne formaty plików faksowych. W szczególności można
wyświetlać pliki faksów używane przez pakiety do wysyłania i
odbierania faksów mgetty/sendfax oraz hylafax. Można wyświetlić także
pierwszą (lub jedyną) stronę plików w stylu "PC-Research" (DigiFAX)
stworzonych przez sterowniki dfaxhigh i dfaxlow z ghostscripta. Pliki
wejściowe mogą używać dowolnego popularnego kodowania, takiego jak G3
(1- i 2-wymiarowego) lub G4. KFax ma wbudowaną natywną możliwość
wydruku do postscriptu.

%description kfax -l pt_BR.UTF-8
Programa de visualização de faxes (formato TIFF).

%package kfile
Summary:	Graphic formats enhanced information
Summary(pl.UTF-8):   Rozszerzone informacje o plikach graficznych
Group:		X11/Applications/Graphics
Requires:	konqueror >= %{version}

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl.UTF-8
Ten pakiet dodaje do okna dialogowego "właściwości pliku" konquerora
dodatkową zakładkę z rozszerzonymi informacjami o pliku.

%package kgamma
Summary:	A monitor calibration tool
Summary(pl.UTF-8):   Narzędzie do kalibracji monitora
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kgamma
A monitor calibration tool.

%description kgamma -l pl.UTF-8
Narzędzie do kalibracji monitora.

%package kghostview
Summary:	KDE Postscript viewer
Summary(pl.UTF-8):   Przeglądarka postscriptu dla KDE
Summary(pt_BR.UTF-8):   Programa de visualização de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	ghostscript
Requires:	kdebase-core >= %{_minbaseevr}

%description kghostview
KGhostView displays and prints PostScript (.ps, .eps) and Portable
Document Format (.pdf) files. It a port to KDE of Tim Theisen's
Ghostview program which uses Alladin Ghostscript to view documents
prepared in Adobe's PostScript page description language. PostScript
is the major page description language for printing on UNIX systems
and this application can be used to preview material intended for
printing or for reading documents online.

%description kghostview -l pl.UTF-8
KGhostView wyświetla i drukuje pliki w formacie PostScript (.ps, .eps)
oraz Portable Document Format (.pdf). Jest to port KDE programu
GhostView Tima Theisena, używającego Alladin Ghostscripta do
przeglądania dokumentów przygotowanych w języku opisu strony
PostScript Adobe'a. PostScript to główny język opisu strony używany do
drukowania w systemach uniksowych, a tej aplikacji można używać do
podglądu materiałów przeznaczonych do druku oraz do czytania
dokumentów online.

%description kghostview -l pt_BR.UTF-8
Programa de visualização de arquivos Postscript e PDF.

%package kiconedit
Summary:	KDE Icon Editor
Summary(pl.UTF-8):   Edytor ikon dla środowiska KDE
Summary(pt_BR.UTF-8):   Editor de ícones
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kiconedit
KDE Icon editor.

%description kiconedit -l pl.UTF-8
Edytor ikon dla KDE.

%description kiconedit -l pt_BR.UTF-8
Editor de ícones, lida inclusive com arquivos .ICO.

%package kmrml
Summary:	Advanced Search
Summary(pl.UTF-8):   Zaawansowane wyszukiwanie
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdegraphics-mrml

%description kmrml
This package provides graphics files advanced search with file
indexing.

%description kmrml -l pl.UTF-8
Ten pakiet umożliwia zaawansowane wyszukiwanie plików graficznych z
indeksowaniem plików.

%package kolourpaint
Summary:	KDE Painter
Summary(pl.UTF-8):   Program graficzny KDE
Summary(pt_BR.UTF-8):   Editor básico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdegraphics-kpaint

%description kolourpaint
A (very) simple painting program for KDE.

%description kolourpaint -l pl.UTF-8
(Bardzo) prosty program do rysowania pod KDE.

%description kolourpaint -l pt_BR.UTF-8
Editor básico de imagens bitmap.

%package kooka
Summary:	Scanning tool
Summary(pl.UTF-8):   Narzędzie do skanowania
Summary(pt_BR.UTF-8):   Um programa de rasterização de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kooka
Kooka is a KDE application that enables easy scanning using SANE
libraries.

%description kooka -l pl.UTF-8
Kooka to aplikacja KDE umożliwiająca łatwe skanowanie przy użyciu
bibliotek SANE.

%description kooka -l pt_BR.UTF-8
Um programa de rasterização de imagens, baseado no SANE e libkscan.

%package kpdf
Summary:	Kpdf is an xpdf based pdf viewer for KDE
Summary(pl.UTF-8):   Kpdf - program bazujący na xpdf do przeglądania plików pdf w KDE
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kpdf
Kpdf is an xpdf based pdf viewer for KDE.

%description kpdf -l pl.UTF-8
Program bazujący na xpdf do przeglądania plików pdf w KDE.

%package kpovmodeler
Summary:	Povary Modeler
Summary(pl.UTF-8):   Modeler Povary
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	povray

%description kpovmodeler
Modeler for POV-Ray scenes.

%description kpovmodeler -l pl.UTF-8
Modeler do scen POV-Raya.

%package kruler
Summary:	KRuler
Summary(pl.UTF-8):   Linijka dla KDE
Summary(pt_BR.UTF-8):   Régua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl.UTF-8
KRuler jest prostą aplikacją, z tylko jednym celem w życiu: mierzenie
odległości na ekranie.

%description kruler -l pt_BR.UTF-8
Régua de pixels para a tela.

%package ksnapshot
Summary:	KDE Snap Shot
Summary(pl.UTF-8):   Program do przechwytywania ekranu dla KDE
Summary(pt_BR.UTF-8):   Programa de captura de tela
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description ksnapshot
KSnapshot is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description ksnapshot -l pl.UTF-8
KSnapshot to prosta aplikacja do robienia zrzutów ekranu. Potrafi
przechwytywać obraz całego pulpitu lub tylko pojedynczego okna. Obrazy
mogą być następnie zapisane w wielu formatach.

%description ksnapshot -l pt_BR.UTF-8
Programa de captura de tela.

%package ksvg
Summary:	Scalable Vector Graphics for KDE
Summary(pl.UTF-8):   Skalowalna grafika wektorowa (SVG) dla KDE
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{_minlibsevr}

%description ksvg
KSVG is a KDE implementation of the Scalable Vector Graphics
Specifications.

%description ksvg -l pl.UTF-8
KSVG stanowi implementację dla KDE specyfikacji skalowalnej grafiki
wektorowej (SVG - Scalable Vector Graphics).

%package kuickshow
Summary:	Image viewer/browser
Summary(pl.UTF-8):   Przeglądarka obrazków
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}
Provides:	kuickshow
Obsoletes:	kuickshow

%description kuickshow
KuickShow is a comfortable image browser/viewer. It displays a
filebrowser where you can select images which are then shown. The
following image formats are supported: jpg, gif, tiff, png, bmp, psd,
xpm, xbm, eim. Images can be displayed either in their own window, as
large as the image, or fullscreen.

%description kuickshow -l pl.UTF-8
KuickShow to wygodna przeglądarka obrazków. Wyświetla przeglądarkę
plików, w której można wybierać obrazki do pokazania. Obsługiwane są
następujące formaty obrazków: jpg, gif, tiff, png, bmp, psd, xpm, xbm,
eim. Obrazki mogą być wyświetlane w swoim oknie o rozmiarze obrazka
lub na pełnym ekranie.

%package kview
Summary:	KDE graphics file viewer
Summary(pl.UTF-8):   Przeglądarka plików graficznych dla KDE
Summary(pt_BR.UTF-8):   Visualizador de imagens
Group:		X11/Applications/Graphics
Requires:	kdebase-core >= %{_minbaseevr}

%description kview
KView is an image viewer for the KDE desktop. You can view graphics of
many different formats such as PostScript, TIFF etc. By saving your
files in a different format than the original you can easily convert
images to other graphics formats. In addition, KView provides some
nice little features for doing simple image processing, like
stretching/shrinking, rotation and filtering. You can tile your images
directly onto the desktop as a background picture, or arrange them in
a little slideshow.

%description kview -l pl.UTF-8
KView to przeglądarka plików graficznych dla KDE. Pozwala oglądać
grafikę w wielu różnych formatach, takich jak PostScript, TIFF itd.
Zapisując pliki w innym formacie niż oryginalny można łatwo
przekonwertować obrazki do innych formatów graficznych. Ponadto KView
dostarcza pewnych możliwości prostej obróbki obrazu, takich jak
rozciąganie/zmniejszanie, obracanie i filtrowanie. Można umieszczać
obrazki bezpośrednio na pulpicie jako tło lub łączyć je w przegląd
slajdów.

%description kview -l pt_BR.UTF-8
Visualizador de imagens poderoso para KDE.

%package kviewshell
Summary:	KDE generic framework for graphics viewers
Summary(pl.UTF-8):   Szkielet dla przeglądarek grafiki
Group:		X11/Applications/Graphics
Requires:	kdelibs >= %{_minlibsevr}
Conflicts:	kdegraphics-kview < 9:3.2.90.040514

%description kviewshell
KDE generic framework for graphics viewers allowing them to be
embedded in KDE applications.

%description kviewshell -l pl.UTF-8
Szkielet KDE dla przeglądarek grafiki pozwala na zagnieżdżnie w
aplikacjach KDE.

%prep
%setup -q
#%patch100 -p0
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Graphics;Viewer;/' \
	kdvi/kdvi.desktop \
	kfax/kfax.desktop \
	kview/kview.desktop \
	kuickshow/src/kuickshow.desktop \
	kghostview/kghostview.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Graphics;Viewer;PDFViewer;/' \
	kpdf/shell/kpdf.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Graphics;Scanning;/' \
	kooka/kooka.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Graphics;/' \
	kcoloredit/kcolorchooser.desktop \
	kcoloredit/kcoloredit.desktop \
	ksnapshot/ksnapshot.desktop \
	kruler/kruler.desktop \
	kolourpaint/kolourpaint.desktop \
	kiconedit/kiconedit.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Graphics;/' \
	kpovmodeler/kpovmodeler.desktop
for f in `find . -name *.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
cp %{_datadir}/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs

%if !%{with kuickshow}
export DO_NOT_COMPILE="$DO_NOT_COMPILE kuickshow"
%endif

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
	--enable-kpdf-drm=%{!?with_protections:no}%{?with_protections:yes} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kamera	--with-kde
%find_lang kcoloredit	--with-kde
%find_lang kgamma	--with-kde
%find_lang kdvi		--with-kde
%find_lang kghostview	--with-kde
%find_lang kiconedit	--with-kde
%find_lang kolourpaint	--with-kde
%find_lang kooka	--with-kde
%find_lang kpdf		--with-kde
%find_lang kpovmodeler	--with-kde
%find_lang kruler	--with-kde
%find_lang ksnapshot	--with-kde
%find_lang kuickshow	--with-kde
%find_lang kview	--with-kde

rm -f $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/kruler.desktop
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	kghostview	-p /sbin/ldconfig
%postun	kghostview	-p /sbin/ldconfig

%post	kooka		-p /sbin/ldconfig
%postun	kooka		-p /sbin/ldconfig

%post	ksvg		-p /sbin/ldconfig
%postun	ksvg		-p /sbin/ldconfig

%post	kview		-p /sbin/ldconfig
%postun	kview		-p /sbin/ldconfig

%post	kviewshell	-p /sbin/ldconfig
%postun	kviewshell	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkscan.so
%attr(755,root,root) %{_libdir}/libkmultipage.so
%attr(755,root,root) %{_libdir}/libkimageviewer.so
%attr(755,root,root) %{_libdir}/libksvg.so
%attr(755,root,root) %{_libdir}/libtext2path.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_includedir}/dom/*
%{_includedir}/ksvg
%{_includedir}/kviewshell
%{_includedir}/libtext2path-0.1

%files daemonwatcher
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kded_daemonwatcher.so
%{_datadir}/services/kded/daemonwatcher.desktop

%files kamera -f kamera.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kcm_kamera.so
%attr(755,root,root) %{_libdir}/kde3/kio_kamera.so
%{_datadir}/services/camera.protocol
%{_desktopdir}/kde/kamera.desktop
%{_iconsdir}/*/*/*/camera*

%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_desktopdir}/kde/kcolorchooser.desktop
%{_iconsdir}/[!l]*/*/*/kcolorchooser.*

%files kcoloredit -f kcoloredit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_datadir}/apps/kcoloredit
%{_desktopdir}/kde/kcoloredit.desktop
%{_iconsdir}/[!l]*/*/*/kcoloredit.*

%files kdvi -f kdvi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdvi
%attr(755,root,root) %{_libdir}/kde3/kdvipart.so
%{_datadir}/apps/kdvi
%{_datadir}/config.kcfg/kdvi.kcfg
%{_datadir}/services/kdvimultipage.desktop
%{_desktopdir}/kde/kdvi.desktop
%{_iconsdir}/*/*/*/kdvi.*

%files kfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%attr(755,root,root) %{_bindir}/kfaxview
%attr(755,root,root) %{_libdir}/libkfaximage.so
%attr(755,root,root) %{_libdir}/kde3/kfaxviewpart.so
%{_datadir}/apps/kfax/
%{_datadir}/apps/kfaxview
%{_datadir}/services/kfaxmultipage.desktop
%{_datadir}/services/kfaxmultipage_tiff.desktop
%{_desktopdir}/kde/kfax.desktop
%{_desktopdir}/kde/kfaxview.desktop
%{_iconsdir}/*/*/*/kfax.*
%{_iconsdir}/[!l]*/*/*/kfaxview.*

%files kfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/gsthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/gsthumbnail.desktop
%{_datadir}/services/kfile_*.desktop

%files kgamma -f kgamma.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xf86gammacfg
%attr(755,root,root) %{_libdir}/kde3/kcm_kgamma.so
%{_datadir}/apps/kgamma
%{_desktopdir}/kde/kgamma.desktop
%{_iconsdir}/*/*/apps/kgamma.png

%files kghostview -f kghostview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%attr(755,root,root) %{_libdir}/libkghostviewlib.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/libkghostviewpart.so
%{_datadir}/apps/kconf_update/kghostview.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/update-to-xt-names.pl
%{_datadir}/apps/kghostview
%{_datadir}/config.kcfg/kghostview.kcfg
%{_datadir}/services/kghostview_part.desktop
%{_desktopdir}/kde/kghostview.desktop
%{_iconsdir}/*/*/*/kghostview.*

%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_datadir}/apps/kiconedit
%{_desktopdir}/kde/kiconedit.desktop
%{_iconsdir}/*/*/*/kiconedit.*

%files kmrml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mrmlsearch
%attr(755,root,root) %{_libdir}/libkdeinit_mrmlsearch.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kmrml.so
%attr(755,root,root) %{_libdir}/kde3/kio_mrml.so
%attr(755,root,root) %{_libdir}/kde3/libkmrmlpart.so
%attr(755,root,root) %{_libdir}/kde3/mrmlsearch.so
%{_datadir}/mimelnk/text/mrml.desktop
%{_datadir}/services/mrml.protocol
%{_datadir}/services/mrml_part.desktop
%{_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{_desktopdir}/kde/kcmkmrml.desktop

%files kolourpaint -f kolourpaint.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolourpaint
%{_datadir}/apps/kolourpaint
%{_desktopdir}/kde/kolourpaint.desktop
%{_iconsdir}/[!l]*/*/*/kolourpaint.*

%files kooka -f kooka.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kooka
%attr(755,root,root) %{_libdir}/libkscan.so.*.*.*
%{_datadir}/apps/kooka
%{_datadir}/config/kookarc
%{_datadir}/services/scanservice.desktop
%{_desktopdir}/kde/kooka.desktop
%{_iconsdir}/*/*/actions/palette*

%files kpdf -f kpdf.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpdf
%attr(755,root,root) %{_libdir}/kde3/libkpdfpart.so
%{_datadir}/apps/kpdf
%{_datadir}/apps/kpdfpart
%{_datadir}/config.kcfg/kpdf.kcfg
%{_datadir}/services/kpdf_part.desktop
%{_desktopdir}/kde/kpdf.desktop
%{_iconsdir}/[!l]*/*/*/kpdf.*

%files kpovmodeler -f kpovmodeler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpovmodeler
%attr(755,root,root) %{_libdir}/libkpovmodeler.so.*
%attr(755,root,root) %{_libdir}/kde3/libkpovmodelerpart.so*
%{_datadir}/apps/kpovmodeler
%{_desktopdir}/kde/kpovmodeler.desktop
%{_iconsdir}/[!l]*/*/*/kpovmodeler*

%files kruler -f kruler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_desktopdir}/kde/kruler.desktop
%{_iconsdir}/*/*/apps/kruler.*

%files ksnapshot -f ksnapshot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%{_desktopdir}/kde/ksnapshot.desktop
%{_iconsdir}/*/*/apps/ksnapshot.*

%files ksvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/printnodetest
%attr(755,root,root) %{_bindir}/svgdisplay
%attr(755,root,root) %{_libdir}/libksvg.so.*.*.*
%attr(755,root,root) %{_libdir}/libtext2path.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/libksvgplugin.so
%attr(755,root,root) %{_libdir}/kde3/libksvgrendererlibart.so
%attr(755,root,root) %{_libdir}/kde3/svgthumbnail.so
%{_datadir}/apps/ksvg
%{_datadir}/services/ksvglibartcanvas.desktop
%{_datadir}/services/ksvgplugin.desktop
%{_datadir}/services/svgthumbnail.desktop
%{_datadir}/servicetypes/ksvgrenderer.desktop

%if %{with kuickshow}
%files kuickshow -f kuickshow.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%attr(755,root,root) %{_libdir}/libkdeinit_kuickshow.so
%attr(755,root,root) %{_libdir}/kde3/kuickshow.so
%{_datadir}/apps/kuickshow
%{_desktopdir}/kde/kuickshow.desktop
%{_iconsdir}/[!l]*/*/*/kuickshow.*
%endif

%files kview -f kview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kview
%attr(755,root,root) %{_libdir}/libkdeinit_kview.so
%attr(755,root,root) %{_libdir}/libkimageviewer.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewcanvasconfig.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewgeneralconfig.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewpluginsconfig.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kviewviewerpluginsconfig.so
%attr(755,root,root) %{_libdir}/kde3/kview.so
%attr(755,root,root) %{_libdir}/kde3/kview_browserplugin.so
%attr(755,root,root) %{_libdir}/kde3/kview_effectsplugin.so
%attr(755,root,root) %{_libdir}/kde3/kview_presenterplugin.so
%attr(755,root,root) %{_libdir}/kde3/kview_scannerplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkviewcanvas.so
%attr(755,root,root) %{_libdir}/kde3/libkviewviewer.so
%attr(755,root,root) %{_libdir}/kde3/libphotobook.so
%{_datadir}/apps/kview
%{_datadir}/apps/kviewviewer
%{_datadir}/apps/photobook
%{_datadir}/services/kconfiguredialog/kviewcanvasconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewgeneralconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewpluginsconfig.desktop
#%{_datadir}/services/kconfiguredialog/kviewpresenterconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewviewerpluginsconfig.desktop
%{_datadir}/services/kviewcanvas.desktop
%{_datadir}/services/kviewviewer.desktop
%{_datadir}/servicetypes/kimageviewer.desktop
%{_datadir}/servicetypes/kimageviewercanvas.desktop
%{_datadir}/services/photobook.desktop
%{_desktopdir}/kde/kview.desktop
%{_iconsdir}/*/*/*/kview.png
%{_iconsdir}/crystalsvg/*/apps/photobook.png

%files kviewshell
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kviewshell
%attr(755,root,root) %{_libdir}/libkmultipage.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/emptymultipagepart.so
%attr(755,root,root) %{_libdir}/kde3/kviewerpart.so
%{_datadir}/apps/kviewerpart
%{_datadir}/apps/kviewshell
%{_datadir}/config.kcfg/kviewshell.kcfg
%{_datadir}/services/emptymultipage.desktop
%{_datadir}/servicetypes/kmultipage.desktop
%{_iconsdir}/*/*/*/kviewshell.png
# New
%attr(755,root,root) %{_libdir}/kde3/djvuviewpart.so
%attr(755,root,root) %{_libdir}/kde3/libdjvu.so
%{_datadir}/apps/djvumultipage.rc
%{_datadir}/config.kcfg/djvumultipage.kcfg
%{_datadir}/services/djvumultipage.desktop
