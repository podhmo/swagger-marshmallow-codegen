default: new legacy

new:
	SRC=swagger.yaml DST=schema.py $(MAKE) -f ../gen.mk -C .

legacy:
	OPTS="--legacy" SRC=swagger.yaml DST=legacy_schema.py $(MAKE) -f ../gen.mk -C .
