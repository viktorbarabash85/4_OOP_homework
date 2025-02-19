# 15_1_homework

from typing import Any, List

from src.product import Product


class Category:
    """
    Класс для представления категории товаров.
    """

    _name: str  # Название категории.
    _description: str  # Описание категории.
    __products: List[Product]  # Список товаров (приватный).

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """
        Инициализирует новую категорию.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список объектов Product.
        """
        self._name = name
        self._description = description
        # Копируем список, чтобы не изменять исходный.
        self.__products = products[:]
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.

        Формат: "Название категории, количество продуктов: X шт."
        Где X – сумма количества всех товаров в категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self._name}, количество продуктов: {total_quantity} шт."

    @property
    def name(self) -> str:
        """Геттер для имени категории."""
        return self._name

    @property
    def description(self) -> str:
        """Геттер для описания категории."""
        return self._description

    @property
    def products(self) -> str:
        """
        Геттер для списка товаров в категории.

        Возвращает строку, где каждый товар представлен с помощью его __str__.
        """
        return "\n".join(str(product) for product in self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.

        :param product: Объект Product.
        """
        self.__products.append(product)
        Category.product_count += 1

    def get_products_list(self) -> List[Product]:
        """
        Возвращает внутренний список товаров.
        Используется для сохранения в JSON или тестирования.

        :return: Список объектов Product.
        """
        return self.__products

    def __iter__(self) -> Any:
        from src.category_iterator import CategoryIterator  # Ленивая загрузка (Lazy Import)

        return CategoryIterator(self)  # Передаём всю категорию, а не список
