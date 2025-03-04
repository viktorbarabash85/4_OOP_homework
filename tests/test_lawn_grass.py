import pytest

from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone

# ================================
# tests 16_1_homework
# ================================


def test_lawn_grass_initialization() -> None:
    """
    Тестирует корректную инициализацию объекта LawnGrass,
    проверяя как унаследованные, так и новые атрибуты.
    """
    lawn: LawnGrass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        country="Россия",
        germination_period=7,
        color="Зелёный",
    )
    assert lawn.name == "Газонная трава"
    assert lawn.description == "Элитная трава для газона"
    assert lawn.price == 500.0
    assert lawn.quantity == 20
    assert lawn.country == "Россия"
    assert lawn.germination_period == 7
    assert lawn.color == "Зелёный"
    # Строковое представление унаследовано от Product
    expected_str: str = "Газонная трава, 500.0 руб. Остаток: 20 шт."
    assert str(lawn) == expected_str


def test_lawn_grass_addition() -> None:
    """
    Тестирует сложение двух объектов LawnGrass и проверяет корректность суммарной стоимости.
    """
    lawn1: LawnGrass = LawnGrass(
        "Газонная трава 1", "Элитная трава", 500.0, 20, country="Россия", germination_period=7, color="Зелёный"
    )
    lawn2: LawnGrass = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        country="США",
        germination_period=5,
        color="Темно-зелёный",
    )
    expected: float = (500.0 * 20) + (450.0 * 15)
    assert lawn1 + lawn2 == expected


def test_lawn_grass_addition_different_type() -> None:
    """
    Проверяет, что при попытке сложения объекта LawnGrass с объектом другого типа (например, Smartphone)
    выбрасывается ошибка TypeError.
    """
    lawn: LawnGrass = LawnGrass(
        "Газонная трава", "Элитная трава", 500.0, 20, country="Россия", germination_period=7, color="Зелёный"
    )
    smartphone: Smartphone = Smartphone(
        "Iphone 15", "512GB", 210000.0, 8, efficiency=98, model="15", memory=512, color="Gray space"
    )
    with pytest.raises(TypeError):
        _ = lawn + smartphone
