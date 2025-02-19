# 14_2_homework

from src.category import Category
from src.data_loader import export_products_to_file, load_products_from_json
from src.product import Product

if __name__ == "__main__":
    # Задание 1: Создаем продукты вручную
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию со списком продуктов.
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Задание 2: Выводим список продуктов через геттер.
    print("=" * 50)
    print("Список товаров в категории:\n" + category1.products)

    # Добавляем новый продукт через метод add_product().
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("=" * 50)
    print("Обновленный список товаров:\n" + category1.products)
    print("Общее количество товаров:", Category.product_count)

    # Задание 3: Создаем новый продукт через класс-метод new_product().
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    # Если товар уже совпадает с имеющимися, их количество складывается.
    print("=" * 50)
    print("\nДобавляем новый продукт:")
    print("Имя:", new_product.name)
    print("Описание:", new_product.description)
    print("Цена:", new_product.price)
    print("Количество:", new_product.quantity)  # Ожидается 10 шт, т.к. есть совпадение

    # Задание 4: Изменение цены нового продукта.
    print("=" * 50)
    new_product.price = 800
    print("После попытки понижения цены (если подтверждено):", new_product.price)

    new_product.price = -100
    print("При попытке установить -100, цена остается:", new_product.price)

    new_product.price = 0
    print("При попытке установить 0, цена остается:", new_product.price)
    print("=" * 50)

    # --- Работа с JSON ---
    print("\nЗагрузка данных из JSON")
    print("=" * 50)

    # Сохраняем вручную созданные категории выше в файле
    manual_categories = [category1]

    # Интерактивное управление: загрузка данных из JSON, если пользователь выбирает 'y'
    categories = []
    load_choice = input("\nЗагрузить данные из JSON? (y/n): ").strip().lower()
    if load_choice == "y":
        try:
            categories = load_products_from_json()
            print("Данные успешно загружены из JSON.")
        except FileNotFoundError:
            print("Файл JSON не найден, продолжаем без загрузки.")
    else:
        # Если пользователь ввёл 'n', выводим сообщение и используем ранее созданные данные
        print("Выводится текущая информация о товарах")
        categories = manual_categories

    print("\nТекущие категории:")
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print("Товары:\n" + category.products)

    # Экспорт данных в выбранный формат (по желанию пользователя)
    export_choice = (
        input("\nЭкспортировать данные? Введите формат (txt, xlsx, docx) или n для отмены: ").strip().lower()
    )
    if export_choice in ("txt", "xlsx", "docx"):
        export_products_to_file(categories, output_format=export_choice, base_filename="products")
        print("Данные экспортированы в файл products_." + export_choice)
    else:
        print("Экспорт отменен.")
