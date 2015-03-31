Name: driller
Summary: Mr. Driller (C)NAMCO clone
Version: 0.05
Release: b2
URL: http://www.geocities.co.jp/Berkeley/2093/driller.html
Source0: %name-%version.tar.bz2
License: LGPL
Group: Amusements/Games
Buildroot: %{_tmppath}/%{name}-%{version}
Buildrequires: SDL-devel, SDL_mixer-devel
Requires: SDL_mixer >= 1.2.2

BuildArchitectures: i586


%description
Miss Driller, a high quality addictive game using SDL.


%prep
%setup -q

%build
#make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=%buildroot%{_prefix}
make


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/opt/game/%name/{arrows,player,susumi,system}
install -d $RPM_BUILD_ROOT/opt/game/%name/system/{bmp,wav}
strip drill
install -m 755 drill $RPM_BUILD_ROOT/opt/game/%name
cp -a drill.ini $RPM_BUILD_ROOT/opt/game/%name
cp -a drill.scr $RPM_BUILD_ROOT/opt/game/%name
cp -a drilltime.scr $RPM_BUILD_ROOT/opt/game/%name
cp -a engrave16.bmp $RPM_BUILD_ROOT/opt/game/%name
cp -a blockbg.txt $RPM_BUILD_ROOT/opt/game/%name
cp -a charabg.txt $RPM_BUILD_ROOT/opt/game/%name
cp -a otherbg.txt $RPM_BUILD_ROOT/opt/game/%name
cp -a wav.txt $RPM_BUILD_ROOT/opt/game/%name
cp -a COPYING $RPM_BUILD_ROOT/opt/game/%name
cp -a readme.txt $RPM_BUILD_ROOT/opt/game/%name
cp -a arrows/* $RPM_BUILD_ROOT/opt/game/%name/arrows
cp -a player/* $RPM_BUILD_ROOT/opt/game/%name/player
cp -a susumi/* $RPM_BUILD_ROOT/opt/game/%name/susumi
cp -a system/bmp/* $RPM_BUILD_ROOT/opt/game/%name/system/bmp
cp -a system/wav/* $RPM_BUILD_ROOT/opt/game/%name/system/wav

#install -d $RPM_BUILD_ROOT/etc/X11/applnk/Games
#install -m 644 kde/driller.desktop $RPM_BUILD_ROOT/etc/X11/applnk/Games
install -m 644 kde/driller.png $RPM_BUILD_ROOT/opt/game/%name

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor=%name              \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications  \
  --add-category X-Red-Hat-Base                  \
  --add-category Application                     \
  --add-category Game                            \
  kde/%{name}.desktop

# install icons and GNOME desktop entry
#cp -a icons $RPM_BUILD_ROOT/usr/share/%name
#cat >%name.desktop <<EOF
#[Desktop Entry]
#Name=Frozen Bubble
#TryExec=frozen-bubble
#Exec=frozen-bubble
#Icon=%{_prefix}/share/frozen-bubble/icons/frozen-bubble-icon-32x32.png
#Terminal=0
#Type=Application
#EOF
#mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
#desktop-file-install --vendor=%name              \
#  --dir $RPM_BUILD_ROOT%{_datadir}/applications  \
#  --add-category X-Red-Hat-Extra                 \
#  --add-category Application                     \
#  --add-category Game                            \
#  %{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/opt/game/%name/*
##/etc/X11/applnk/Games/*
%{_datadir}/applications
#%doc AUTHORS CHANGES COPYING README INSTALL
#%{_prefix}/bin/*
#%{_prefix}/lib/frozen-bubble
#%{_prefix}/share/frozen-bubble
#%{_datadir}/applications
# %{_prefix}/share/man/man3/*
#%{_prefix}/share/man/man6/*

%changelog
* Fri Oct 3 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Create for Berry Linux
