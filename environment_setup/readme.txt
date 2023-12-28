================================================================
Installing Utilities and Dependencies
================================================================
Hit:1 http://ca.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:3 http://packages.microsoft.com/repos/code stable InRelease
Hit:4 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:5 https://packages.microsoft.com/repos/edge stable InRelease
Hit:6 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Hit:8 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu jammy InRelease
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
software-properties-common is already the newest version (0.99.22.8).
The following package was automatically installed and is no longer required:
  nvidia-firmware-535-535.86.05
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 55 not upgraded.
Hit:1 http://ca.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://packages.microsoft.com/repos/code stable InRelease
Hit:3 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:4 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:5 https://packages.microsoft.com/repos/edge stable InRelease
Hit:6 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Hit:8 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu jammy InRelease
Reading package lists...
PPA publishes dbgsym, you may need to include 'main/debug' component
Repository: 'deb https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu/ jammy main'
Description:
Toolchain test builds; see https://wiki.ubuntu.com/ToolChain

More info: https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test
Adding repository.
Found existing deb entry in /etc/apt/sources.list.d/ubuntu-toolchain-r-ubuntu-test-jammy.list
Adding deb entry to /etc/apt/sources.list.d/ubuntu-toolchain-r-ubuntu-test-jammy.list
Found existing deb-src entry in /etc/apt/sources.list.d/ubuntu-toolchain-r-ubuntu-test-jammy.list
Adding disabled deb-src entry to /etc/apt/sources.list.d/ubuntu-toolchain-r-ubuntu-test-jammy.list
Adding key to /etc/apt/trusted.gpg.d/ubuntu-toolchain-r-ubuntu-test.gpg with fingerprint 60C317803A41BA51845E371A1E9377A2BA9EF27F
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://packages.microsoft.com/repos/code stable InRelease
Hit:3 http://ca.archive.ubuntu.com/ubuntu jammy InRelease
Hit:4 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:5 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:6 https://packages.microsoft.com/repos/edge stable InRelease
Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Hit:8 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu jammy InRelease
Reading package lists...
Repository: 'deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/ jammy main'
Description:
This PPA contains more recent Python versions packaged for Ubuntu.

Disclaimer: there's no guarantee of timely updates in case of security problems or other issues. If you want to use them in a security-or-otherwise-critical environment (say, on a production server), you do so at your own risk.

Update Note
===========
Please use this repository instead of ppa:fkrull/deadsnakes.

Reporting Issues
================

Issues can be reported in the master issue tracker at:
https://github.com/deadsnakes/issues/issues

Supported Ubuntu and Python Versions
====================================

- Ubuntu 20.04 (focal) Python3.5 - Python3.7, Python3.9 - Python3.13
- Ubuntu 22.04 (jammy) Python3.7 - Python3.9, Python3.11 - Python3.13
- Note: Python2.7 (all), Python 3.8 (focal), Python 3.10 (jammy) are not provided by deadsnakes as upstream ubuntu provides those packages.

Why some packages aren't built:
- Note: for focal, older python versions require libssl<1.1 so they are not currently built
- Note: for jammy, older python versions requre libssl<3 so they are not currently built
- If you need these, reach out to asottile to set up a private ppa

The packages may also work on other versions of Ubuntu or Debian, but that is not tested or supported.

Packages
========

The packages provided here are loosely based on the debian upstream packages with some modifications to make them more usable as non-default pythons and on ubuntu.  As such, the packages follow debian's patterns and often do not include a full python distribution with just `apt install python#.#`.  Here is a list of packages that may be useful along with the default install:

- `python#.#-dev`: includes development headers for building C extensions
- `python#.#-venv`: provides the standard library `venv` module
- `python#.#-distutils`: provides the standard library `distutils` module
- `python#.#-lib2to3`: provides the `2to3-#.#` utility as well as the standard library `lib2to3` module
- `python#.#-gdbm`: provides the standard library `dbm.gnu` module
- `python#.#-tk`: provides the standard library `tkinter` module

Third-Party Python Modules
==========================

Python modules in the official Ubuntu repositories are packaged to work with the Python interpreters from the official repositories. Accordingly, they generally won't work with the Python interpreters from this PPA. As an exception, pure-Python modules for Python 3 will work, but any compiled extension modules won't.

To install 3rd-party Python modules, you should use the common Python packaging tools.  For an introduction into the Python packaging ecosystem and its tools, refer to the Python Packaging User Guide:
https://packaging.python.org/installing/

