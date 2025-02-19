# 15_1_homework


class Product:
    """
    Класс для представления продукта.
    """

    _name: str  # Название продукта.
    _description: str  # Описание продукта.
    __price: float  # Приватное значение цены.
    _quantity: int  # Количество продукта на складе.

    _registry: dict[str, "Product"] = {}

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует новый объект Product.

        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта на складе.
        """
        self._name = name
        self._description = description
        self.__price = price
        self._quantity = quantity

        # Регистрируем продукт, если с таким именем ещё не зарегистрирован.
        if name not in Product._registry:
            Product._registry[name] = self

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта.
        Пример: "Ноутбук, 50000 руб. Остаток: 10 шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other_product: "Product") -> float:
        """
        Магический метод сложения. Возвращает общую стоимость всего количества обоих товаров.
        Суммируется произведение цены на количество для self и other_product.

        :param other_product: Другой объект Product.
        :return: Суммарная стоимость товаров.
        :raises TypeError: Если other_product не является экземпляром Product.
        """
        if not isinstance(other_product, Product):
            raise TypeError("Сложение возможно только между объектами Product.")
        return (self.price * self.quantity) + (other_product.price * other_product.quantity)

    @property
    def name(self) -> str:
        """Геттер для имени продукта."""
        return self._name

    @property
    def description(self) -> str:
        """Геттер для описания продукта."""
        return self._description

    @property
    def price(self) -> float:
        """Геттер для цены продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для цены продукта.
        Если новая цена меньше или равна нулю, выводит сообщение и не обновляет значение.
        Если новая цена ниже текущей, запрашивает подтверждение через input.

        :param new_price: Новая цена продукта.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            response = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if response.lower() != "y":
                return
        self.__price = new_price

    @property
    def quantity(self) -> int:
        """Геттер для количества продукта на складе."""
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        """
        Сеттер для количества продукта.
        Выбрасывает ValueError, если значение отрицательное.

        :param new_quantity: Новое количество продукта.
        """
        if new_quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")
        self._quantity = new_quantity

    def increase_quantity(self, amount: int) -> None:
        """
        Увеличивает количество товара на складе.

        :param amount: Положительное число для увеличения количества.
        """
        if amount < 0:
            raise ValueError("Количество для увеличения должно быть положительным.")
        self._quantity += amount

    def decrease_quantity(self, amount: int) -> None:
        """
        Уменьшает количество товара на складе.

        :param amount: Положительное число для уменьшения количества.
        :raises ValueError: Если уменьшение приводит к отрицательному количеству.
        """
        if amount < 0:
            raise ValueError("Количество для уменьшения должно быть положительным.")
        if amount > self._quantity:
            raise ValueError("Нельзя уменьшить количество ниже нуля.")
        self._quantity -= amount

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """
        Создает новый объект Product из словаря.
        Если продукт уже существует, увеличивает его количество и обновляет цену.

        :param product_data: Словарь с ключами 'name', 'description', 'price', 'quantity'.
        :return: Объект Product.
        """
        name = product_data.get("name")
        if name in cls._registry:
            prod = cls._registry[name]
            prod.quantity += product_data.get("quantity", 0)
            new_price = product_data.get("price", 0)
            if new_price > prod.price:
                prod.price = new_price
            return prod
        else:
            new_prod = cls(
                name=str(product_data.get("name")),
                description=str(product_data.get("description")),
                price=float(product_data.get("price", 0)),
                quantity=int(product_data.get("quantity", 0)),
            )
            cls._registry[name] = new_prod
            return new_prod
