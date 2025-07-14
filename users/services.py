import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_product(create_product):
    """Создает новый продукт (курс или урок)"""

    product_name = (
        create_product.course if create_product.course else create_product.lesson
    )
    product = stripe.Product.create(name=product_name)
    return product


def create_price(price_product, product):
    """Создает цену на новый продукт"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=price_product.payment_amount,
        product=product,
    )
    return price


def create_checkout_session(price):
    """Создает цену в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
