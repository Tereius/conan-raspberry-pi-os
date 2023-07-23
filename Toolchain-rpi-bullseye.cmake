set(TOOLCHAIN_ROOT "${CMAKE_CURRENT_LIST_DIR}/x-tools/armv6-rpi-linux-gnueabihf")
set(SYSROOT_PATH "${TOOLCHAIN_ROOT}/armv6-rpi-linux-gnueabihf/sysroot")

# Cross-compilation system information
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)

# The sysroot contains all the libraries we might need to link against and 
# possibly headers we need for compilation
set(CMAKE_SYSROOT ${SYSROOT_PATH})
set(CMAKE_FIND_ROOT_PATH ${CMAKE_SYSROOT})
set(CMAKE_LIBRARY_ARCHITECTURE "arm-linux-gnueabihf")
#set(CMAKE_STAGING_PREFIX $ENV{HOME}/RPi-dev/staging-armv6-rpi)

# Set the compilers for C, C++ and Fortran
set(RPI_GCC_TRIPLE "armv6-rpi-linux-gnueabihf")
set(CMAKE_C_COMPILER ${RPI_GCC_TRIPLE}-gcc CACHE FILEPATH "C compiler")
set(CMAKE_CXX_COMPILER ${RPI_GCC_TRIPLE}-g++ CACHE FILEPATH "C++ compiler")
set(CMAKE_Fortran_COMPILER ${RPI_GCC_TRIPLE}-gfortran CACHE FILEPATH "Fortran compiler")

# Set the architecture-specific compiler flags
set(ARCH_FLAGS "-mcpu=arm1176jzf-s")
set(CMAKE_C_FLAGS_INIT ${ARCH_FLAGS})
set(CMAKE_CXX_FLAGS_INIT ${ARCH_FLAGS})
set(CMAKE_Fortran_FLAGS_INIT ${ARCH_FLAGS})

set(CMAKE_SHARED_LINKER_FLAGS "${COMMON_FLAGS} ${CMAKE_SHARED_LINKER_FLAGS}" )
set(CMAKE_MODULE_LINKER_FLAGS "${COMMON_FLAGS} ${CMAKE_MODULE_LINKER_FLAGS}" )
set(CMAKE_EXE_LINKER_FLAGS    "${COMMON_FLAGS} ${CMAKE_EXE_LINKER_FLAGS}" )

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

set(QT_HOST_PATH "$ENV{QT_HOST_PATH}" CACHE PATH "Set QT_HOST_PATH")

install(FILES "${SYSROOT_PATH}/lib/libstdc++.so.6.0.30" "${SYSROOT_PATH}/lib/libstdc++.so.6" "${SYSROOT_PATH}/lib/libstdc++.so" DESTINATION "lib")
