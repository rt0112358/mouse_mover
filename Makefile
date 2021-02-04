#!/bin/bash
###################################################
# Makefile
# 
# Setup for pushing updates via git 
# 
# Usage for make push:
#	$ make push msg="commit message"
###################################################
all:
	@echo "Git Makefile\n"
	git status
	@echo
	@echo To push to Github:
	@echo '    make push msg="enter git commit message"'
	@echo

push:
	@githome 
	@git status
	@git add .
	git commit -m "$(msg)"
	@git status
	@git push
