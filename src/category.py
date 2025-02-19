from src.product import Product


class Category:
    """
    Класс для представления категории товаров.
    """

    name: str  # Название категории.
    description: str  # Описание категории.
    products: list  # Список товаров в категории.
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация нового объекта категории.
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновление атрибутов класса при добавлении новой категории и товаров
        Category.category_count += 1
        Category.product_count += len(products)
