gen:
	python gen.py --logging=INFO \
 defs/00simple-object.py \
 defs/02nesting.py \
 defs/03self-nesting.py \

gen-candidates:
	python gen-candidates.py expected > codegen_candidates.py
	cp codegen_candidates.py ../swagger_marshmallow_codegen/tests

.PHONY: gen

test: gen-candidates
	pytest -vv ../swagger_marshmallow_codegen/tests/test_codegen.py

.PHONY: test
