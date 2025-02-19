from src.category import Category
from src.category_iterator import CategoryIterator
from src.data_loader import export_products_to_file, load_products_from_json
from src.product import Product

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Выводим строковое представление каждого продукта
    print("=" * 50)
    print("Продукты:")
    print(str(product1))
    print(str(product2))
    print(str(product3))

    # Создаем категорию и передаем в неё продукты
    print("---")
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    # Выводим строковое представление категории (учитывается общее количество товаров)
    print(str(category1))

    # Выводим подробный список товаров через геттер products
    print("=" * 50)
    print(category1.products)

    # Демонстрация магического метода __add__ для сложения продуктов
    print("---")
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    print("=" * 50)

    # --- Вариант 1. Применение нового итератора для перебора товаров в категории (с участием пользователя)
    print("\n--- Перебор товаров в категории ---")

    print(
        f"\nВариант 1. Перебор товаров в категории '{category1.name}' пользователем"
        f"\n(нажмите Enter для следующего товара, 'q' для выхода): "
    )
    iterator = iter(category1)
    while True:
        command = input().strip().lower()
        if command == "q":
            break
        try:
            next_product = next(iterator)
            print(next_product, end="")
        except StopIteration as e:
            print(e)
            break

    print("=" * 50)

    # --- Вариант 2. Применение нового итератора для перебора товаров в категории (просто перебор)
    print(f"\nВариант 2. Перебор товаров в категории '{category1.name}' (просто перебор)\n")
    iterator = CategoryIterator(category1)  # Передаём объект категории
    for product in iterator:
        print(product)
    print("\nВы ознакомились со всем списком товаров в категории.")

    # --- Работа с JSON: загрузка и экспорт данных --- # 15_1_homework
    print("=" * 50)
    print("\n--- Загрузка данных из JSON ---")

    # Если пользователь не загружает JSON, используем вручную созданные данные
    manual_categories = [category1]
    categories = []

    load_choice = input("\nЗагрузить данные из JSON? (y/n): ").strip().lower()
    if load_choice == "y":
        try:
            categories = load_products_from_json()
            print("Данные успешно загружены из JSON.")
        except FileNotFoundError:
            print("Файл JSON не найден, продолжаем без загрузки.")
    else:
        print("Выводится текущая информация о товарах")
        categories = [category1]

    print("___")
    print("Текущие категории:")
    print("___")
    for cat in categories:
        print(f"Категория: {cat.name}")
        print(f"Описание: {cat.description}")
        print("Товары:\n" + cat.products)
        print("___")
        print(str(category1))

    export_choice = (
        input("\nЭкспортировать данные? Введите формат (txt, xlsx, docx) или n для отмены: ").strip().lower()
    )
    if export_choice in {"txt", "xlsx", "docx"}:
        export_products_to_file(categories, output_format=export_choice, base_filename="products")
        print("Данные экспортированы в файл products_." + export_choice)
    else:
        print("Экспорт отменен.")
