class Product:
    """
    Класс для представления продукта.
    """

    name: str  # Название продукта.
    description: str  # Описание продукта.
    price: float  # Цена продукта.
    quantity: int  # Количество продукта на складе.

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация нового продукта.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
