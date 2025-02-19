from typing import Any, List

from src.category import Category
from src.product import Product

# ================================
# tests 15_1_homework
# ================================


def test_category_str(category_items: "Category") -> None:
    """Тест __str__ у Category"""
    assert str(category_items) == "Смартфоны, количество продуктов: 13 шт."


def test_category_empty_str() -> None:
    """Тест __str__ для пустой категории"""
    empty_category = Category("Ноутбуки", "Описание", [])
    assert str(empty_category) == "Ноутбуки, количество продуктов: 0 шт."


# ================================
# tests 14_2_homework
# ================================


def test_category_creation() -> None:
    """Тестирование корректной инициализации категории."""
    products = [Product("Товар1", "Описание1", 100, 5), Product("Товар2", "Описание2", 200, 10)]
    category = Category("Электроника", "Гаджеты", products)
    assert category.name == "Электроника", "Имя категории должно быть 'Электроника'"
    assert category.description == "Гаджеты", "Описание категории должно быть 'Гаджеты'"
    # Поскольку свойство products возвращает отформатированную строку, проверяем наличие имен товаров
    formatted = category.products
    assert "Товар1" in formatted and "Товар2" in formatted, "Форматированная строка должна содержать имена товаров"


def test_add_product() -> None:
    """Тестирование метода add_product для добавления продукта в категорию."""
    category = Category("Одежда", "Мужская и женская", [])
    product = Product("Футболка", "Хлопковая", 500, 20)
    category.add_product(product)
    # Используем вспомогательный метод, чтобы получить реальный список товаров, а не форматированную строку
    products_list = category.get_products_list()
    assert len(products_list) == 1, "После добавления должен быть 1 товар"
    assert products_list[0].name == "Футболка", "Имя добавленного товара должно быть 'Футболка'"


# ================================
# tests 14_1_homework
# ================================


def test_category_initialization(sample_products: List[Product]) -> None:
    """Тестирование корректной инициализации категории."""
    category = Category("Смартфоны", "Описание", sample_products)
    assert category.name == "Смартфоны"
    assert category.description == "Описание"
    # Геттер products возвращает отформатированную строку с информацией о товарах.
    # Разобъем строку по символу новой строки и отфильтруем пустые строки.
    products_str = category.products
    products_lines = [line for line in products_str.split("\n") if line.strip() != ""]
    assert len(products_lines) == 3
    print(f"Ожидается 3 товара, найдено {len(products_lines)} наименований товаров: {products_lines}")


def test_category_count_increment(sample_products: Any) -> None:
    """Тестирование корректного увеличения count при создании новых категорий."""
    Category("Смартфоны", "Описание", sample_products)
    Category("Телевизоры", "Описание", [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)])

    # Проверка увеличения счетчика категорий
    assert Category.category_count == 2
    print(f"Ожидается количество категорий 2, получено {Category.category_count}")


def test_category_product_count(sample_products: Any) -> None:
    """Тестирование подсчета количества товаров в категории."""
    category = Category("Смартфоны", "Описание", sample_products)
    assert category.product_count == 3
    print(f"Ожидается 3 товара в категории, получено {category.product_count}")
