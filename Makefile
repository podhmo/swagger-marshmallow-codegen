lint:
	flake8 --ignore=E501 --exclude=dst/ swagger_marshmallow_codegen

examples:
	for i in `find ./examples -name Makefile`; do make -C `dirname $$i`; done

.PHONY: examples
