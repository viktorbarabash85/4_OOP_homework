from typing import Any

import pytest

from src.product import Product

# ================================
# tests 15_1_homework
# ================================


def test_product_str() -> None:
    """Тест магического метода __str__"""
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add() -> None:
    """Тест магического метода __add__"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    assert product1 + product2 == (180000.0 * 5) + (210000.0 * 8)


def test_product_add_zero() -> None:
    """Тест __add__ с пустыми остатками"""
    product1 = Product("Product A", "desc", 100.0, 0)
    product2 = Product("Product B", "desc", 200.0, 0)
    assert product1 + product2 == 0


# ================================
# tests 14_2_homework
# ================================


def test_product_creation() -> None:
    """Тест создания продукта."""
    product = Product("Ноутбук", "Описание", 50000, 10)
    assert product.name == "Ноутбук", "Имя должно быть 'Ноутбук'"
    assert product.description == "Описание", "Описание должно быть 'Описание'"
    assert product.price == 50000, "Цена должна быть 50000"
    assert product.quantity == 10, "Количество должно быть 10"


def test_set_price() -> None:
    """Тест установки новой цены при увеличении цены."""
    product = Product("Ноутбук", "Описание", 50000, 10)
    product.price = 55000
    assert product.price == 55000, "Цена должна измениться на 55000 при увеличении"


def test_set_price_negative(capsys: Any) -> None:
    """
    Тест ошибки при установке отрицательной цены.
    При попытке установить цену <= 0 должно выводиться сообщение:
    \"Цена не должна быть нулевая или отрицательная\"
    и цена оставаться прежней.
    """
    product = Product("Ноутбук", "Описание", 50000, 10)
    product.price = -1000
    captured = capsys.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in captured
    assert product.price == 50000, "Цена не должна измениться при отрицательном значении"


def test_decrease_price_with_confirmation(monkeypatch: Any) -> None:
    """
    Тест изменения цены при понижении.
    Если новая цена ниже текущей, должен запрашиваться ввод.
    При подтверждении (ввод 'y') цена обновится.
    """
    product = Product("Ноутбук", "Описание", 50000, 10)
    # Симулируем подтверждение изменения цены (ввод 'y')
    monkeypatch.setattr("builtins.input", lambda prompt: "y")
    product.price = 40000
    assert product.price == 40000, "Цена должна измениться при подтверждении понижения"


def test_decrease_price_without_confirmation(monkeypatch: Any) -> None:
    """
    Тест изменения цены при понижении.
    Если пользователь не подтверждает (ввод не 'y'), цена остается прежней.
    """
    product = Product("Ноутбук", "Описание", 50000, 10)
    # Симулируем отказ (ввод 'n')
    monkeypatch.setattr("builtins.input", lambda prompt: "n")
    product.price = 40000
    assert product.price == 50000, "Цена должна остаться прежней при отсутствии подтверждения"


def test_increase_quantity() -> None:
    """Тест увеличения количества товара."""
    product = Product("Ноутбук", "Описание", 50000, 10)
    product.increase_quantity(5)
    assert product.quantity == 15, "Количество должно стать 15 после увеличения на 5"


def test_decrease_quantity() -> None:
    """Тест уменьшения количества товара."""
    product = Product("Ноутбук", "Описание", 50000, 10)
    product.decrease_quantity(3)
    assert product.quantity == 7, "Количество должно стать 7 после уменьшения на 3"


def test_decrease_quantity_negative() -> None:
    """Тест ошибки при уменьшении количества ниже нуля."""
    product = Product("Ноутбук", "Описание", 50000, 10)
    with pytest.raises(ValueError, match="Нельзя уменьшить количество ниже нуля."):
        product.decrease_quantity(15)


def test_product_string_representation() -> None:
    """Тест строкового представления продукта."""
    product = Product("Ноутбук", "Игровой ноутбук", 50000.0, 10)
    expected = "Ноутбук, 50000.0 руб. Остаток: 10 шт."
    assert str(product) == expected


def test_product_quantity_setter() -> None:
    """Тест сеттера для количества продукта."""
    product = Product("Телефон", "Смартфон", 30000.0, 5)
    product.quantity = 10
    assert product.quantity == 10
    with pytest.raises(ValueError):
        product.quantity = -1


def test_product_increase_decrease_quantity() -> None:
    """Тест методов изменения количества продукта."""
    product = Product("Планшет", "Планшет", 20000.0, 5)
    product.increase_quantity(3)
    assert product.quantity == 8
    product.decrease_quantity(4)
    assert product.quantity == 4
    with pytest.raises(ValueError):
        product.decrease_quantity(10)


def test_product_new_product() -> None:
    """Тест метода new_product для создания или обновления продукта."""
    Product._registry.clear()
    data = {"name": "Колонка", "description": "Bluetooth колонка", "price": 5000.0, "quantity": 2}
    product1 = Product.new_product(data)
    data_update = {"name": "Колонка", "description": "Bluetooth колонка", "price": 6000.0, "quantity": 3}
    product2 = Product.new_product(data_update)
    assert product1 is product2
    assert product2.quantity == 5
    assert product2.price == 6000.0


# ================================
# tests 14_1_homework
# ================================


def test_product_initialization() -> None:
    """Тестирование корректной инициализации продукта."""
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
