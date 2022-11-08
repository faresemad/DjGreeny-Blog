import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()
import random

from faker import Faker

from products.models import Brand, Category, Product


def seedCategory(n):
    fake = Faker()
    images = [
        '1.jpeg', '2.jpeg', '3.png', '4.jpeg', '5.jpeg', '6.jpg', '7.jpg',
        '8.jpg', '9.jpg', '10.png'
    ]
    num_image = images[random.randint(0, len(images) - 1)]
    for _ in range(n):
        name = fake.word()
        image = f"categories/22/11/{num_image}"
        Category.objects.create(name=name, image=image)
    print(f"Created {n} categories")


def seedBrand(n):  #name , image , category
    fake = Faker()
    images = [
        '1.jpeg', '2.jpeg', '3.png', '4.jpeg', '5.jpeg', '6.jpg', '7.jpg',
        '8.jpg', '9.jpg', '10.png'
    ]
    for _ in range(n):
        name = fake.word()
        num_image = images[random.randint(0, len(images) - 1)]
        image = f"brands/22/11/{num_image}"
        Brand.objects.create(
            name=name,
            image=image,
            category=Category.objects.get(id=random.randint(3, 12)))
    print(f"Created {n} brands")


def seedProduct(n):
    fake = Faker()
    images = [
        '1.jpeg', '2.jpeg', '3.png', '4.jpeg', '5.jpeg', '6.jpg', '7.jpg',
        '8.jpg', '9.jpg', '10.png'
    ]
    for _ in range(n):
        name = fake.word()
        sku = random.randint(100000, 999999)
        subtitle = fake.sentence()
        description = fake.text()
        price = round(random.uniform(20.99, 99.99), 2)
        quantity = random.randint(1, 100)
        image = f"products/22/11/{images[random.randint(0, len(images) - 1)]}"
        flag = random.choice(['New', 'Sale', 'Featured'])
        Product.objects.create(
            name=name,
            sku=sku,
            subtitle=subtitle,
            description=description,
            price=price,
            quantity=quantity,
            image=image,
            flag=flag,
            brand=Brand.objects.get(id=random.randint(3, 12)),
            category=Category.objects.get(id=random.randint(3, 12)))
    print(f"Created {n} products")


# seedCategory(10)
# seedBrand(10)
# seedProduct(20)