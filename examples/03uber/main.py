import sys
from uberschema import ProductList


if __name__ == "__main__":
    try:
        d = {
            "products": [
                dict(product_id="x1", description="first", display_name="1st", capacity="4 people"),
                dict(product_id="x2", description="second", display_name="2nd", capacity="5 people", image="http://example.jp/img/notfound.jpg"),
            ]
        }
        data = ProductList().load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
