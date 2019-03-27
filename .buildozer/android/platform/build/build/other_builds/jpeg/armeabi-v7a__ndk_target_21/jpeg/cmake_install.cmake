# Install script for directory: /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "TRUE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/libturbojpeg.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE PROGRAM RENAME "tjbench" FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/tjbench-static")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/turbojpeg.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/libjpeg.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE PROGRAM RENAME "cjpeg" FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/cjpeg-static")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE PROGRAM RENAME "djpeg" FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/djpeg-static")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE PROGRAM RENAME "jpegtran" FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jpegtran-static")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/rdjpgcom")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/rdjpgcom" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/rdjpgcom")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/rdjpgcom")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/wrjpgcom")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/wrjpgcom" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/wrjpgcom")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/wrjpgcom")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/doc/libjpeg-turbo" TYPE FILE FILES
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/README.ijg"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/README.md"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/example.txt"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/tjexample.c"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/libjpeg.txt"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/structure.txt"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/usage.txt"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/wizard.txt"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/LICENSE.md"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/man/man1" TYPE FILE FILES
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/cjpeg.1"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/djpeg.1"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jpegtran.1"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/rdjpgcom.1"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/wrjpgcom.1"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/pkgscripts/libjpeg.pc"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/pkgscripts/libturbojpeg.pc"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jconfig.h"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jerror.h"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jmorecfg.h"
    "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jpeglib.h"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/simd/cmake_install.cmake")
  include("/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/md5/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
