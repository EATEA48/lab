# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.15

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\Andrey\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\193.5662.56\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\Andrey\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\193.5662.56\bin\cmake\win\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Andrey\CLionProjects\BubbleSort

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Andrey\CLionProjects\BubbleSort\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/BubbleSort.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/BubbleSort.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/BubbleSort.dir/flags.make

CMakeFiles/BubbleSort.dir/main.c.obj: CMakeFiles/BubbleSort.dir/flags.make
CMakeFiles/BubbleSort.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Andrey\CLionProjects\BubbleSort\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/BubbleSort.dir/main.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\BubbleSort.dir\main.c.obj   -c C:\Users\Andrey\CLionProjects\BubbleSort\main.c

CMakeFiles/BubbleSort.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/BubbleSort.dir/main.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\Andrey\CLionProjects\BubbleSort\main.c > CMakeFiles\BubbleSort.dir\main.c.i

CMakeFiles/BubbleSort.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/BubbleSort.dir/main.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\Andrey\CLionProjects\BubbleSort\main.c -o CMakeFiles\BubbleSort.dir\main.c.s

# Object files for target BubbleSort
BubbleSort_OBJECTS = \
"CMakeFiles/BubbleSort.dir/main.c.obj"

# External object files for target BubbleSort
BubbleSort_EXTERNAL_OBJECTS =

BubbleSort.exe: CMakeFiles/BubbleSort.dir/main.c.obj
BubbleSort.exe: CMakeFiles/BubbleSort.dir/build.make
BubbleSort.exe: CMakeFiles/BubbleSort.dir/linklibs.rsp
BubbleSort.exe: CMakeFiles/BubbleSort.dir/objects1.rsp
BubbleSort.exe: CMakeFiles/BubbleSort.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Andrey\CLionProjects\BubbleSort\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable BubbleSort.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\BubbleSort.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/BubbleSort.dir/build: BubbleSort.exe

.PHONY : CMakeFiles/BubbleSort.dir/build

CMakeFiles/BubbleSort.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\BubbleSort.dir\cmake_clean.cmake
.PHONY : CMakeFiles/BubbleSort.dir/clean

CMakeFiles/BubbleSort.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Andrey\CLionProjects\BubbleSort C:\Users\Andrey\CLionProjects\BubbleSort C:\Users\Andrey\CLionProjects\BubbleSort\cmake-build-debug C:\Users\Andrey\CLionProjects\BubbleSort\cmake-build-debug C:\Users\Andrey\CLionProjects\BubbleSort\cmake-build-debug\CMakeFiles\BubbleSort.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/BubbleSort.dir/depend

