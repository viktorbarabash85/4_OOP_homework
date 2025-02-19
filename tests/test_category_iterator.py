import pytest

from src.category import Category
from src.category_iterator import CategoryIterator

# ================================
# tests 15_1_homework
# ================================


def test_category_iterator(category_items: Category) -> None:
    """Тест итерации по товарам категории через CategoryIterator."""
    # Создаем итератор, передавая объект категории
    iterator = CategoryIterator(category_items)

    # Получаем список товаров через публичный метод, чтобы сравнивать объекты
    products_list = category_items.get_products_list()

    # Первый вызов итератора должен вернуть первый товар
    first_product = next(iterator)
    # Второй вызов – второй товар
    second_product = next(iterator)

    assert first_product is products_list[0]
    assert second_product is products_list[1]

    # После двух вызовов итератора должно быть вызвано StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_empty_category_iterator() -> None:
    """Тест итерации по пустой категории"""
    empty_category = Category("Ноутбуки", "Описание", [])
    iterator = iter(CategoryIterator(empty_category))
    with pytest.raises(StopIteration):
        next(iterator)
