# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.
%define		_ver		3.0.2
#define		_sub_ver
%define		_rel		1

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	K Desktop Environment - Graphic Applications
Summary(es):	K Desktop Environment - aplicaciones gr�ficas
Summary(pl):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - Aplica��es gr�ficas
Name:		kdegraphics
Version:	%{_version}
Release:	%{_release}
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel >= %{_version}
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libungif-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	sane-backends-devel
BuildRequires:	gettext-devel
BuildRequires:	libxml2-devel
BuildRequires:	gphoto2-lib-devel
BuildRequires:	libxml2-progs
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

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

%description devel
kdegraphics development files.

%description devel -l pl
Pliki dla programist�w kdegraphics.

%description devel -l pt_BR
Arquivos de inclus�o para compila��o de aplica��es que usem as
bibliotecas do kdegraphics.

%package kdvi
Summary:	KDE DVI viewer
Summary(pl):	Przegl�darka plik�w DVI dla KDE
Summary(pt_BR):	Programa de exibi��o de DVIs
Group:		X11/Applications/Graphics
Requires:	qt >= 2.2
Requires:	kdelibs = %{version}

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
Requires:	qt >= 2.2
Requires:	kdelibs = %{version}

%description kfax
A Fax viewer for KDE.

%description kfax -l pl
Program ten umo�liwia przegl�danie plik�w faksowych (G3)

%description kfax -l pt_BR
Programa de visualiza��o de faxes (formato TIFF).

%package kfract
Summary:	KDE fractal generator
Summary(pl):	Generator fraktali dla KDE
Summary(pt_BR):	Gerador de fractais
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kfract
A Fractal generator for KDE.

%description kfract -l pl
Generator fraktali dla KDE

%description kfract -l pt_BR
Gerador de fractais.

%package kghostview
Summary:	KDE Postscript viewer
Summary(pl):	Przegl�darka postscriptu dla KDE
Summary(pt_BR):	Programa de visualiza��o de arquivos Postscript e PDF
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

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
Requires:	kdelibs = %{version}

%description kiconedit
KDE Icon editor.

%description kiconedit -l pl
Edytor ikon dla KDE.

%description kiconedit -l pt_BR
Editor de �cones, lida inclusive com arquivos .ICO.

%package kpaint
Summary:	KDE Painter
Summary(pl):	Program graficzny KDE
Summary(pt_BR):	Editor b�sico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kpaint
A (very) simple painting program for KDE.

%description kpaint -l pl
(Bardzo) prosty program do rysowania pod KDE.

%description kpaint -l pt_BR
Editor b�sico de imagens bitmap.

%package kruler
Summary:	KRuler
Summary(pl):	Linijka dla KDE
Summary(pt_BR):	R�gua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

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
Requires:	kdelibs = %{version}

%description ksnapshot
Snapshot program for KDE.

%description ksnapshot -l pl
Program do przechwytywania ekranu dla KDE.

%description ksnapshot -l pt_BR
Programa de captura de tela.

%package kview
Summary:	KDE graphics file viewer
Summary(pl):	Przegl�darka plik�w graficznych dla KDE
Summary(pt_BR):	Visualizador de imagens
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kview
A graphics files viewer for KDE.

%description kview -l pl
Program ten umo�liwia ogl�danie r�nych plik�w graficznych (G3).

%description kview -l pt_BR
Visualizador de imagens poderoso para KDE.

%package kooka
Summary:	Scanning tool
Summary(pl):	Narz�dzie do skanowania
Summary(pt_BR):	Um programa de rasteriza��o de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kooka
Scanning tool.

%description kooka -l pl
Narz�dzie do skanowania.

%description kooka -l pt_BR
Um programa de rasteriza��o de imagens, baseado no SANE e libkscan.

%package kcoloredit
Summary:	Color palette editor
Summary(pl):	Edytor palety kolor�w
Summary(pt_BR):	Editor de cores
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kcoloredit
Color palette editor.

%description kcoloredit -l pl
Edytor palety kolor�w.

%description kcoloredit -l pt_BR
Editor de cores do KDE.

%package kcolorchooser
Summary:	Color chooser
Summary(pl):	Wybieracz kolr�w
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kcolorchooser
Color chooser

%description kcolorchooser -l pl
Wybieracz kolor�w.

%package kuickshow
Summary:	Image viewer/browser
Summary(pl):	Przegl�darka obrazk�w
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kuickshow
Image viewer/browser.

%description kuickshow -l pl
Przegl�darka obrazk�w.

%package kamera
Summary:	Digital camera support
Summary(pl):	Obs�uga kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}

%description kamera
Digital camera support.

%description kamera -l pl
Obs�uga kamer cyfrowych.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi

#autoconf
%{__make} -f Makefile.cvs

%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} RUN_KAPPFINDER=no DESTDIR=$RPM_BUILD_ROOT$ install

install -d $RPM_BUILD_ROOT%{_applnkdir}/{Graphics/Viewers,KDE}
mv $RPM_BUILD_ROOT%{_applnkdir}/Graphics{,/Viewers}/kghostview.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings,KDE}

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang kdvi --with-kde
#%find_lang kfax --with-kde
#%find_lang kfile_pdf --with-kde
#%find_lang kfile_png --with-kde
#%find_lang kfile_ps --with-kde
#cat kfile_pdf.lang kfile_png.lang kfile_ps.lang >>%{name}.lang
%find_lang kfract --with-kde
%find_lang kghostview --with-kde
%find_lang kiconedit --with-kde
%find_lang kpaint --with-kde
%find_lang kruler --with-kde
%find_lang ksnapshot --with-kde
%find_lang kview --with-kde
#%find_lang kviewshell --with-kde
#cat kviewshell.lang >> kview.lang
%find_lang kooka --with-kde
%find_lang kcoloredit --with-kde
%find_lang kuickshow --with-kde

