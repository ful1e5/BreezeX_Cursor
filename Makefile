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

# generates binaries
BIN_DIR = ../bin
THEMES = Dark Light Black
prepare: bitmaps themes
	@rm -rf bin && mkdir bin
	@$(foreach theme,$(THEMES), mkdir -p bin/$(THEME_PREFIX)-$(theme);)
	@cd bitmaps
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)-$(theme)/bitmaps.zip $(THEME_PREFIX)-$(theme);)
	@zip -r $(BIN_DIR)/bitmaps.zip *
	@cd ..
	@cd themes
	@$(foreach theme,$(THEMES), tar -czvf $(BIN_DIR)/$(THEME_PREFIX)-$(theme)/$(THEME_PREFIX)-$(theme).tar.gz $(THEME_PREFIX)-$(theme);)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/$(THEME_PREFIX)-$(theme)/$(THEME_PREFIX)-$(theme)-Windows.zip $(THEME_PREFIX)-$(theme)-Windows;)
	@cd ..
