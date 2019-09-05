# integration tests (regression tests)
examples:
	$(MAKE) --silent _find-candidates | xargs -n 1 make -C || (echo "**********NG**********" && exit 1)
.PHONY: examples

test:
	python setup.py test

ci:
	$(MAKE) --silent _find-candidates | xargs -n 1 echo "OPTS=--logging=WARNING" make --silent -C | bash -x -e || (echo "**********NG**********" && exit 1)
	test -z `git diff examples/` || (echo  "*********DIFF*********" && git diff examples/ && exit 2)

WHERE ?= .
_find-candidates:
	@find ${WHERE} -mindepth 2 -name Makefile | xargs -n 1 -I{} dirname {} | sort -h

