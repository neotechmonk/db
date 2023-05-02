from datetime import datetime

from products import Product


def main():
    today = datetime.today().strftime("%Y-%m-%d")

    # ?: why is everything a string. No native type compatibility?
    # Tuple is preferrable as opposed to dictionary - as DB al
    product = (
        today,
        "B- Shirts",
        "Awesome Shirts",
        "Custom logo",
        "24.99",
        "http://www.shop.com/products/custom-logo.html",
    )
    db = Product()
    db.insert(product)

    for _prod in db.read():
        print(_prod)


if __name__ == "__main__":
    main()
