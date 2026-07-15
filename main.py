from src.product_classes import Product, Category, Smartphone, LawnGrass


def main() -> None:
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ С АБСТРАКТНЫМ КЛАССОМ И МИКСИНОМ")
    print("=" * 50)

    print("\n🔍 Создание объектов (логирование от LogMixin):\n")

    product = Product("Ноутбук", "Игровой ноутбук", 89999.99, 8)
    phone = Smartphone("iPhone 15", "Смартфон", 99999.0, 10,
                      "A16 Bionic", "iPhone 15 Pro", 256, "Титан")
    grass = LawnGrass("Газонная трава", "Для газона", 500.0, 100,
                     "Россия", 7, "Зелёный")

    print("\n📦 Товары:")
    print(f"  - {product}")
    print(f"  - {phone}")
    print(f"  - {grass}")

    phone2 = Smartphone("iPhone 14", "Смартфон", 79999.0, 5,
                       "A15 Bionic", "iPhone 14 Pro", 128, "Космический")
    total_cost = phone + phone2
    print(f"\n💰 Общая стоимость двух смартфонов: {total_cost} руб.")

    electronics = Category("Электроника", "Электронные товары")
    electronics.add_product(phone)
    electronics.add_product(phone2)

    print("\n📂 Категория 'Электроника':")
    print(electronics.products)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