Sources
=======
The package sources are available at:
https://github.com/deadsnakes/

Nightly Builds
==============

For nightly builds, see ppa:deadsnakes/nightly https://launchpad.net/~deadsnakes/+archive/ubuntu/nightly
More info: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
Adding repository.
Found existing deb entry in /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding deb entry to /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Found existing deb-src entry in /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding disabled deb-src entry to /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-jammy.list
Adding key to /etc/apt/trusted.gpg.d/deadsnakes-ubuntu-ppa.gpg with fingerprint F23C5A6CF475977595C89F51BA6932366A755776
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://ca.archive.ubuntu.com/ubuntu jammy InRelease
Hit:3 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:4 http://packages.microsoft.com/repos/code stable InRelease
Hit:5 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:6 https://packages.microsoft.com/repos/edge stable InRelease
Hit:7 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
Hit:8 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu jammy InRelease
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
default-jdk is already the newest version (2:1.11-72build2).
libffi-dev is already the newest version (3.4.2-4).
python3-yaml is already the newest version (5.4.1-1ubuntu1).
valgrind is already the newest version (1:3.18.1-1ubuntu2).
codespell is already the newest version (2.1.0-1).
kcachegrind is already the newest version (4:21.12.3-0ubuntu1).
libeigen3-dev is already the newest version (3.4.0-2ubuntu2).
sshpass is already the newest version (1.09-1).
cmake is already the newest version (3.22.1-1ubuntu1.22.04.1).
curl is already the newest version (7.81.0-1ubuntu1.15).
git is already the newest version (1:2.34.1-1ubuntu1.10).
libprotobuf-dev is already the newest version (3.12.4-1ubuntu7.22.04.1).
libsqlite3-dev is already the newest version (3.37.2-2ubuntu0.1).
libssl-dev is already the newest version (3.0.2-0ubuntu1.12).
libudev-dev is already the newest version (249.11-0ubuntu3.11).
libusb-1.0-0-dev is already the newest version (2:1.0.25-1ubuntu2).
openssl is already the newest version (3.0.2-0ubuntu1.12).
python3-protobuf is already the newest version (3.12.4-1ubuntu7.22.04.1).
g++-9 is already the newest version (9.5.0-1ubuntu1~22.04).
gcc-9 is already the newest version (9.5.0-1ubuntu1~22.04).
libstdc++6-9-dbg is already the newest version (9.5.0-1ubuntu1~22.04).
protobuf-compiler is already the newest version (3.12.4-1ubuntu7.22.04.1).
python3-pip is already the newest version (22.0.2+dfsg-1ubuntu0.4).
qtbase5-dev is already the newest version (5.15.3+dfsg-2ubuntu0.2).
python3.8 is already the newest version (3.8.18-1+jammy1).
python3.8-dev is already the newest version (3.8.18-1+jammy1).
python3.8-venv is already the newest version (3.8.18-1+jammy1).
The following package was automatically installed and is no longer required:
  nvidia-firmware-535-535.86.05
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 55 not upgraded.
================================================================
Setting Up Virtual Python Environment
================================================================
Requirement already satisfied: pip in /opt/tbotspython/lib/python3.8/site-packages (23.0.1)
Collecting pip
  Using cached pip-23.3.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
      Successfully uninstalled pip-23.0.1
Successfully installed pip-23.3.2
Collecting protobuf==3.20.1 (from -r ubuntu22_requirements.txt (line 1))
  Using cached protobuf-3.20.1-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)
Collecting pyqtgraph==0.12.4 (from -r ubuntu22_requirements.txt (line 2))
  Using cached pyqtgraph-0.12.4-py3-none-any.whl (995 kB)
Collecting autoflake==1.4 (from -r ubuntu22_requirements.txt (line 3))
  Using cached autoflake-1.4-py3-none-any.whl
Collecting pyqt6==6.5.0 (from -r ubuntu22_requirements.txt (line 4))
  Using cached PyQt6-6.5.0-1-cp37-abi3-manylinux_2_28_x86_64.whl (8.0 MB)
Collecting PyQt6-WebEngine (from -r ubuntu22_requirements.txt (line 5))
  Using cached PyQt6_WebEngine-6.6.0-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (1.9 kB)
Collecting thefuzz==0.19.0 (from -r ubuntu22_requirements.txt (line 6))
  Using cached thefuzz-0.19.0-py2.py3-none-any.whl (17 kB)
