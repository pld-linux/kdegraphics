Summary:     K Desktop Environment - Graphic Applications
Summary(pl): K Desktop Environment - Aplikacje graficzne
Name:        kdegraphics
Version:     1.1.1
Release:     2
#ftp://ftp.kde.org/
#patch = pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/
Source:	     %{name}-%{version}.tar.bz2
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Copyright:   GPL
Requires:    qt >= 1.44, kdelibs = %{version}
Vendor:      The KDE Team
BuildRoot:   /tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
Graphic applications for the K Desktop Environment.

Included with this package are:

KDVI: displays TeX's device independent (.dvi) files
KFax: displays fax files
KFract: a fractal generator
KGhostview: displays postscript (.ps) files
KIconedit: icon editor
KPaint: a simple drawing program
KSnapshot: screen capture
KView: displays numerous graphic file formats 

%description -l pl
Aplikacje graficzne dla KDE.
Pakiet zawiera:
  KDVI - Przegl�darka plik�w DVI
  KFax - Program do wy�wietlania faks�w
  KFract - Generator fraktali
  KGhostview - Program do ogl�dania postscriptu (.ps)
  KIconedit - Program do edycji ikon dla KDE
  KPaint - Prosty program do grafiki rastrowej
  KSnapshot - program do przechwytywania wygl�du ekranu
  KView - Przegl�darka plik�w graficznych

%package kdvi
Summary:     KDE DVI viewer
Summary(pl): Przegl�darka plik�w DVI dla KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kdvi
A tool for viewing DVI files generated by TeX system.

%description -l pl kdvi
Program do przegl�dania plik�w DVI.

%package ksnapshot
Summary:     KDE Snap Shot
Summary(pl): Program do przechwytywania ekranu dla KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description ksnapshot
Snapshot program for KDE.

%description -l pl ksnapshot
Program do przechwytywania ekranu dla KDE.

%package kiconedit
Summary:     KDE Icon Editor
Summary(pl): Edytor ikon w �rodowisku KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kiconedit
KDE Icon editor.

%description -l pl kiconedit
Edytor ikon dla KDE.

%package kfax
Summary:     KDE Fax viewer	
Summary(pl): Przegl�darka faks�w dla KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kfax
A Fax viewer for KDE.

%description -l pl kfax
Program ten umo�liwia przegl�danie plik�w faksowych (G3)

%package kfract
Summary:     KDE fractal generator	
Summary(pl): Generator fraktali dla KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kfract
A Fractal generator for KDE.

%description -l pl kfract
Generator fraktali dla KDE

%package kghostview 
Summary:     KDE Postscript viewer
Summary(pl): Przegl�darka postscriptu dla KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kghostview
Postscript files (.ps) viewer for KDE

%description -l pl kghostview
Program ten umo�liwia przegl�danie plik�w postscriptowych (.ps) 

%package kpaint
Summary:     KDE Painter
Summary(pl): Program graficzny KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kpaint
A (very) simple painting program for KDE.

%description -l pl kpaint
(Bardzo) prosty program do rysowania pod KDE.

%package kview
Summary:     KDE graphics file viewer
Summary(pl): Przegl�darka plik�w graficznych dla KDE
Group:       X11/KDE/Graphics
Group(pl):   X11/KDE/Grafika
Requires:    qt >= 1.44, kdelibs = %{version}

%description kview
A graphics files viewer for KDE.

%description -l pl kfax
Program ten umo�liwia ogl�danie r�nych plik�w graficznych (G3)

%prep
%setup -q

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti -fno-exceptions" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang kdvi
%find_lang kfax
%find_lang kfract
%find_lang kghostview
%find_lang kpaint
%find_lang kview
%find_lang ksnapshot
%find_lang kiconedit

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KDVI
#################################################

%files kdvi -f kdvi.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/kdvi.kdelnk

%attr(755, root, root) %{_bindir}/kdvi

%lang(en) %{_datadir}/kde/doc/HTML/en/kdvi
%lang(fi) %{_datadir}/kde/doc/HTML/fi/kdvi

%{_datadir}/kde/apps/kdvi/

%{_datadir}/kde/icons/kdvi.xpm
%{_datadir}/kde/icons/mini/kdvi.xpm

#################################################
#             KFAX
#################################################

%files kfax -f kfax.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/KFax.kdelnk

%attr(755, root, root) %{_bindir}/kfax

%lang(en) %{_datadir}/kde/doc/HTML/en/kfax

%{_datadir}/kde/apps/kfax/

%{_datadir}/kde/icons/mini/kfax.xpm
%{_datadir}/kde/icons/kfax.xpm

#################################################
#             KFract
#################################################

%files kfract -f kfract.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/kfract.kdelnk

%attr(755,root,root) %{_bindir}/kfract

%lang(en) %{_datadir}/kde/doc/HTML/en/kfract

%{_datadir}/kde/icons/mini/kfract.xpm
%{_datadir}/kde/icons/kfract.xpm

#################################################
#             KGHOSTVIEW
#################################################

%files kghostview -f kghostview.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/kghostview.kdelnk

%attr(755, root, root) %{_bindir}/kghostview

%lang(en) %{_datadir}/kde/doc/HTML/en/kghostview

%{_datadir}/kde/icons/mini/kghostview.xpm
%{_datadir}/kde/icons/kghostview.xpm

#################################################
#             KPAINT
#################################################

%files kpaint -f kpaint.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/kpaint.kdelnk

%attr(755, root, root) %{_bindir}/kpaint

%lang(en) %{_datadir}/kde/doc/HTML/en/kpaint

%{_datadir}/kde/apps/kpaint

%{_datadir}/kde/icons/mini/kpaint.xpm
%{_datadir}/kde/icons/kpaint.xpm

#################################################
#             KSNAPSHOT
#################################################

%files ksnapshot -f ksnapshot.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/ksnapshot.kdelnk

%attr(755, root, root) %{_bindir}/ksnapshot

%lang(cs) %{_datadir}/kde/doc/HTML/cs/ksnapshot
%lang(en) %{_datadir}/kde/doc/HTML/en/ksnapshot

%{_datadir}/kde/icons/mini/ksnapshot.xpm
%{_datadir}/kde/icons/ksnapshot.xpm

#################################################
#             KVIEW
#################################################

%files kview -f kview.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/kview.kdelnk

%attr(755, root, root) %{_bindir}/kview

%lang(en) %{_datadir}/kde/doc/HTML/en/kview

%{_datadir}/kde/icons/mini/kview.xpm
%{_datadir}/kde/icons/kview.xpm

#################################################
#             KICONEDIT
#################################################

%files kiconedit -f kiconedit.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Graphics/kiconedit.kdelnk

%attr(755, root, root) %{_bindir}/kiconedit

%lang(da) %{_datadir}/kde/doc/HTML/da/kiconedit
%lang(en) %{_datadir}/kde/doc/HTML/en/kiconedit

%{_datadir}/kde/apps/kiconedit

%{_datadir}/kde/icons/mini/kiconedit.xpm
%{_datadir}/kde/icons/kiconedit.xpm
