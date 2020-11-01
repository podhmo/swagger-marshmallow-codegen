# memo

- try.py generates marshmallow schema's from v2 openapi.json
- gen.py generates v2,v3 openapi.json from python class (POPO)


## before tests

Need `make sync`.

```console
# copy files to swagger_marshmallow_codegen.tests
$ make sync
```

## examples

```console
$ tree
.
├── defs # POPO (plain old python object)
│   ├── 00simple-object.py
│   └── 01simple-primitive.py
├── expected # marshmallow schema
│   └── 00simple-object.py
├── v2 # v2 openapi.json
│   ├── 00simple-object.json
│   └── 01simple-primitive.json
└── v3 # v3 openapi.json
    ├── 00simple-object.json
    └── 01simple-primitive.json
```

## try.py

```console
$ python try.py v2/01simple-primitive.json
```

## gen.py

```console
$ python gen.py defs/00simple-object.py
```
