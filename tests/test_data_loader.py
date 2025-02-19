import os
from pathlib import Path

import pytest

from src.data_loader import load_products_from_json


# Тест на успешную загрузку данных
def test_load_products_from_json() -> None:
    # Проверим рабочую директорию
    print(f"Текущая рабочая директория: {os.getcwd()}")

    categories = load_products_from_json()

    assert len(categories) > 0, "Должна быть хотя бы одна загруженная категория"
    assert all(isinstance(cat.name, str) for cat in categories), "Название категории должно быть строкой"


# Тест на отсутствие файла
def test_file_not_found() -> None:
    # Путь к несуществующему файлу
    nonexistent_filepath = Path(__file__).resolve().parent.parent / "data/nonexistent_file.json"

    # Проверяем, что выбрасывается исключение FileNotFoundError
    with pytest.raises(FileNotFoundError):
        load_products_from_json(str(nonexistent_filepath))


# Тест на пустой файл JSON (пустой список)
def test_empty_json() -> None:
    # Создаем временный пустой JSON файл
    empty_json_path = Path(__file__).resolve().parent.parent / "data/empty_products.json"

    # Запишем пустой список в файл
    with open(empty_json_path, "w", encoding="utf-8") as file:
        file.write("[]")

    # Загружаем данные
    categories = load_products_from_json(str(empty_json_path))

    # Проверяем, что категорий нет
    assert len(categories) == 0, "Категории не должны быть загружены из пустого файла"

    # Удаляем временный файл после теста
    os.remove(empty_json_path)