Collecting iterfzf==0.5.0.20.0 (from -r ubuntu22_requirements.txt (line 7))
  Using cached iterfzf-0.5.0.20.0-py2.py3-none-manylinux1_x86_64.whl (1.2 MB)
Collecting pyqtdarktheme==1.1.0 (from -r ubuntu22_requirements.txt (line 8))
  Using cached PyQtDarkTheme-1.1.0-py3-none-any.whl (109 kB)
Collecting python-Levenshtein==0.12.2 (from -r ubuntu22_requirements.txt (line 9))
  Using cached python_Levenshtein-0.12.2-cp38-cp38-linux_x86_64.whl
Collecting psutil==5.9.0 (from -r ubuntu22_requirements.txt (line 10))
  Using cached psutil-5.9.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (283 kB)
Collecting qt-material==2.12 (from -r ubuntu22_requirements.txt (line 11))
  Using cached qt_material-2.12-py3-none-any.whl (1.7 MB)
Collecting PyOpenGL==3.1.6 (from -r ubuntu22_requirements.txt (line 12))
  Using cached PyOpenGL-3.1.6-py3-none-any.whl (2.4 MB)
Collecting numpy==1.24.4 (from -r ubuntu22_requirements.txt (line 14))
  Using cached numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.6 kB)
Collecting pyflakes>=1.1.0 (from autoflake==1.4->-r ubuntu22_requirements.txt (line 3))
  Using cached pyflakes-3.1.0-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting PyQt6-sip<14,>=13.4 (from pyqt6==6.5.0->-r ubuntu22_requirements.txt (line 4))
  Using cached PyQt6_sip-13.6.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl.metadata (503 bytes)
Collecting PyQt6-Qt6>=6.5.0 (from pyqt6==6.5.0->-r ubuntu22_requirements.txt (line 4))
  Using cached PyQt6_Qt6-6.6.1-py3-none-manylinux_2_28_x86_64.whl.metadata (534 bytes)
Requirement already satisfied: setuptools in /opt/tbotspython/lib/python3.8/site-packages (from iterfzf==0.5.0.20.0->-r ubuntu22_requirements.txt (line 7)) (56.0.0)
Collecting Jinja2 (from qt-material==2.12->-r ubuntu22_requirements.txt (line 11))
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting PyQt6-WebEngine-Qt6>=6.6.0 (from PyQt6-WebEngine->-r ubuntu22_requirements.txt (line 5))
  Using cached PyQt6_WebEngine_Qt6-6.6.1-py3-none-manylinux_2_28_x86_64.whl.metadata (574 bytes)
Collecting MarkupSafe>=2.0 (from Jinja2->qt-material==2.12->-r ubuntu22_requirements.txt (line 11))
  Using cached MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Using cached numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB)
Using cached PyQt6_WebEngine-6.6.0-cp37-abi3-manylinux_2_28_x86_64.whl (257 kB)
Using cached pyflakes-3.1.0-py2.py3-none-any.whl (62 kB)
Using cached PyQt6_Qt6-6.6.1-py3-none-manylinux_2_28_x86_64.whl (67.5 MB)
Using cached PyQt6_sip-13.6.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (298 kB)
Using cached PyQt6_WebEngine_Qt6-6.6.1-py3-none-manylinux_2_28_x86_64.whl (91.5 MB)
Using cached MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Installing collected packages: thefuzz, PyQt6-WebEngine-Qt6, PyQt6-Qt6, PyOpenGL, python-Levenshtein, pyqtdarktheme, PyQt6-sip, pyflakes, psutil, protobuf, numpy, MarkupSafe, iterfzf, pyqtgraph, pyqt6, Jinja2, autoflake, qt-material, PyQt6-WebEngine
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.3 PyOpenGL-3.1.6 PyQt6-Qt6-6.6.1 PyQt6-WebEngine-6.6.0 PyQt6-WebEngine-Qt6-6.6.1 PyQt6-sip-13.6.0 autoflake-1.4 iterfzf-0.5.0.20.0 numpy-1.24.4 protobuf-3.20.1 psutil-5.9.0 pyflakes-3.1.0 pyqt6-6.5.0 pyqtdarktheme-1.1.0 pyqtgraph-0.12.4 python-Levenshtein-0.12.2 qt-material-2.12 thefuzz-0.19.0
================================================================
Done Setting Up Virtual Python Environment
================================================================
================================================================
Fetching game controller
================================================================
================================================================
Installing Bazel
================================================================
Bazel installer
---------------

