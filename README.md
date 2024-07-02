# BreezeX Cursor

Extended KDE cursor, Highly inspired on **KDE Breeze** for `Windows` and `Linux` with _HiDPi Support_ .

[![build](https://github.com/ful1e5/BreezeX_Cursor/actions/workflows/build.yml/badge.svg)](https://github.com/ful1e5/BreezeX_Cursor/actions/workflows/build.yml)

## Notes

-   All cursor's SVG files are found in [svg](./svg) directory or you can also find them on [Figma](https://www.figma.com/design/Uo4LeHvFUPDgoqLjnFc1LB/BreezeX?node-id=2620-3&t=7QqTBQ4MOqXONrGI-1).

<!-- If you're interested, you can learn more about "sponsor-spotlight" on
 https://dev.to/ful1e5/lets-give-recognition-to-those-supporting-our-work-on-github-sponsors-b00 -->

![shoutout-sponsors](https://sponsor-spotlight.vercel.app/sponsor?login=ful1e5)

-   **2024-07-01**: [b9d526d](https://github.com/ful1e5/BreezeX_Cursor/commit/b9d526df48ac582ea80b7b6329da903f2760e046) Partitioned cursor build configuration into multiple files according to platform:
    `build.toml` -> `configs/win_lg.build.toml`, `configs/win_rg.build.toml`, `configs/win_xl.build.toml`, `configs/x.build.toml`.

---

![BreezeX Dark](https://imgur.com/zDGsq2h.png)
![BreezeX Light](https://imgur.com/tmKu1vC.png)
![BreezeX Black](https://imgur.com/kzLufkT.png)

## Cursor Sizes

### Xcursor Sizes:

<kbd>16</kbd>
<kbd>20</kbd>
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

### Windows Cursor Size:

| size | Regular (× ²⁄₃) | Large (× ⁴⁄₅) | Extra-Large (× 1) |
| ---: | --------------: | ------------: | ----------------: |
|   32 |     21.333 → 22 |     25.6 → 26 |                32 |
|   48 |              32 |     38.4 → 39 |                48 |
|   64 |     42.666 → 43 |     51.2 → 52 |                64 |
|   96 |              64 |     76.8 → 77 |                96 |
|  128 |     85.333 → 86 |   102.4 → 103 |               128 |

## Colors

### BreezeX Dark

-   Outline Color - `#FFFFFF` (White)
-   Base Color - `#4D4D4D` (Breeze)

### BreezeX Light

-   Outline Color - `#4D4D4D` (Breeze)
-   Base Color - `#FFFFFF` (White)

### BreezeX Black

-   Outline Color - `#FFFFFF` (White)
-   Base Color - `#000000` (Black)

## How to get it

### Easiest Way

You can download latest `stable` & `development` releases from
[Release Page](https://github.com/ful1e5/BreezeX_Cursor/releases).

## Installing BreezeX Cursor

#### Linux/X11

**Installation:**

```bash
tar -xvf BreezeX-Dark.tar.gz                # extract `BreezeX-Dark.tar.gz`
mv BreezeX-* ~/.icons/                      # Install to local users
sudo mv BreezeX-* /usr/share/icons/         # Install to all users
```

**Uninstallation:**

```bash
rm ~/.icons/BreezeX-*                       # Remove from local users
sudo rm /usr/share/icons/BreezeX-*          # Remove from all users
```

#### Windows

**Installation:**

1. Unzip `.zip` file
2. Open unziped directory in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open Control Panel > Personalization and Appearance > Change mouse pointers,
   and select **BreezeX Cursors**.
5. Click '**Apply**'.

**Uninstallation:**

Run the `uninstall.bat` script packed with the `.zip` archive

**OR** follow these steps:

1. Go to **Registry Editor** by typing the same in the _start search box_.
2. Expand `HKEY_CURRENT_USER` folder and expand `Control Panel` folder.
3. Go to `Cursors` folder and click on `Schemes` folder - all the available custom cursors that are
   installed will be listed here.
4. **Right Click** on the name of cursor file you want to uninstall; for eg.: _BreezeX Cursors_ and
   click `Delete`.
5. Click '**yes**' when prompted.

## Build From Source

### Prerequisites

-   Python version 3.7 or higher
-   [clickgen](https://github.com/ful1e5/clickgen)>=2.2.5 (`pip install clickgen`)
-   [yarn](https://github.com/yarnpkg/yarn)

### Quick start

1. Install [build prerequisites](#prerequisites) on your system
2. `git clone https://github.com/ful1e5/BreezeX_Cursor`
3. `cd BreezeX_Cursor`
4. `yarn install`
5. `yarn generate`
6. See [Installing BreezeX Cursor](#installing-breezex-cursor).

### Getting Started

Once you have the [build prerequisites](#prerequisites) installed, You can personalize colors,
customize sizes, change target platforms, and more. This process involves using external tools,
as this repository only contains SVG files and configuration for these tools:

-   [cbmp](https://github.com/ful1e5/cbmp): Used for customizing colors and generating PNG files.
-   [ctgen](https://github.com/ful1e5/clickgen): Used for customizing sizes and building XCursor and Windows Cursors.

You can refer to the README of each tool for more information on their command-line options.

#### Crafting Your BreezeX Cursor

The process of creating custom cursor themes involves two main steps:

1. Rendering SVG files to PNG files.
2. Building cursor themes from PNG files.

#### Customize Colors

`cbmp` provides three options for changing colors:

1. `-bc`: Base color, which replaces the `#00FF00` color in the SVG.
2. `-oc`: Outlined color, which replaces the `#0000FF` color in the SVG.
3. `-wc` (optional): Watch Background color, which replaces the `#FF0000` color in the SVG.

```bash
npx cbmp [...] -bc '<hex>' -oc '<hex>' -wc '<hex>'
```

Alternatively, you can provide a JSON configuration file to render SVG files, which contains a sequence of `cbmp` commands:

```bash
npx cbmp render.json
```

#### Customize Sizes

##### Customize Windows Cursor size

To build Windows cursor with size `16`:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/BreezeX-Dark' -n 'BreezeX-Dark' -c 'Extended Breeze XCursors with size 16'
```

You can also customize output directory with `-o` option:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/BreezeX-Dark' -o 'out' -n 'BreezeX-Dark' -c 'Extended Breeze Windows Cursors with size 16'
```

##### Customize XCursor size

To build XCursor with size `16`:

```bash
ctgen build.toml -s 16 -p x11 -d 'bitmaps/BreezeX-Dark' -n 'BreezeX-Dark' -c 'Extended Breeze XCursors with size 16'
```

You can also assign multiple sizes to `ctgen` for XCursors build:

```bash
ctgen build.toml -s 16 18 24 32 -p x11 -d 'bitmaps/BreezeX-Dark' -n 'BreezeX-Dark' -c 'Extended Breeze XCursors with multi-sizes'
```

#### Examples

Lets generate BreezeX Cursor with green and black colors:

```bash
npx cbmp -d 'svg' -o 'bitmaps/BreezeX-Hacker' -bc '#00FE00' -oc '#000000'
```

After rendering custom color you have to build cursor through `ctgen`:

```bash
ctgen build.toml -d 'bitmaps/BreezeX-Hacker' -n 'BreezeX-Hacker' -c 'Green and Black BreezeX cursors.'
```

Afterwards, Generated theme can be found in the `themes` directory.

###### BreezeX Gruvbox

```bash
npx cbmp -d 'svg/original' -o 'bitmaps/BreezeX-Gruvbox' -bc '#282828' -oc '#EBDBB2'
ctgen build.toml -d 'bitmaps/BreezeX-Gruvbox' -n 'BreezeX-Gruvbox' -c 'Groovy BreezeX cursors.'
```

###### BreezeX Solarized Dark

```bash
npx cbmp -d 'svg/original' -o 'bitmaps/BreezeX-Solarized-Dark' -bc '#002b36' -oc '#839496'
ctgen build.toml -d 'bitmaps/BreezeX-Solarized-Dark' -n 'BreezeX-Solarized-Dark' -c 'Solarized Dark BreezeX cursors.'
```

###### BreezeX Solarized Light

```bash
npx cbmp -d 'svg/original' -o 'bitmaps/BreezeX-Solarized-Light' -bc '#839496' -oc '#002b36'
ctgen build.toml -d 'bitmaps/BreezeX-Solarized-Light' -n 'BreezeX-Solarized-Light' -c 'Solarized Light BreezeX cursors.'
```

###### BreezeX Dracula

```bash
npx cbmp -d 'svg/original' -o 'bitmaas/BreezeX-Dracula' -bc '#282a36' -oc '#f8f8f2'
ctgen build.toml -d 'bitmaps/BreezeX-Dracula' -n 'BreezeX-Dracula' -c 'Dracula BreezeX cursors.'
```

## Testing Cursor

There are several websites that allow you to test your cursor states by hovering over buttons. This can be very useful when developing or verifying the behavior of a cursor. The following websites cover many of the most commonly used cursors, although they may not include all available options.

-   [Cursor-Test](https://vibhorjaiswal.github.io/Cursor-Test/)
-   [Mozilla CSS Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)

For a blueprint for creating XCursors, you may also want to refer to [Cursor-demo](https://wiki.tcl-lang.org/page/Cursor+demo).

## Bugs

Bugs should be reported [here](https://github.com/ful1e5/BreezeX_Cursor/issues) on the Github issues page.

## Getting Help

You can create a **issue**, I will help you.

## Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.
