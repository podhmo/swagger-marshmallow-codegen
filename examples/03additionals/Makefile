default: new legacy

new:
	SRC=score.yaml DST=score.py $(MAKE) -f ../gen.mk -C .

legacy:
	OPTS="--logging=DEBUG --legacy" SRC=score.yaml DST=legacy_score.py $(MAKE) -f ../gen.mk -C .
