import sys
from uberschema import ProductList
from uberschema import Error

if __name__ == "__main__":
    try:
        d = {
            "products": [
                dict(product_id="x1", description="first", display_name="1st", capacity="4"),
                dict(
                    product_id="x2",
                    description="second",
                    display_name="2nd",
                    capacity="5",
                    image="http://example.jp/img/notfound.jpg"
                ),
            ]
        }
        data = ProductList().load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)

print("----------------------------------------")
print(Error().dump({"code": "400", "message": "bad request", "fields_": "*fields(dump to)*"}))
