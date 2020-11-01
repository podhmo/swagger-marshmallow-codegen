gen:
	python gen.py --logging=INFO \
 defs/00simple-object.py \
 defs/02nesting.py \
 defs/03self-nesting.py \

gen-candidates:
	python gen-candidates.py expected > codegen_candidates.py


.PHONY: gen

test:
	pytest -vv ../swagger_marshmallow_codegen/tests/test_codegen.py

# TODO: use symlink (even windows environment)
sync: gen gen-candidates
	rm -rf ../swagger_marshmallow_codegen/tests/v2src
	mkdir -p ../swagger_marshmallow_codegen/tests/v2src
	cp -r ./v2/* ../swagger_marshmallow_codegen/tests/v2src/
	rm -rf ../swagger_marshmallow_codegen/tests/v3src
	mkdir -p ../swagger_marshmallow_codegen/tests/v3src
	cp -r ./v3/* ../swagger_marshmallow_codegen/tests/v3src/
	rm -rf ../swagger_marshmallow_codegen/tests/v3dst
	mkdir -p ../swagger_marshmallow_codegen/tests/v3dst
	cp -r ./expected/* ../swagger_marshmallow_codegen/tests/v3dst/
	rm -rf ../swagger_marshmallow_codegen/tests/v2dst
	mkdir -p ../swagger_marshmallow_codegen/tests/v2dst
	cp -r ./expected/* ../swagger_marshmallow_codegen/tests/v2dst/
	cp codegen_candidates.py ../swagger_marshmallow_codegen/tests


.PHONY: test
