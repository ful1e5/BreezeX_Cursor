<p align="center">
    <img src="https://imgur.com/5M6xQZx.png" width="120" alt="BreezeX" />
</p>

<p align="center">
    extended KDE cursor 💙
</p>

<!-- Badges -->
<p align="center">
  <!-- First Row -->
  <a href="https://github.com/ful1e5/BreezeX_Cursor/actions">
    <img alt="GitHub Action Build" src="https://github.com/ful1e5/BreezeX_Cursor/actions/workflows/build.yml/badge.svg" width="102" />
  </a>

  <a href="https://www.codefactor.io/repository/github/ful1e5/breezex_cursor">
    <img src="https://www.codefactor.io/repository/github/ful1e5/breezex_cursor/badge" alt="CodeFactor" />
  </a>

  <!-- Second Row -->
  </br >
  <a href="https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html">
    <img alt="npm type definitions" src="https://img.shields.io/npm/types/typescript">
  </a>

  <a href="https://github.com/puppeteer/puppeteer/">
    <img alt="Puppeteer version" src="https://img.shields.io/github/package-json/dependency-version/ful1e5/BreezeX_Cursor/puppeteer?filename=bitmapper%2Fpackage.json">
  </a>

  <a href="https://github.com/ful1e5/clickgen">
    <img alt="Clickgen" src="https://img.shields.io/badge/theme%20builder-clickgen-FD0542" />
  </a>

  <!-- Second Row -->
  <br />
  <a href="https://github.com/ful1e5/BreezeX_Cursor/releases">
    <img alt="BreezeX Cursor release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/ful1e5/BreezeX_Cursor?include_prer">
  </a>

  <a href="https://github.com/ful1e5/BreezeX_Cursor/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/ful1e5/BreezeX_Cursor?color=0081FB" />
  </a>

  <!-- Third Row -->

  <br />
  <a href="https://www.pling.com/p/1538515/#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Linux-grey?logo=linux" />
  </a>

  <a href="https://www.pling.com/p/1538515/#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Windows-blue?logo=windows" />
  </a>

  <a href="https://www.python.org/">
    <img alt="License" src="https://img.shields.io/badge/-Python-yellow?logo=python" />
  </a>

 <!-- Fourth Row -->
  <br />
  <a href="https://github.com/ful1e5">
    <img alt="Made By Kaiz"  src="https://kaiz.vercel.app/api/badge" width="133" />
  </a>
</p>

---

<!-- Intro -->

# BreezeX Cursor

Extended KDE Cursor theme, Highly inspired on **KDE Breeze** for `Windows` and `Linux` with _HiDPi Support_ 🎉.

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

#### Quick install

<!-- Quick install -->

<p align="center">
  <a href="https://www.pling.com/p/1538515/#files-panel" >
    <img title="BreezeX Pling Store" width="40%" src="https://imgur.com/VxSgrWw.png">
  </a>
</p>

#### Preview:

> Check Figma file [here](https://www.figma.com/file/Uo4LeHvFUPDgoqLjnFc1LB/BreezeX?node-id=0%3A1)

<!-- Preview -->

<p align="center">
  <img title="BreezeX Dark" src="https://imgur.com/xfmjST3.png">
  </br>
  <sub>Dark BreezeX Cursors</sub>
</p>

<p align="center">
  <img title="BreezeX Light" src="https://imgur.com/3wCoRYV.png">
  </br>
  <sub>Light BreezeX Cursors</sub>
</p>

<p align="center">
  <img title="BreezeX Black" src="https://imgur.com/l75GrMa.png">
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

<!-- Build Dependencies -->

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

<!-- Bug Report -->

# Bugs

Bugs 🐛 should be reported [here](https://github.com/ful1e5/BreezeX_Cursor/issues) on the Github issues page.

<!-- Help -->

# Getting Help

You can create a **issue**, I will help you. 🙂

<!-- Contributions and Suggestion -->

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.

<!-- Support -->

## Support

Give a **★** or Follow on [GitHub](https://github.com/ful1e5),That's work as **Steroid 💉** for me. 😉

> For extra support

<a href="https://www.buymeacoffee.com/Nt7Wg4V" target="_blank">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" >
</a>

<!-- Ninja  -->

<h1 align="center">
  ( `ω´ )۶▬ι═══════ﺤ
</h1>
<p align="center">
  <sub>I'm Using Katana</sub>
</p>
