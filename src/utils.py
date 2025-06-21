def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float, discount: float = 0, rounding: int = 2) -> float | None:
    """Функция вычисляет стоимость товаров с учётом налога, скидки и округляет до заданной точности"""
    if (
        isinstance(price, (float, int))
        and isinstance(tax_rate, (float, int))
        and isinstance(discount, (float, int))
        and isinstance(rounding, (float, int))
    ):
        if price <= 0:
            raise ValueError("Неверная цена")
        if tax_rate < 0 or tax_rate > 100:
            raise ValueError("Неверный налоговый процент")
        price_tax = price * tax_rate / 100 + price
        discount_price = price_tax * discount / 100
        return round(price_tax - discount_price, rounding)
    else:
        raise TypeError("Неправильный тип данных")
