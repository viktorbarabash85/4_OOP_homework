from typing import Iterator, List

from src.category import Category
from src.product import Product


class CategoryIterator:
    """
    Класс-итератор для перебора товаров в категории.
    """

    category: Category  # Объект категории, которую нужно перебирать
    _products: List[Product]  # Список товаров для итерации
    _index: int  # Индекс текущего товара

    def __init__(self, category: Category) -> None:
        """
        Принимает объект категории и подготавливает итерацию по его товарам.

        :param category: Объект категории, товары которой нужно перебирать.
        """
        self._products = category.get_products_list()  # Получаем список товаров из категории
        self._index = 0  # Индекс текущего товара

    def __iter__(self) -> Iterator[Product]:
        """Возвращает самого себя как итератор."""
        return self

    def __next__(self) -> Product:
        """
        Возвращает следующий товар в категории.

        :return: Следующий объект Product.
        :raises StopIteration: Если товары закончились.
        """
        if self._index >= len(self._products):
            raise StopIteration("\nВы ознакомились со всем списком товаров в категории.")
        product = self._products[self._index]
        self._index += 1
        return product
