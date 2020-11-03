PKG := swagger_marshmallow_codegen

test:
	pytest -vv $(PKG)

lint:
	flake8 ${PKG} --ignore=E501,E303,E203,W391,W503

format:
	black ${PKG} --exclude=dst

# TODO: typing
typing:
	:

examples:
	python -m pip install bson
	$(MAKE) ci
.PHONY: examples

integration-test:
	$(MAKE) --silent _find-candidates | xargs -n 1 make -C || (echo "**********NG**********" && exit 1)
.PHONY: integration-test

# for travis
ci:
	$(MAKE) --silent _find-candidates | xargs -n 1 echo "OPTS=--logging=WARNING" make --silent -C | bash -x -e || (echo "**********NG**********" && exit 1)
	test -z `git diff examples/` || (echo  "*********DIFF*********" && git diff examples/ && exit 2)
.PHONY: ci

WHERE ?= .
_find-candidates:
	@find ${WHERE} -mindepth 2 -name Makefile | xargs -n 1 -I{} dirname {} | sort -h

