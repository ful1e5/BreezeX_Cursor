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

src = ./themes/BreezeX-*
local := ~/.icons
local_dest := $(local)/BreezeX-*

root := /usr/share/icons
root_dest := $(root)/BreezeX-*

install: themes
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing 'BreezeX' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r $(src) $(local)/ && echo "> Installed!"
	@else
		@echo "> Installing 'BreezeX' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r $(src) $(root)/ && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing 'BreezeX' cursors from '$(local)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing 'BreezeX' cursors from '$(root)'..."
		@sudo rm -rf $(root_dest)
	@fi

reinstall: uninstall install
