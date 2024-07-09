# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Changes

-   Updated build from source commands using new build configs path

## [v2.0.1] - 02 July 2024

### :warning: Changes for Developers/Package Distributors

-   The 'bitmaps' directory has been removed from the git repository. You can now generate the PNG files using `yarn render` or download them from the release assets.

-   The `build.toml` file has been removed. Instead, the cursor build configurations are now distributed according to platforms within the `configs` directory:
    -   `configs/x.build.toml`: Used to build XCursor.
    -   `configs/win_rg.build.toml`: Used to build regular size Windows cursors.
    -   `configs/win_lg.build.toml`: Used to build large size Windows cursors.
    -   `configs/win_xxl.build.toml`: Used to build extra large size Windows cursors.

### What's New?

-   Support `256px` cursors
-   feat: Added `Person` and `Pin` cursors for Windows
-   Official Distributing `16` and `20` XCursors #24
-   Multi Resolution Windows Cursors #18
-   Attach version meta-data inside cursor packages
-   Using [cbmp v1.1.1](https://github.com/ful1e5/cbmp/tree/v1.1.1) for rendering cursor bitmaps.

### Changes

-   build script renamed (`release.sh` -> `build.sh`)
-   Use 'xz' for better compression in `build.sh` script
-   De-framed animated cursors to static SVG files

## [v2.0.0] - 14 October 2021

### What's New?

-   ci: support `clickgen v2` build with cross platform test
-   Uninstall docs ful1e5/apple_cursor#79 ful1e5/apple_cursor#80
-   Add cursor top_left_arrow #10 #11
-   Refactor: build with `clickgen v2` #21

### Issue Fixes

-   Human readable docs #16
-   fixed #21
-   fixed #17

## [v1.0.3] - 13 November 2021

### Added

-   upload `BreezeX-Black` artifacts in `build` GitHub Action
-   `prepare` command added inside `Makefile`
-   distributed pling products docs inside `pling` directory
-   `Makefile` command with `THEME_PREFIX` variable

### Changed

-   minimal `README.md` (removed badges and emojis)
-   bitmapping log more descriptive
-   builder module renamed to `src`
-   sponsor with liberapay

## [v1.0.2] - 20 June 2021

### Added

-   **BreezeX-Black** variant added

### Changed

-   `text` & `vertical-text` cursors scale down
-   Windows resize cursors scale down
-   Bigger hotspot dot for Resize cursors

## [v1.0.1] - 16 June 2021

### Changed

-   Cursors preview updated
-   `left_ptr_watch` and `wait` got minimal design

## [v1.0.0] - 14 June 2021

### Added

-   CI/CD Pipelines
-   Logo and badges
-   Initial release 🎊

[unreleased]: https://github.com/ful1e5/BreezeX_Cursor/compare/v2.0.1...main
[v2.0.1]: https://github.com/ful1e5/BreezeX_Cursor/compare/v2.0.0...v2.0.1
[v2.0.0]: https://github.com/ful1e5/BreezeX_Cursor/compare/v1.0.3...v2.0.0
[v1.0.3]: https://github.com/ful1e5/BreezeX_Cursor/compare/v1.0.2...v1.0.3
[v1.0.2]: https://github.com/ful1e5/BreezeX_Cursor/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/ful1e5/BreezeX_Cursor/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/ful1e5/BreezeX_Cursor/tree/v1.0.0
