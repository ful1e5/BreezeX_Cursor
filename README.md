# BreezeX Cursor

Extended KDE cursor, Highly inspired on **KDE Breeze** for `Windows` and `Linux` with _HiDPi Support_ 🎉.

[![build](https://github.com/ful1e5/BreezeX_Cursor/actions/workflows/build.yml/badge.svg)](https://github.com/ful1e5/BreezeX_Cursor/actions/workflows/build.yml)

#### Cursor Sizes

<kbd>22</kbd>
<kbd>24</kbd>
<kbd>28</kbd>
<kbd>32</kbd>
<kbd>40</kbd>
<kbd>48</kbd>
<kbd>56</kbd>
<kbd>64</kbd>
<kbd>72</kbd>
<kbd>80</kbd>
<kbd>88</kbd>
<kbd>96</kbd>

#### Colors

![#4C4C4C](https://imgur.com/oHJxr47.png)
![#FFFFFF](https://imgur.com/0Wexs1k.png)
![#000000](https://imgur.com/06jisfL.png)

### Quick install

- BreezeX Dark: [https://www.pling.com/p/1538515](https://www.pling.com/p/1538515)
- BreezeX Light: [https://www.pling.com/p/1640746](https://www.pling.com/p/1640746)
- BreezeX Black: [https://www.pling.com/p/1640747](https://www.pling.com/p/1640747)

#### Preview:

> Check Figma file [here](https://www.figma.com/file/Uo4LeHvFUPDgoqLjnFc1LB/BreezeX?node-id=0%3A1)

<p align="center">
  <img title="BreezeX Dark" src="https://imgur.com/zDGsq2h.png">
  </br>
  <sub>Dark BreezeX Cursors</sub>
</p>

<p align="center">
  <img title="BreezeX Light" src="https://imgur.com/tmKu1vC.png">
  </br>
  <sub>Light BreezeX Cursors</sub>
</p>

<p align="center">
  <img title="BreezeX Black" src="https://imgur.com/kzLufkT.png">
  </br>
  <sub>Black BreezeX Cursors</sub>
</p>

### Manual Install

#### Linux/X11

```bash
# extract `BreezeX.tar.gz`
tar -xvf BreezeX.tar.gz

# For local users
mv BreezeX-* ~/.icons/

# For all users
sudo mv BreezeX-* /usr/share/icons/
```

#### Windows

1. unzip `.zip` file
2. Open unzipped directory in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open _Control Panel > Personalization and Appearance > Change mouse pointers_, and select **BreezeX Cursors**.
5. Click '**Apply**'.

### Uninstall

#### Linux/X11

```bash
# From local users
rm -rf ~/.icons/BreezeX-*

# From all users
sudo rm -rf /usr/share/icons/BreezeX-*
```

#### Windows

1. Go to **Registry Editor** by typing the same in the _start search box_.
2. Expand `HKEY_CURRENT_USER` folder and expand `Control Panel` folder.
3. Go to `Cursors` folder and click on `Schemes` folder - all the available custom cursors that are installed will be listed here.
4. **Right Click** on the name of cursor file you want to uninstall; for eg.: \_BreezeX Cursors\_ and click `Delete`.
5. Click '**yes**' when prompted.

# Dependencies

## External Libraries

- libxcursor
- libx11
- libpng (<=1.6)

#### Install External Libraries

##### ~macOS~ **[WIP]**

```bash
brew install --cask xquartz
brew install libpng
```

##### Debain/ubuntu

```bash
sudo apt install libx11-dev libxcursor-dev libpng-dev
```

##### ArchLinux/Manjaro

```bash
sudo pacman -S libx11 libxcursor libpng
```

##### Fedora/Fedora Silverblue/CentOS/RHEL

```bash
sudo dnf install libX11-devel libXcursor-devel libpng-devel
```

## Build Dependencies

- [gcc](https://gcc.gnu.org/install/)
- [make](https://www.gnu.org/software/make/)
- [nodejs](https://nodejs.org/en/) (<=12.x.x)
- [yarn](https://classic.yarnpkg.com/en/docs/install/)
- [python](https://www.python.org/downloads/) (<=3.8)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

- [puppeteer](https://www.npmjs.com/package/puppeteer)
- [pngjs](https://www.npmjs.com/package/pngjs)
- [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

- [clickgen](https://pypi.org/project/clickgen/s)

## Build Dependencies

- [gcc](https://gcc.gnu.org/install/)
- [make](https://www.gnu.org/software/make/)
- [nodejs](https://nodejs.org/en/) (<=12.x.x)
- [yarn](https://classic.yarnpkg.com/en/docs/install/)
- [python](https://www.python.org/downloads/) (<=3.8)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

- [puppeteer](https://www.npmjs.com/package/puppeteer)
- [pngjs](https://www.npmjs.com/package/pngjs)
- [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

- [clickgen](https://pypi.org/project/clickgen/s)

## Build From Scratch

### ⚡ Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **main** and **dev** branches) and `pull request`(on **main** branch), You found theme resources in `artifact` section of **build**.GitHub **Actions** available inside [.github/workflows](https://github.com/ful1e5/BreezeX_Cursor/tree/main/.github/workflows) directory.

### Manual Build

```bash
make
```

#### Build `XCursor` theme

```bash
make unix
```

#### Customize `XCursor` size

```bash
make unix X_SIZES=22            # Only built '22px' pixel-size.
make unix X_SIZES=22 24 32      # Multiple sizes are provided with  ' '(Space)
```

#### Install `XCursor` theme

```bash
make install            # install as user
  # OR
sudo make install       # install as root
```

#### Build `Windows` theme

```bash
make windows
```

#### Customize `Windows Cursor` size

```bash
make windows WIN_SIZE=96            # Supports only one pixel-size
```

> For installation follow [these](#windows) steps.

# Bugs

Bugs should be reported [here](https://github.com/ful1e5/BreezeX_Cursor/issues) on the Github issues page.

# Getting Help

You can create a **issue**, I will help you.

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.
