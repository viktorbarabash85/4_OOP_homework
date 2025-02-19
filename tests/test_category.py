from typing import Any

from src.category import Category
from src.product import Product


def test_category_initialization(sample_products: Any) -> None:
    """Тестирование корректной инициализации категории."""
    category = Category("Смартфоны", "Описание", sample_products)
    assert category.name == "Смартфоны"
    assert category.description == "Описание"
    assert len(category.products) == 3  # Проверяем, что товары добавлены в категорию


def test_category_count_increment(sample_products: Any) -> None:
    """Тестирование корректного увеличения count при создании новых категорий."""
    Category("Смартфоны", "Описание", sample_products)
    Category("Телевизоры", "Описание", [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)])

    # Проверка увеличения счетчика категорий
    assert Category.category_count == 2, f"Ожидалось количество категорий 2, но получено {Category.category_count}"


def test_category_product_count(sample_products: Any) -> None:
    """Тестирование подсчета количества товаров в категории."""
    category = Category("Смартфоны", "Описание", sample_products)
    assert category.product_count == 3, f"Ожидалось 3 товара в категории, но получено {category.product_count}"