Bazel is bundled with software licensed under the GPLv2 with Classpath exception.
You can find the sources next to the installer on our release page:
   https://github.com/bazelbuild/bazel/releases

# 

## Build information
   - [Commit](https://github.com/bazelbuild/bazel/commit/41feb61)
Uncompressing.......

Bazel is now installed!

Make sure you have "/usr/bin" in your path.

For bash completion, add the following line to your ~/.bashrc:
  source /home/vhe/.bazel/bin/bazel-complete.bash

For fish shell completion, link this file into your
/root/.config/fish/completions/ directory:
  ln -s /home/vhe/.bazel/bin/bazel.fish /root/.config/fish/completions/bazel.fish

See http://bazel.build/docs/getting-started.html to start a new project!
================================================================
Done Installing Bazel
================================================================
================================================================
Setting Up PlatformIO
================================================================
# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#####################################################################################
#
# INSTALLATION
#
# Please visit > https://docs.platformio.org/en/latest/core/installation/udev-rules.html
#
#####################################################################################

#
# Boards
#

# CP210X USB UART
ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea[67][013]", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"
ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="80a9", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# FT231XS USB UART
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Prolific Technology, Inc. PL2303 Serial Port
ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# QinHeng Electronics HL-340 USB-Serial adapter
ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"
# QinHeng Electronics CH9102 USB-Serial adapter
ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d4", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Arduino boards
ATTRS{idVendor}=="2341", ATTRS{idProduct}=="[08][023]*", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"
ATTRS{idVendor}=="2a03", ATTRS{idProduct}=="[08][02]*", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Arduino SAM-BA
ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="6124", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{MTP_NO_PROBE}="1"

# Digistump boards
ATTRS{idVendor}=="16d0", ATTRS{idProduct}=="0753", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Maple with DFU
ATTRS{idVendor}=="1eaf", ATTRS{idProduct}=="000[34]", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# USBtiny
ATTRS{idProduct}=="0c9f", ATTRS{idVendor}=="1781", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# USBasp V2.0
ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05dc", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Teensy boards
ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="04[789B]?", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"
ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="04[789A]?", ENV{MTP_NO_PROBE}="1"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="04[789ABCD]?", MODE:="0666"
KERNEL=="ttyACM*", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="04[789B]?", MODE:="0666"

# TI Stellaris Launchpad
ATTRS{idVendor}=="1cbe", ATTRS{idProduct}=="00fd", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# TI MSP430 Launchpad
ATTRS{idVendor}=="0451", ATTRS{idProduct}=="f432", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# GD32V DFU Bootloader
ATTRS{idVendor}=="28e9", ATTRS{idProduct}=="0189", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# FireBeetle-ESP32
ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7522", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Wio Terminal
ATTRS{idVendor}=="2886", ATTRS{idProduct}=="[08]02d", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Raspberry Pi Pico
ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="[01]*", MODE:="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# AIR32F103
ATTRS{idVendor}=="0d28", ATTRS{idProduct}=="0204", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"


#
# Debuggers
#

# Black Magic Probe
SUBSYSTEM=="tty", ATTRS{interface}=="Black Magic GDB Server", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"
SUBSYSTEM=="tty", ATTRS{interface}=="Black Magic UART Port", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# opendous and estick
ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="204f", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Original FT232/FT245/FT2232/FT232H/FT4232
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="60[01][104]", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# DISTORTEC JTAG-lock-pick Tiny 2
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="8220", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# TUMPA, TUMPA Lite
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="8a9[89]", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# XDS100v2
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="a6d0", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Xverve Signalyzer Tool (DT-USB-ST), Signalyzer LITE (DT-USB-SLITE)
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="bca[01]", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# TI/Luminary Stellaris Evaluation Board FTDI (several)
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="bcd[9a]", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# egnite Turtelizer 2
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="bdc8", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Section5 ICEbear
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="c14[01]", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Amontec JTAGkey and JTAGkey-tiny
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="cff8", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# TI ICDI
ATTRS{idVendor}=="0451", ATTRS{idProduct}=="c32a", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# STLink probes
ATTRS{idVendor}=="0483", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Hilscher NXHX Boards
ATTRS{idVendor}=="0640", ATTRS{idProduct}=="0028", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Hitex probes
ATTRS{idVendor}=="0640", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Altera USB Blaster
ATTRS{idVendor}=="09fb", ATTRS{idProduct}=="6001", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Amontec JTAGkey-HiSpeed
ATTRS{idVendor}=="0fbb", ATTRS{idProduct}=="1000", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# SEGGER J-Link
ATTRS{idVendor}=="1366", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Raisonance RLink
ATTRS{idVendor}=="138e", ATTRS{idProduct}=="9000", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Debug Board for Neo1973
ATTRS{idVendor}=="1457", ATTRS{idProduct}=="5118", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Olimex probes
ATTRS{idVendor}=="15ba", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# USBprog with OpenOCD firmware
ATTRS{idVendor}=="1781", ATTRS{idProduct}=="0c63", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# TI/Luminary Stellaris In-Circuit Debug Interface (ICDI) Board
ATTRS{idVendor}=="1cbe", ATTRS{idProduct}=="00fd", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Marvell Sheevaplug
ATTRS{idVendor}=="9e88", ATTRS{idProduct}=="9e8f", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Keil Software, Inc. ULink
ATTRS{idVendor}=="c251", ATTRS{idProduct}=="2710", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# CMSIS-DAP compatible adapters
ATTRS{product}=="*CMSIS-DAP*", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Atmel AVR Dragon
ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2107", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"

# Espressif USB JTAG/serial debug unit
ATTRS{idVendor}=="303a", ATTR{idProduct}=="1001", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1", ENV{ID_MM_PORT_IGNORE}="1"Requirement already satisfied: platformio==6.0.2 in /usr/local/lib/python3.8/dist-packages (6.0.2)
Requirement already satisfied: requests==2.* in /usr/lib/python3/dist-packages (from platformio==6.0.2) (2.25.1)
Requirement already satisfied: uvicorn==0.17.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.17.6)
Requirement already satisfied: aiofiles==0.8.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.8.0)
Requirement already satisfied: colorama in /usr/lib/python3/dist-packages (from platformio==6.0.2) (0.4.4)
Requirement already satisfied: wsproto==1.1.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (1.1.0)
Requirement already satisfied: tabulate==0.8.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.8.10)
Requirement already satisfied: pyserial==3.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (3.5)
Requirement already satisfied: click<9,>=8.0.4 in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (8.1.7)
Requirement already satisfied: bottle==0.12.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.12.25)
Requirement already satisfied: marshmallow==3.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (3.20.1)
Requirement already satisfied: starlette==0.20.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.20.4)
Requirement already satisfied: zeroconf<1 in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.131.0)
Requirement already satisfied: semantic-version==2.10.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (2.10.0)
Requirement already satisfied: ajsonrpc==1.* in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (1.2.0)
Requirement already satisfied: pyelftools<1,>=0.27 in /usr/local/lib/python3.8/dist-packages (from platformio==6.0.2) (0.30)
Requirement already satisfied: packaging>=17.0 in /usr/local/lib/python3.8/dist-packages (from marshmallow==3.*->platformio==6.0.2) (23.2)
Requirement already satisfied: anyio<5,>=3.4.0 in /usr/local/lib/python3.8/dist-packages (from starlette==0.20.*->platformio==6.0.2) (4.2.0)
Requirement already satisfied: typing-extensions>=3.10.0 in /usr/local/lib/python3.8/dist-packages (from starlette==0.20.*->platformio==6.0.2) (4.9.0)
Requirement already satisfied: asgiref>=3.4.0 in /usr/local/lib/python3.8/dist-packages (from uvicorn==0.17.*->platformio==6.0.2) (3.7.2)
Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.8/dist-packages (from uvicorn==0.17.*->platformio==6.0.2) (0.14.0)
Requirement already satisfied: async-timeout>=3.0.0 in /usr/local/lib/python3.8/dist-packages (from zeroconf<1->platformio==6.0.2) (4.0.3)
Requirement already satisfied: ifaddr>=0.1.7 in /usr/local/lib/python3.8/dist-packages (from zeroconf<1->platformio==6.0.2) (0.2.0)
Requirement already satisfied: exceptiongroup>=1.0.2 in /usr/local/lib/python3.8/dist-packages (from anyio<5,>=3.4.0->starlette==0.20.*->platformio==6.0.2) (1.2.0)
Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.8/dist-packages (from anyio<5,>=3.4.0->starlette==0.20.*->platformio==6.0.2) (1.3.0)
Requirement already satisfied: idna>=2.8 in /usr/lib/python3/dist-packages (from anyio<5,>=3.4.0->starlette==0.20.*->platformio==6.0.2) (3.3)
================================================================
Done PlatformIO Setup
================================================================
================================================================
Done Software Setup, please reboot for changes to take place
================================================================
