import pytest
from src.product_classes import Product, Category, Smartphone, LawnGrass, BaseProduct


class TestBaseProduct:
    def test_base_product_is_abstract(self):
        assert BaseProduct.__abstractmethods__


class TestProduct:
    def test_product_creation(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.price == 50000.0

    def test_product_is_instance_of_base(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert isinstance(product, BaseProduct)

    def test_product_price_setter_valid(self):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = 45000.0
        assert product.price == 45000.0

    def test_product_price_setter_invalid(self, capsys):
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = -100
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000.0


class TestSmartphone:
    def test_smartphone_creation(self):
        phone = Smartphone("iPhone 15", "Смартфон", 99999.0, 10,
                          "A16 Bionic", "iPhone 15 Pro", 256, "Титан")
        assert phone.model == "iPhone 15 Pro"
        assert phone.memory == 256


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        grass = LawnGrass("Газонная трава", "Для газона", 500.0, 100,
                         "Россия", 7, "Зелёный")
        assert grass.country == "Россия"
        assert grass.germination_period == 7


class TestAdd:
    def test_add_same_class(self):
        p1 = Product("Товар1", "Описание", 100.0, 10)
        p2 = Product("Товар2", "Описание", 200.0, 5)
        assert p1 + p2 == 100 * 10 + 200 * 5

    def test_add_different_classes_raises_error(self):
        phone = Smartphone("iPhone", "Смартфон", 100.0, 2,
                          "A16", "Pro", 256, "Титан")
        grass = LawnGrass("Трава", "Для газона", 50.0, 10,
                         "Россия", 7, "Зелёный")
        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            phone + grass


class TestCategory:
    def test_category_creation(self):
        category = Category("Электроника", "Электронные товары")
        assert category.name == "Электроника"

    def test_category_add_product(self):
        category = Category("Электроника", "Электронные товары")
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        category.add_product(product)
        assert len(category._Category__products) == 1

    def test_category_add_invalid_object_raises_error(self):
        category = Category("Электроника", "Электронные товары")
        with pytest.raises(TypeError, match="Можно добавлять только объекты Product"):
            category.add_product("not a product")
