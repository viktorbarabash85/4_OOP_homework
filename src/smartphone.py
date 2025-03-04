from src.product import Product


class Smartphone(Product):
    """
    Класс-наследник класса Product для категории «Смартфон» (расширяется дополнительными свойствами).
    """
    efficiency: int  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: int, model: str, memory: int, color: str) -> None:
        """
        Инициализирует новую категорию «Смартфон».

        :param name: Название смартфона.
        :param description: Описание смартфона.
        :param price: Цена смартфона.
        :param quantity: Количество смартфонов на складе.

        :param efficiency: Производительность смартфона.
        :param model: Модель смартфона.
        :param memory: Объем встроенной памяти.
        :param color : Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
