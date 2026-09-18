# Проект FitLife - MVP версия 1.0
# 1.Нормальная ли практика использовать многократно print?
# 2.И то, что используются очень похожие циклы While?

WATER_PER_KG = 30
MILLILITERS_TO_LITERS = 1000

print('Здравствуйте!')
user_name = ''.join(input('Введите Ваше имя: ').split()).capitalize()
while True:
    try:
        user_age = int(input('Введите Ваш возраст: '))
        break
    except ValueError:
        print("Некорректный ввод. Введите возраст цифрами")

while True:
    try:
        user_weight = float(input('Ваш вес, кг: '))
        break
    except ValueError:
        print("Некорректный ввод. Введите вес цифрами, через точку")

while True:
    try:
        user_height = float(input('Ваш рост (в метрах, например 1.75): '))
        break
    except ValueError:
        print("Некорректный ввод. Введите рост цифрами, через точку")


def calculation_bmi(user_weight, user_height):
    """Рассчет Индекса Массы Тела"""
    return round(user_weight / (user_height ** 2), 1)


def calculation_water_needed(user_weight):
    """Рассчет Нормы потребления воды в сутки, литров"""
    return round(user_weight * WATER_PER_KG / MILLILITERS_TO_LITERS, 3)


bmi = calculation_bmi(user_weight, user_height)
water_needed = calculation_water_needed(user_weight)

print('-' * 70, f'Привет, {user_name}!', sep='\n')
print(
    f'Отчет по введенным данным: Возраст - {user_age}; '
    f'Вес - {user_weight} кг; '
    f'Рост - {user_height} м')
print(f'Твой Индекс Массы Тела - {bmi}')
print(f'Рекомендуемая норма воды в сутки - {water_needed} л.')
print("Расчет окончен")
