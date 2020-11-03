PKG := swagger_marshmallow_codegen
SHELL := bash

test:
	pytest -vv $(PKG)

lint:
	flake8 ${PKG} --ignore=E501,E303,E203,W391,W503

format:
	black ${PKG} --exclude=dst

# TODO: typing
typing:
	:

define runT
	$(1)

endef

define findCandidatesT
$(shell find ${1} -mindepth 2 -name Makefile | xargs -n 1 -I{} dirname {} | sort -h)
endef

WHERE ?= .

examples:
	python -m pip install bson
	$(foreach x,$(call findCandidatesT $(WHERE)),$(call runT,OPTS=--logging=WARNING make --silent -C $(x)))
.PHONY: examples

# for travis
ci:
	$(foreach x,$(call findCandidatesT $(WHERE)),$(call runT,OPTS=--logging=WARNING make --silent -C $(x)))
	test -z `git diff examples/` || (echo  "*********DIFF*********" && git diff examples/ && exit 2)
.PHONY: ci

_find-candidates:
	echo $(call findCandidatesT $(WHERE))

