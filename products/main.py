from datetime import datetime

from products import Product


def main():
    today = datetime.today().strftime("%Y-%m-%d")

    # ?: why is everything a string. No native type compatibility?
    # Tuple is preferrable as opposed to dictionary - as DB al
    product = (
        today,
        "T- Shirts",
        "Awesome Shirts",
        "Custom logo",
        "24.99",
        "http://www.shop.com/products/custom-logo.html",
    )
    db = Product()
    db.insert(product)


if __name__ == "__main__":
    main()