%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%post   kdvi -p /sbin/ldconfig
%postun kdvi -p /sbin/ldconfig

%post   kfax -p /sbin/ldconfig
%postun kfax -p /sbin/ldconfig

%post   kghostview -p /sbin/ldconfig
%postun kghostview -p /sbin/ldconfig

%post   kview -p /sbin/ldconfig
%postun kview -p /sbin/ldconfig

%post   kooka -p /sbin/ldconfig
%postun kooka -p /sbin/ldconfig

%post   kcoloredit -p /sbin/ldconfig
%postun kcoloredit -p /sbin/ldconfig

%post   kcolorchooser -p /sbin/ldconfig
%postun kcolorchooser -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kfile_*.??
%{_datadir}/services/kfile_*.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libkscan.so

#################################################
#             KDVI
#################################################
%files kdvi -f kdvi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdvi
%attr(755,root,root) %{_libdir}/libkdvi.??
%{_datadir}/apps/kdvi/
%{_applnkdir}/Graphics/kdvi.desktop
%{_pixmapsdir}/*/*/apps/kdvi.*

#################################################
#             KFAX
#################################################
%files kfax
# TODO -f kfax.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%attr(755,root,root) %{_libdir}/libkfax.??
%{_datadir}/apps/kfax/
%{_applnkdir}/Graphics/kfax.desktop
%{_pixmapsdir}/*/*/apps/kfax.*

#################################################
#             KFRACT
#################################################
%files kfract -f kfract.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfract
%{_datadir}/apps/kfract/
%{_applnkdir}/Graphics/kfract.desktop
%{_pixmapsdir}/*/*/apps/kfract.*

#################################################
#             KGHOSTVIEW
#################################################
%files kghostview -f kghostview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%attr(755,root,root) %{_libdir}/libkghostview.*
%{_datadir}/apps/kghostview
%{_applnkdir}/Graphics/Viewers/kghostview.desktop
%{_pixmapsdir}/*/*/apps/kghostview.*

#################################################
#             KICONEDIT
#################################################
%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_datadir}/apps/kiconedit
%{_applnkdir}/Graphics/kiconedit.desktop
%{_pixmapsdir}/*/*/apps/kiconedit.*

#################################################
#             KPAINT
#################################################
%files kpaint -f kpaint.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpaint
%{_datadir}/apps/kpaint
%{_applnkdir}/Graphics/kpaint.desktop
%{_pixmapsdir}/*/*/apps/kpaint.*

#################################################
#             KRULER
#################################################
%files kruler -f kruler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_applnkdir}/Graphics/kruler.desktop
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
#             KVIEW
#################################################
%files kview -f kview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kview
%attr(755,root,root) %{_bindir}/kviewshell
%attr(755,root,root) %{_libdir}/kview.??
%attr(755,root,root) %{_libdir}/libkviewpart.??
%attr(755,root,root) %{_libdir}/libkviewerpart.??
%attr(755,root,root) %{_libdir}/libkmultipage.*
%attr(755,root,root) %{_libdir}/libkpagetest.??
%{_datadir}/apps/kview*
%{_applnkdir}/Graphics/kview.desktop
%{_pixmapsdir}/*/*/apps/kview*

#################################################
#             KOOKA
#################################################
%files kooka -f kooka.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kooka
%attr(755,root,root) %{_libdir}/libkscan.so.*.*.*
%attr(755,root,root) %{_libdir}/libkscan.la
%{_datadir}/apps/kooka
%{_datadir}/services/scanservice.desktop
%{_applnkdir}/Graphics/kooka.desktop
%{_pixmapsdir}/*/*/actions/palette*

#################################################
#             KCOLOREDIT
#################################################
%files kcoloredit -f kcoloredit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_applnkdir}/Graphics/kcoloredit.desktop
%{_pixmapsdir}/*/*/apps/kcoloredit.*

#################################################
#             KCOLORCHOOSER
#################################################
%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%attr(755,root,root) %{_libdir}/kcolorchooser.??
%{_applnkdir}/Graphics/kcolorchooser.desktop

#################################################
#             KUICKSHOW
#################################################
%files kuickshow -f kuickshow.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%{_libdir}/kuickshow.??
%{_datadir}/apps/kuickshow
%{_applnkdir}/Graphics/kuickshow.desktop
%{_pixmapsdir}/*/*/apps/kuickshow.*

#################################################
#             KAMERA
#################################################
%files kamera
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_kamera.??
%{_libdir}/kde3/libkcm_kamera.??
%{_datadir}/services/kamera.protocol
%{_applnkdir}/KDE/Settings/Peripherals/kamera.desktop
%{_pixmapsdir}/*/*/actions/camera_test.*
%{_pixmapsdir}/*/*/apps/camera.*
%{_pixmapsdir}/*/*/devices/camera.*
%{_pixmapsdir}/*/*/filesystems/camera.*
