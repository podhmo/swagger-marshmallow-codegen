default:
	SRC=github.yaml DST=githubschema.py make -f ../gen.mk -C .

fetch:
	wget https://api.apis.guru/v2/specs/github.com/v3/swagger.yaml -O github.yaml
	gsed -i "s/type: *'null'/type: object/g;" github.yaml
