# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# Include any dependencies generated for this target.
include CMakeFiles/simd.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/simd.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/simd.dir/flags.make

CMakeFiles/simd.dir/jsimd_none.c.o: CMakeFiles/simd.dir/flags.make
CMakeFiles/simd.dir/jsimd_none.c.o: jsimd_none.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/simd.dir/jsimd_none.c.o"
	/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=armv7-none-linux-androideabi --gcc-toolchain=/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64 --sysroot=/home/chaos/.buildozer/android/platform/android-ndk-r17c/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/simd.dir/jsimd_none.c.o   -c /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jsimd_none.c

CMakeFiles/simd.dir/jsimd_none.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/simd.dir/jsimd_none.c.i"
	/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=armv7-none-linux-androideabi --gcc-toolchain=/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64 --sysroot=/home/chaos/.buildozer/android/platform/android-ndk-r17c/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jsimd_none.c > CMakeFiles/simd.dir/jsimd_none.c.i

CMakeFiles/simd.dir/jsimd_none.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/simd.dir/jsimd_none.c.s"
	/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=armv7-none-linux-androideabi --gcc-toolchain=/home/chaos/.buildozer/android/platform/android-ndk-r17c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64 --sysroot=/home/chaos/.buildozer/android/platform/android-ndk-r17c/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/jsimd_none.c -o CMakeFiles/simd.dir/jsimd_none.c.s

CMakeFiles/simd.dir/jsimd_none.c.o.requires:

.PHONY : CMakeFiles/simd.dir/jsimd_none.c.o.requires

CMakeFiles/simd.dir/jsimd_none.c.o.provides: CMakeFiles/simd.dir/jsimd_none.c.o.requires
	$(MAKE) -f CMakeFiles/simd.dir/build.make CMakeFiles/simd.dir/jsimd_none.c.o.provides.build
.PHONY : CMakeFiles/simd.dir/jsimd_none.c.o.provides

CMakeFiles/simd.dir/jsimd_none.c.o.provides.build: CMakeFiles/simd.dir/jsimd_none.c.o


simd: CMakeFiles/simd.dir/jsimd_none.c.o
simd: CMakeFiles/simd.dir/build.make

.PHONY : simd

# Rule to build all files generated by this target.
CMakeFiles/simd.dir/build: simd

.PHONY : CMakeFiles/simd.dir/build

CMakeFiles/simd.dir/requires: CMakeFiles/simd.dir/jsimd_none.c.o.requires

.PHONY : CMakeFiles/simd.dir/requires

CMakeFiles/simd.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/simd.dir/cmake_clean.cmake
.PHONY : CMakeFiles/simd.dir/clean

CMakeFiles/simd.dir/depend:
	cd /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/CMakeFiles/simd.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/simd.dir/depend

