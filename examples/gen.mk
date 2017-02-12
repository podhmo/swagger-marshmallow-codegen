SRC ?= ./00simple/person.yaml
DST ?= ./00simple/person.py

default:
	swagger-marshmallow-codegen --full --logging=DEBUG ${SRC} > ${DST}
	python `dirname ${DST}`/main.py
