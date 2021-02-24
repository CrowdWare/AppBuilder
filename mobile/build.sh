export ANDROID_NDK_ROOT=/Users/art/Library/Android/sdk/ndk/19.2.5345600
export ANDROID_NDK_PLATFORM=android-28
export ANDROID_SDK_ROOT=/Users/art/Library/Android/sdk
mkdir build-android
cd build-android
/Users/art/qt/5.12.3/android_armv7/bin/qmake ../main.pro
make
make install INSTALL_ROOT=/Users/art/SourceCode/AppBuilder/mobile/build-android/
/Users/art/qt/5.12.3/android_armv7/bin/androiddeployqt --input /Users/art/SourceCode/AppBuilder/mobile/build-android/android-libmain.so-deployment-settings.json --output /Users/art/SourceCode/AppBuilder/mobile/build-android --android-platform android-28 --jdk /home/art/Software/jdk1.8.0_231/bin/java --gradle
cd ..

