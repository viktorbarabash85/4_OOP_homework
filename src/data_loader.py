import json
from pathlib import Path
from typing import List

from src.category import Category
from src.product import Product


def load_products_from_json(filepath: str = "data/products.json") -> List[Category]:
    """
    * Дополнительное задание

    Реализована подгрузка данных по категориям и товарам из файла JSON.
    Функция читает файл и создает объекты классов.
    ______
    Загружает товары и категории из JSON-файла и создает соответствующие объекты.
    """

    # Путь к файлу относительно текущего каталога
    file_path = Path(__file__).resolve().parent.parent / filepath

    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with file_path.open(encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:  # data — это список, перебираем его
        products = [
            Product(p["name"], p["description"], p["price"], p["quantity"]) for p in category_data.get("products", [])
        ]
        category = Category(category_data["name"], category_data["description"], products)
        categories.append(category)

    return categories
