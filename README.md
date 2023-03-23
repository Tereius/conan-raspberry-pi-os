# conan-raspberry-pi-os

| os    | os_build | Status                                                                                                                                                                                                                                                                                                                           |
| ----- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux | Linux    | [![Build Status](https://dev.azure.com/bjoernstresing/bjoernstresing/_apis/build/status/Tereius.conan-raspberry-pi-os?repoName=Tereius%2Fconan-raspberry-pi-os&branchName=master)](https://dev.azure.com/bjoernstresing/bjoernstresing/_build/latest?definitionId=24&repoName=Tereius%2Fconan-raspberry-pi-os&branchName=master) |

### A conan package that provides a recent cross compiler and a minimal sysroot for Raspberry Pi OS buster and bullseye

| option | values                 | default    |
| ------ | ---------------------- | ---------- |
| os     | ["buster", "bullseye"] | "bullseye" |

Raspberry Pi OS **buster** provides the proprietary Broadcom EGL and GLES implementations

Raspberry Pi OS **bullseye** provides the oss mesa EGL and GLES implementations
