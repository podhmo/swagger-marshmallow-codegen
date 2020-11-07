SRC ?= ./person.yaml
DST ?= ./person.py
OPTS ?= "--logging=DEBUG"

default:
	PYTHONPATH=. swagger-marshmallow-codegen ${OPTS} --driver=_custom.py:MyDriver ${SRC} > ${DST}
	PYTHONPATH=. python main.py
