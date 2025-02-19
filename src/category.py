# 14_2_homework

from typing import List

from src.product import Product


class Category:
    """
    Класс для представления категории товаров.
    """

    _name: str  # Защищенный атрибут названия категории (публичный через геттер)
    _description: str  # Защищенный атрибут описания категории (публичный через геттер)
    __products: List[Product]  # Приватный атрибут списка товаров (недоступен напрямую извне)
    category_count: int = 0  # Счетчик созданных категорий
    product_count: int = 0  # Общий счетчик товаров во всех категориях

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """
        Инициализация новой категории.
        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список объектов Product, входящих в категорию.
        """
        self._name = name
        self._description = description

        # Копируем список, чтобы не ссылаться на внешний объект
        self.__products = products[:]
        Category.category_count += 1
        Category.product_count += len(products)

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
        Геттер для приватного списка товаров.
        Возвращает строку, где каждый продукт представлен по шаблону:
        "Название продукта, X руб. Остаток: X шт.\n"
        (Это нужно для вывода пользователю в main.)
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def add_product(self, product: Product) -> None:
        """
        Добавляет объект Product в приватный список товаров __products.
        :param product: Объект Product, который необходимо добавить.
        """
        self.__products.append(product)
        Category.product_count += 1

    def get_products_list(self) -> List[Product]:
        """
        (Вспомогательный метод) Возвращает внутренний список товаров.
        Используется для сохранения в JSON или для тестирования.
        """
        return self.__products
