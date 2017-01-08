SRC ?= ./person.yaml
DST ?= ./person.py


default:
	PYTHONPATH=. swagger-marshmallow-codegen --driver=_custom.py:MyDriver --logging=DEBUG ${SRC} > ${DST}
	PYTHONPATH=. python main.py
