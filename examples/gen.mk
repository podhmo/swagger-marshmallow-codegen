SRC ?= ./00simple/person.yaml
DST ?= ./00simple/person.py
OPTS ?= --logging=DEBUG
default:
	swagger-marshmallow-codegen --strict-additional-properties --full ${OPTS} ${SRC} > ${DST}
	python `dirname ${DST}`/main.py
