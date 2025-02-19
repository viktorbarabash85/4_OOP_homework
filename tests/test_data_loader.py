import json
import os
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pytest

from src.category import Category
from src.data_loader import export_products_to_file, load_products_from_json, save_products_to_json
from src.product import Product

# ================================
# tests 14_2_homework
# ================================


def test_load_products_from_json_success() -> None:
    """
    Тест на успешную загрузку данных из JSON-файла.
    Ожидается, что будет загружено хотя бы 1 категория.
    """
    categories = load_products_from_json()
    assert len(categories) > 0, "Должна быть хотя бы одна загруженная категория."


def test_load_products_from_json_file_not_found() -> None:
    """
    Тест на отсутствие файла JSON.
    Ожидается, что функция выбросит FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        load_products_from_json("data/nonexistent.json")


def test_load_products_from_json_2(tmp_path: Any) -> None:
    """Тест загрузки продуктов из JSON из временного файла."""
    test_data = {
        "categories": [
            {
                "name": "Смартфоны",
                "description": "Категория для смартфонов",
                "products": [
                    {"name": "iPhone 13", "description": "128GB, Черный", "price": 80000, "quantity": 5},
                    {"name": "Samsung S21", "description": "256GB, Серый", "price": 70000, "quantity": 3},
                ],
            }
        ]
    }
    test_file = tmp_path / "test_products.json"
    test_file.write_text(json.dumps(test_data, ensure_ascii=False, indent=4), encoding="utf-8")
    categories = load_products_from_json(str(test_file))
    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    # Геттер products возвращает строку, проверяем наличие имени продукта
    assert "iPhone 13" in categories[0].products


def test_load_products_from_json_valid(mocker: Any) -> None:
    """Тест корректной загрузки JSON-файла с мокированием."""
    data = {
        "categories": [
            {
                "name": "Смартфоны",
                "description": "Категория для смартфонов",
                "products": [
                    {
                        "name": "Samsung Galaxy S23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    }
                ],
            }
        ]
    }
    # Патчим Path.exists, чтобы вернуть True для любого пути
    mocker.patch("pathlib.Path.exists", return_value=True)
    # Патчим метод open() для класса Path; read_data должен быть корректным JSON
    mock_open = mocker.mock_open(read_data=json.dumps(data))
    mocker.patch("pathlib.Path.open", mock_open)

    categories = load_products_from_json("mock.json")
    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    # Геттер products возвращает строку, проверяем, что имя продукта встречается в ней
    assert "Samsung Galaxy S23 Ultra" in categories[0].products


def test_load_products_from_empty_json(tmp_path: Any) -> None:
    """
    Тест на загрузку из пустого JSON-файла.
    Ожидается, что функция вернет пустой список категорий.
    """
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("[]", encoding="utf-8")
    categories = load_products_from_json(str(empty_file))
    assert len(categories) == 0, "При загрузке пустого JSON список категорий должен быть пустым."


def test_save_and_load_products_from_json(tmp_path: Any) -> None:
    """Тест сохранения и загрузки JSON."""
    file_path = tmp_path / "test_products.json"

    product1 = Product("Тестовый товар", "Описание", 100.0, 10)
    category = Category("Тестовая категория", "Описание", [product1])

    save_products_to_json([category], str(file_path))
    loaded_categories = load_products_from_json(str(file_path))

    assert len(loaded_categories) == 1, "Должна быть загружена 1 категория."
    assert loaded_categories[0].name == "Тестовая категория", "Неверное имя категории."
    # Используем вспомогательный метод для получения списка товаров:
    products_list = loaded_categories[0].get_products_list()
    assert len(products_list) == 1, "Должен быть 1 товар в категории."
    assert products_list[0].name == "Тестовый товар", "Неверное имя товара."
    # Очистка временного файла:
    os.remove(str(file_path))


def test_export_products_to_txt(mocker: MagicMock) -> None:
    """Тест экспорта данных в TXT-файл с моком файловой системы."""
    category = Category(
        "Смартфоны",
        "Категория для смартфонов",
        [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )
    # Патчим создание директории через метод mkdir() у Path
    mkdir_patch = mocker.patch("pathlib.Path.mkdir")
    # Патчим метод open() для экземпляров Path
    open_patch = mocker.patch("pathlib.Path.open", mocker.mock_open())
    export_products_to_file([category], "txt", "test_products")
    # Проверяем, что создана директория
    mkdir_patch.assert_called_once_with(exist_ok=True)
    # Проверяем, что файл открыт для записи с нужными параметрами
    open_patch.assert_called_once_with("w", encoding="utf-8")


def test_export_products_to_docx(mocker: MagicMock) -> None:
    """Тест экспорта данных в DOCX-файл с моком docx."""
    category = Category(
        "Смартфоны",
        "Категория для смартфонов",
        [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )
    mkdir_patch = mocker.patch("pathlib.Path.mkdir")
    doc_mock = mocker.patch("docx.Document", return_value=mocker.MagicMock())
    save_patch = mocker.patch.object(doc_mock.return_value, "save")

    export_products_to_file([category], "docx", "test_products")

    base_dir = Path(__file__).resolve().parent.parent / "data"
    expected_file = base_dir / "test_products_.docx"  # Ожидаем объект Path
    mkdir_patch.assert_called_once_with(exist_ok=True)
    save_patch.assert_called_once_with(expected_file)


# ================================
# tests 14_1_homework
# ================================


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
