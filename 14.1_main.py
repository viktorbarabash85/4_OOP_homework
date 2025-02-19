from src.category import Category
from src.data_loader import load_products_from_json
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # ========================================================
    print("=" * 50)
    print("=" * 50)
    print("=" * 50)
    # ========================================================

    # Сбрасываем существующие счетчики перед загрузкой JSON
    Category.category_count = 0
    Category.product_count = 0

    # Загрузка данных из JSON-файла
    categories = load_products_from_json("data/products.json")
    print("Загруженные категории и товары из JSON-файла:\n")

    # Вывод информации о загруженных категориях и товарах
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products)}")

        for product in category.products:
            print(f"  - {product.name}, {product.description}, {product.price} руб., {product.quantity} шт.")
        print("=" * 50)

    # Вывод общего количества категорий и товаров
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
