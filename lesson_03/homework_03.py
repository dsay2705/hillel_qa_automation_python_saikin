# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
"""
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don't much care where ——" said Alice.\n'
    '"Then it doesn't matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
)
"""

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Разом Чорне та Азовське моря займають {total_area} км2.")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
first_and_second = 250449
second_and_third = 222950

first = total_goods - second_and_third
third = total_goods - first_and_second
second = total_goods - first - third

print(f"На першому складі: {first} товарів.")
print(f"На другому складі: {second} товарів.")
print(f"На третьому складі: {third} товарів.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = int(1.5 * 12)
monthly_payment = 1179
total_price = months * monthly_payment
print(f"Вартість комп'ютера: {total_price} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainders = {
    "a": 8019 % 8,
    "b": 9907 % 9,
    "c": 2789 % 5,
    "d": 7248 % 6,
    "e": 7128 % 5,
    "f": 19224 % 9
}
for key, value in remainders.items():
    print(f"{key}: {value}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
total_money = (
    4 * 274 +
    2 * 218 +
    4 * 35 +
    1 * 350 +
    3 * 21
)
print(f"Іринці знадобиться {total_money} грн для замовлення.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_page = 8
pages = photos // photos_per_page
if photos % photos_per_page != 0:
    pages += 1
print(f"Ігорю знадобиться {pages} сторінок для всіх фото.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_per_100km = 9
tank_capacity = 48
total_fuel = (distance / 100) * fuel_per_100km
refuels = total_fuel // tank_capacity
if total_fuel % tank_capacity != 0:
    refuels += 1
print(f"Для подорожі потрібно {total_fuel} літрів бензину.")
print(f"Потрібно заїхати на заправку щонайменше {refuels} рази.")