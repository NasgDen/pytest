import pytest

from src.utils import calculate_tax, calculate_taxes


@pytest.mark.parametrize("prices, tax_rate, expected", [
    ([10, 20, 30], 10, [11.0, 22.0, 33.0]),
    ([], 20, [])
])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_fixture(list_of_float):
    assert calculate_taxes(list_of_float, 10) == [2.2, 4.4, 6.6]


def test_calculate_tax_rate_raise():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([1, 2], -10)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == 'Неверный налоговый процент'


def test_calculate_price_raise():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([-1, -2], 10)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == 'Неверная цена'


# Тест calculate_tax
def test_calculate_tax_price_raise():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(-10, 10)
    assert str(exc_info.value) == "Неверная цена"


def test_calculate_tax_tax_raise():
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(10, -10)
    assert str(exc_info.value) == "Неверный налоговый процент"


@pytest.mark.parametrize("prices, tax_rate, expected", [
    (100, 10, 110),
    (50, 5, 52.5)
])
def test_calculate_tax_param(prices, tax_rate, expected):
    assert calculate_tax(prices, tax_rate) == expected
