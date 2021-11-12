all: clean render build

clean:
	@rm -rf bitmaps themes
	
render: bitmapper svg
	@cd bitmapper && $(MAKE)

build: bitmaps
	@cd builder && make build clean

.PHONY: all

unix: clean render bitmaps
	@cd builder && make build_unix clean

windows: clean render bitmaps
	@cd builder && make build_windows clean


# Installation
.ONESHELL:
SHELL:=/bin/bash
THEME_PREFIX = BreezeX

src = ./themes/$(THEME_PREFIX)-*
local := ~/.icons
local_dest := $(local)/$(THEME_PREFIX)-*

root := /usr/share/icons
root_dest := $(root)/$(THEME_PREFIX)-*

install: themes
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing '$(THEME_PREFIX)' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r $(src) $(local)/ && echo "> Installed!"
	@else
		@echo "> Installing '$(THEME_PREFIX)' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r $(src) $(root)/ && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing '$(THEME_PREFIX)' cursors from '$(local)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing '$(THEME_PREFIX)' cursors from '$(root)'..."
		@sudo rm -rf $(root_dest)
	@fi

reinstall: uninstall install
