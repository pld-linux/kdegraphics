# TODO:
#   pdf plugin requires pdfinfo from xpdf to show pdf info.
#   for some reason it checks for kpsewhich from tetex.
#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	K Desktop Environment - Graphic Applications
Summary(es):	K Desktop Environment - aplicaciones gr�ficas
Summary(ko):	K ����ũž ȯ�� - �׷��� �������α׷�
Summary(pl):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR):	K Desktop Environment - Aplica��es gr�ficas
Summary(zh_CN):	KDEͼ��Ӧ�ó���
Name:		kdegraphics
Version:	3.0.4
Release:	4
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-extra_icons.tar.bz2
Patch0:		%{name}-fix-gs-configure.patch
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	awk
BuildRequires:	gettext-devel
BuildRequires:	gphoto2-devel
BuildRequires:	imlib-devel
BuildRequires:	kdelibs-devel >= %{version}
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
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1
%define		_with_pixmapsubdirs		1

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
Summary(ko):	kdegraphics ���� ���߿� �ʿ��� ����
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
Color chooser.

%description kcolorchooser -l pl
Wybieracz kolor�w.

%package kuickshow
Summary:	Image viewer/browser
Summary(pl):	Przegl�darka obrazk�w
Group:		X11/Applications/Graphics
Requires:	kdelibs = %{version}
Provides:	kuickshow
Obsoletes:	kuickshow

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
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#%{__make} -f Makefile.cvs

%configure \
	--enable-final \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Settings/KDE,Graphics/Viewers}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	RUN_KAPPFINDER=no

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/Peripherals $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE
mv $RPM_BUILD_ROOT%{_applnkdir}/Graphics/{kdvi,kfax,kghostview,kuickshow,kview}.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
cd $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/Peripherals
cat kamera.desktop |sed -e 's/Peripherals[/]kamera/kamera/' > kamera.desktop.tmp
mv -f kamera.desktop.tmp kamera.desktop
cd -

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{kdvi,kfax,kfract,kghostview,kiconedit,kpaint,kruler,ksnapshot,kview}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}

%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
# moved
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{kdvi,kfax,kfract,kghostview,kiconedit,kpaint,kruler,ksnapshot,kview}.png
# resized
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{camera,kcoloredit,kuickshow}.png
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

%find_lang kcmkamera	--with-kde
%find_lang kcoloredit	--with-kde
%find_lang kdvi	--with-kde
%find_lang kfax	--with-kde
%find_lang kfile_pdf	--with-kde
%find_lang kfile_png	--with-kde
%find_lang kfile_ps	--with-kde
%find_lang kpixmap2bitmap	--with-kde
cat kpixmap2bitmap.lang kfile_pdf.lang kfile_png.lang kfile_ps.lang >> %{name}.lang
%find_lang kfract	--with-kde
%find_lang kghostview	--with-kde
%find_lang kiconedit	--with-kde
%find_lang kooka	--with-kde
%find_lang libkscan	--with-kde
cat libkscan.lang >> kooka.lang
%find_lang kpaint	--with-kde
%find_lang kruler	--with-kde
%find_lang ksnapshot	--with-kde
%find_lang kuickshow	--with-kde
%find_lang kview	--with-kde
%find_lang kviewshell	--with-kde
cat kviewshell.lang >> kview.lang

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kfile_*.??
%{_datadir}/services/kfile_*.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libkscan.so
%{_libdir}/lib*.la

#################################################
#             KDVI
#################################################
%files kdvi -f kdvi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdvi
%attr(755,root,root) %{_libdir}/libkdvi.so
%{_applnkdir}/Graphics/Viewers/kdvi.desktop
%{_datadir}/apps/kdvi
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kdvi.png}
%{_pixmapsdir}/kdvi.png

#################################################
#             KFAX
#################################################
%files kfax -f kfax.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%attr(755,root,root) %{_libdir}/libkfax.so
%{_applnkdir}/Graphics/Viewers/kfax.desktop
%{_datadir}/apps/kfax
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kfax.png}
%{_pixmapsdir}/kfax.png

#################################################
#             KFRACT
#################################################
%files kfract -f kfract.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfract
%{_applnkdir}/Graphics/kfract.desktop
%{_datadir}/apps/kfract
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kfract.png}
%{_pixmapsdir}/kfract.png

#################################################
#             KGHOSTVIEW
#################################################
%files kghostview -f kghostview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kghostview
%attr(755,root,root) %{_libdir}/libkghostview.so
%{_applnkdir}/Graphics/Viewers/kghostview.desktop
%{_datadir}/apps/kghostview
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kghostview.png}
%{_pixmapsdir}/kghostview.png

#################################################
#             KICONEDIT
#################################################
%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_applnkdir}/Graphics/kiconedit.desktop
%{_datadir}/apps/kiconedit
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kiconedit.png}
%{_pixmapsdir}/kiconedit.png

#################################################
#             KPAINT
#################################################
%files kpaint -f kpaint.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpaint
%{_applnkdir}/Graphics/kpaint.desktop
%{_datadir}/apps/kpaint
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kpaint.png}
%{_pixmapsdir}/kpaint.png

#################################################
#             KRULER
#################################################
%files kruler -f kruler.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_applnkdir}/Graphics/kruler.desktop
%{_datadir}/apps/kruler
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kruler.png}
%{_pixmapsdir}/kruler.png

#################################################
#             KSNAPSHOT
#################################################
%files ksnapshot -f ksnapshot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%{_applnkdir}/Graphics/ksnapshot.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/ksnapshot.png}
%{_pixmapsdir}/ksnapshot.png

#################################################
#             KVIEW
#################################################
%files kview -f kview.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kview
%attr(755,root,root) %{_bindir}/kviewshell
%attr(755,root,root) %{_libdir}/kview.so
%attr(755,root,root) %{_libdir}/libkviewpart.so
%attr(755,root,root) %{_libdir}/libkviewerpart.so
%attr(755,root,root) %{_libdir}/libkmultipage.*.*
%attr(755,root,root) %{_libdir}/libkpagetest.so
%{_datadir}/apps/kview*
%{_applnkdir}/Graphics/Viewers/kview.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kview*}
%{!?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kviews*}
%{_pixmapsdir}/kview*

#################################################
#             KOOKA
#################################################
%files kooka -f kooka.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kooka
%attr(755,root,root) %{_libdir}/libkscan.so.*.*.*
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
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kcoloredit.png}
%{_pixmapsdir}/kcoloredit.png

#################################################
#             KCOLORCHOOSER
#################################################
%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%attr(755,root,root) %{_libdir}/kcolorchooser.so
%{_applnkdir}/Graphics/kcolorchooser.desktop
%{_pixmapsdir}/kcolorchooser.png

#################################################
#             KUICKSHOW
#################################################
%files kuickshow -f kuickshow.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%attr(755,root,root) %{_libdir}/kuickshow.so
%{_datadir}/apps/kuickshow
%{_applnkdir}/Graphics/Viewers/kuickshow.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/apps/kuickshow.png}
%{_pixmapsdir}/kuickshow.png

#################################################
#             KAMERA
#################################################
%files kamera -f kcmkamera.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_kamera.??
%attr(755,root,root) %{_libdir}/kde3/libkcm_kamera.??
%{_datadir}/services/kamera.protocol
%{_pixmapsdir}/*/*/actions/camera_test.*
%{_applnkdir}/Settings/KDE/Peripherals/kamera.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*/*/*/camera.png}
%{_pixmapsdir}/camera.png
