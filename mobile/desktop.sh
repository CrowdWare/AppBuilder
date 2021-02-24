mkdir build-desktop
cd build-desktop
/Users/art/qt/5.12.3/clang_64/bin/qmake ../main.pro
make
make install INSTALL_ROOT=/Users/art/SourceCode/AppBuilder/mobile/build-desktop/
cd ..