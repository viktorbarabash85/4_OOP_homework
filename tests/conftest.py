from typing import List

import pytest

from src.category import Category
from src.product import Product


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


@pytest.fixture
def sample_category() -> "Category":
    """Создает тестовую категорию с продуктами."""
    return Category(
        "Смартфоны",
        "Категория для смартфонов",
        [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )
