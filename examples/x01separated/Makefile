GREP := $(shell which ggrep || which grep)

default: clean
	$(MAKE) $(shell cat Makefile | $(GREP) -P '^[0-9]+:' | tr ':' ' ')

clean:
	rm -rf petstore petstore_extend

# simple
00:
	swagger-marshmallow-codegen petstore.json -d petstore

# with simple relation
01:
	swagger-marshmallow-codegen petstore-extend.json -d petstore-extend

# with mutual reference
02:
	swagger-marshmallow-codegen team-and-user.json -d team-and-user
