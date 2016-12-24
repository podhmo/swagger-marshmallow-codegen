examples:
	for i in `find ./examples -name Makefile`; do make -C `dirname $$i`; done

.PHONY: examples
