GREP := $(shell which ggrep || grep)

default: clean
	$(MAKE) $(shell cat Makefile | $(GREP) -P '^[0-9]+:' | tr ':' ' ')

clean:
	rm -rf petstore petstore_extend

# simple
00:
	swagger-marshmallow-codegen petstore.json -d --output petstore

# with simple relation
01:
	swagger-marshmallow-codegen petstore-extend.json -d --output petstore-extend
