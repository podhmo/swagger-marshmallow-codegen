gen:
	python gen.py --logging=INFO \
 defs/00simple-object.py \
 defs/02nesting.py \
 defs/03self-nesting.py \
 defs/05additionalProperties-without-properties.py \

	python gen.py --verbose --logging=INFO \
 defs/07additionalProperties-with-bool.py \


# 01,04,06 are added by hand.

gen-candidates:
	python gen-candidates.py expected > codegen_candidates.py
	cp codegen_candidates.py ../swagger_marshmallow_codegen/tests

.PHONY: gen

test: gen-candidates
	pytest -vv ../swagger_marshmallow_codegen/tests/test_codegen.py
	pytest .

.PHONY: test
