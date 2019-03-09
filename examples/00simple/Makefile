default: new legacy

new:
	SRC=person.yaml DST=person.py $(MAKE) -f ../gen.mk -C .

legacy:
	OPTS="--logging=DEBUG --legacy" SRC=person.yaml DST=legacy_person.py $(MAKE) -f ../gen.mk -C .
