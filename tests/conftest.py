from typing import List

import pytest

from src.category import Category
from src.product import Product

# ================================
# tests 15_1_homework
# ================================


@pytest.fixture
def category_items() -> "Category":  # sample_category_2():
    """Создает тестовую категорию с товарами"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    return Category("Смартфоны", "Описание категории", [product1, product2])


# ================================
# tests 14_2_homework
# ================================


@pytest.fixture
def sample_category() -> "Category":
    """Создает тестовую категорию с продуктами."""
    return Category(
        "Смартфоны",
        "Категория для смартфонов",
        [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )


# ================================
# tests 14_1_homework
# ================================
@pytest.fixture(autouse=True)
def reset_category_count() -> None:
    """Сбрасывает счетчик категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products() -> List[Product]:
    """Фикстура для создания списка продуктов."""
    return [
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]
