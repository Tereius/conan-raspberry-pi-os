#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
import shutil


class RaspberryPiOsConan(ConanFile):
    name = "RaspberryPiOS"
    version = "0.0.9"
    description = "Raspberry Pi OS Cross-Toolchain"
    license = "GPL"
    url = "https://github.com/Tereius/conan-raspberry-pi-os"
    homepage = "https://github.com/tttapa/docker-arm-cross-toolchain"
    default_user = "tereius"
    default_channel = "stable"
    exports_sources = ["Toolchain-rpi-buster.cmake", "Toolchain-rpi-bullseye.cmake"]
    settings = {"os": ["Linux"]}
    options = {"os": ["buster", "bullseye"]}
    default_options = {"os": "bullseye"}
    no_copy_source = True

    def installDebPkg(self, url: str):
        tools.download(url, "pkg.deb")
        self.run("ar xv pkg.deb", output=False)
        tools.untargz("data.tar.xz")
        self.run("rm pkg.deb", output=False)
        self.run("rm debian-binary", output=False)

    def source(self):

        tools.get("https://github.com/tttapa/docker-arm-cross-toolchain/releases/download/%s/x-tools-armv6-rpi-linux-gnueabihf.tar.xz" % self.version)
        self.run("chmod -R +w " + os.path.join(self.source_folder, "x-tools"), output=False)
        tools.get("https://github.com/raspberrypi/firmware/archive/refs/heads/master.zip")

        # apt-get download --print-uris `apt-cache depends -i --recurse libegl-dev | awk '/Depends:/{print$2}' | sort | uniq` | awk '{print$1}'
        # apt-get download --print-uris `apt-cache depends -i --recurse libgles-dev | awk '/Depends:/{print$2}' | sort | uniq` | awk '{print$1}'
        debPackages = [
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libgles-dev_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libegl-dev_1.3.2-1_armhf.deb',
            #'http://archive.raspberrypi.org/debian/pool/main/g/glibc/libc6_2.31-13%2brpt2%2brpi1%2bdeb11u5_armhf.deb',
            'http://archive.raspberrypi.org/debian/pool/main/m/mesa/libegl-mesa0_20.3.5-1%2brpt5%2brpi1_armhf.deb',
            'http://archive.raspberrypi.org/debian/pool/main/m/mesa/libgbm1_20.3.5-1%2brpt5%2brpi1_armhf.deb',
            'http://archive.raspberrypi.org/debian/pool/main/m/mesa/libgl1-mesa-dri_20.3.5-1%2brpt5%2brpi1_armhf.deb',
            'http://archive.raspberrypi.org/debian/pool/main/m/mesa/libglapi-mesa_20.3.5-1%2brpt5%2brpi1_armhf.deb',
            'http://archive.raspberrypi.org/debian/pool/main/m/mesa/libglx-mesa0_20.3.5-1%2brpt5%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/e/elfutils/libelf1_0.183-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/e/expat/libexpat1_2.2.10-2%2bdeb11u5_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/g/gcc-10/gcc-10-base_10.2.1-6%2brpi1_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/g/gcc-10/libatomic1_10.2.1-6%2brpi1_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/g/gcc-10/libgcc-s1_10.2.1-6%2brpi1_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/g/gcc-10/libstdc%2b%2b6_10.2.1-6%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libb/libbsd/libbsd0_0.11.3-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libd/libdrm/libdrm2_2.4.104-1%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libd/libdrm/libdrm-amdgpu1_2.4.104-1%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libd/libdrm/libdrm-common_2.4.104-1%2brpi1_all.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libd/libdrm/libdrm-nouveau2_2.4.104-1%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libd/libdrm/libdrm-radeon1_2.4.104-1%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libe/libedit/libedit2_3.1-20191231-2_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libf/libffi/libffi7_3.3-6_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libegl1_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libegl-dev_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libgl1_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libgl-dev_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libgles1_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libgles2_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libglvnd0_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libglx0_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libg/libglvnd/libglx-dev_1.3.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libm/libmd/libmd0_1.0.3-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libp/libpthread-stubs/libpthread-stubs0-dev_0.4-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libx11/libx11-6_1.7.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libx11/libx11-data_1.7.2-1_all.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libx11/libx11-dev_1.7.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libx11/libx11-xcb1_1.7.2-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxau/libxau6_1.0.9-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxau/libxau-dev_1.0.9-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb1_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb1-dev_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-dri2-0_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-dri3-0_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-glx0_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-present0_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-shm0_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-sync1_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcb/libxcb-xfixes0_1.14-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxcrypt/libcrypt1_4.4.18-4_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxdamage/libxdamage1_1.1.5-2_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxdmcp/libxdmcp6_1.1.2-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxdmcp/libxdmcp-dev_1.1.2-3_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxext/libxext6_1.3.3-1.1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxfixes/libxfixes3_5.0.3-2_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxshmfence/libxshmfence1_1.3-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/libx/libxxf86vm/libxxf86vm1_1.1.4-1%2bb2_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/libz/libzstd/libzstd1_1.4.8%2bdfsg-2.1%2brpi1_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/l/llvm-toolchain-11/libllvm11_11.0.1-2%2brpi1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/l/lm-sensors/libsensors5_3.6.0-7_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/l/lm-sensors/libsensors-config_3.6.0-7_all.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/n/ncurses/libtinfo6_6.2%2b20201114-2_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/v/vulkan-loader/libvulkan1_1.2.162.0-1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/w/wayland/libwayland-client0_1.18.0-2%7eexp1.1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/w/wayland/libwayland-server0_1.18.0-2%7eexp1.1_armhf.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/x/xorgproto/x11proto-core-dev_2020.1-1_all.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/x/xorgproto/x11proto-dev_2020.1-1_all.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/x/xorg-sgml-doctools/xorg-sgml-doctools_1.11-1.1_all.deb',
            'http://raspbian.raspberrypi.org/raspbian/pool/main/x/xtrans/xtrans-dev_1.4.0-1_all.deb'
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/z/z3/libz3-4_4.8.10-1_armhf.deb',
            #'http://raspbian.raspberrypi.org/raspbian/pool/main/z/zlib/zlib1g_1.2.11.dfsg-2%2bdeb11u2_armhf.deb',
        ]

        for depPackage in debPackages:
            self.installDebPkg(depPackage)

    @property
    def arch(self):
        if hasattr(self, "settings_target"):
            return self.settings_target.arch
        return self.settings.arch

    @property
    def toolchainabi(self):
        return "armv6-rpi-linux-gnueabihf"

    def package(self):
        self.copy(pattern="Toolchain-rpi-%s.cmake" % self.options.os)
        self.copy(pattern="*", src="x-tools", dst="x-tools")
        if self.options.os == "buster":
            self.copy(pattern="*", src="firmware-master/opt", dst=os.path.join("x-tools", self.toolchainabi, self.toolchainabi, "sysroot", "opt"))
        elif self.options.os == "bullseye":
            self.copy(pattern="*", src="usr", dst=os.path.join("x-tools", self.toolchainabi, self.toolchainabi, "sysroot", "usr"))

    def define_tool_var(self, name, value, bin_folder):
        path = os.path.join(bin_folder, value)
        self.output.info('Creating %s environment variable: %s' % (name, path))
        return path

    def package_info(self):
        package = self.package_folder

        toolchain = os.path.join(package, 'x-tools', self.toolchainabi)

        cmake_toolchain = os.path.join(package, 'Toolchain-rpi-%s.cmake' % self.options.os)
        toolchain_bin = os.path.join(toolchain, 'bin')

        self.output.info('Creating CHOST environment variable: %s' % self.toolchainabi)
        self.buildenv_info.define("CHOST", self.toolchainabi)

        self.output.info('Appending PATH environment variable: %s' % toolchain_bin)
        self.buildenv_info.append_path("PATH", toolchain_bin)

        self.output.info('Injecting cmaketoolchain:user_toolchain: %s' % cmake_toolchain)
        self.conf_info.append("tools.cmake.cmaketoolchain:user_toolchain", cmake_toolchain)

        self.buildenv_info.define("CC", self.define_tool_var('CC', self.toolchainabi + '-gcc', toolchain_bin))
        self.buildenv_info.define("CXX", self.define_tool_var('CXX', self.toolchainabi + '-g++', toolchain_bin))
        self.buildenv_info.define("AS", self.define_tool_var('AS', self.toolchainabi + '-as', toolchain_bin))
        self.buildenv_info.define("LD", self.define_tool_var('LD', self.toolchainabi + '-ld', toolchain_bin))
        self.buildenv_info.define("AR", self.define_tool_var('AR', self.toolchainabi + '-ar', toolchain_bin))
        self.buildenv_info.define("RANLIB", self.define_tool_var('RANLIB', self.toolchainabi + '-ranlib', toolchain_bin))
        self.buildenv_info.define("STRIP", self.define_tool_var('STRIP', self.toolchainabi + '-strip', toolchain_bin))
        self.buildenv_info.define("NM", self.define_tool_var('NM', self.toolchainabi + '-nm', toolchain_bin))
        self.buildenv_info.define("ADDR2LINE", self.define_tool_var('ADDR2LINE', self.toolchainabi + '-addr2line', toolchain_bin))
        self.buildenv_info.define("OBJCOPY", self.define_tool_var('OBJCOPY', self.toolchainabi + '-objcopy', toolchain_bin))
        self.buildenv_info.define("OBJDUMP", self.define_tool_var('OBJDUMP', self.toolchainabi + '-objdump', toolchain_bin))
        self.buildenv_info.define("READELF", self.define_tool_var('READELF', self.toolchainabi + '-readelf', toolchain_bin))
        self.buildenv_info.define("ELFEDIT", self.define_tool_var('ELFEDIT', self.toolchainabi + '-elfedit', toolchain_bin))
