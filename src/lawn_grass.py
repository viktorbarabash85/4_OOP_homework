from src.product import Product


class LawnGrass(Product):
    """
    Класс-наследник класса Product для категории «Трава газонная» (расширяется дополнительными свойствами).
    """
    country: str  # страна-производитель
    germination_period: int  # срок прорастания
    color: str  # производительность

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int, color: str):
        """
        Инициализирует новую категорию «Трава газонная».

        :param name: Название продукта (газонная трава).
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта на складе.

        :param country: Страна-производитель.
        :param germination_period: Срок прорастания.
        :param color: Цвет.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
