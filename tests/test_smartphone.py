import pytest

from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone

# ================================
# tests 16_1_homework
# ================================


def test_smartphone_initialization() -> None:
    """
    Тестирует корректную инициализацию объекта Smartphone,
    проверяя как унаследованные, так и новые атрибуты.
    """
    smartphone: Smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        efficiency=95,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"
    # Строковое представление унаследовано от Product
    expected_str: str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(smartphone) == expected_str


def test_smartphone_addition() -> None:
    """
    Тестирует сложение двух объектов Smartphone и проверяет корректность вычисления суммарной стоимости.
    """
    smartphone1: Smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5, efficiency=95, model="S23 Ultra", memory=256, color="Серый"
    )
    smartphone2: Smartphone = Smartphone(
        "Iphone 15", "512GB", 210000.0, 8, efficiency=98, model="15", memory=512, color="Gray space"
    )
    expected: float = (180000.0 * 5) + (210000.0 * 8)
    assert smartphone1 + smartphone2 == expected


def test_smartphone_addition_different_type() -> None:
    """
    Проверяет, что при попытке сложения объекта Smartphone с объектом другого типа (например, LawnGrass)
    выбрасывается ошибка TypeError.
    """
    smartphone: Smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5, efficiency=95, model="S23 Ultra", memory=256, color="Серый"
    )
    lawn: LawnGrass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        country="Россия",
        germination_period=7,
        color="Зелёный",
    )
    with pytest.raises(TypeError):
        _ = smartphone + lawn
