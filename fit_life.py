# Проект FitLife - MVP версия 1.0

print('Здравствуйте!')
user_name = input('Введите Ваше имя: ').capitalize()
while True:
    try:
        user_age = int(input('Введите Ваш возраст: '))
        break
    except ValueError:
        print("Некорректный ввод. Введите возраст цифрами")

user_weight = float(input('Ваш вес, кг: '))
user_height = float(input('Ваш рост (в метрах, например 1.75): '))

WATER_PER_KG = 30
MILLILITERS_TO_LITERS = 1000


def calculation_bmi(user_weight, user_height):
    """
    Рассчитывает Индекс Массы Тела

    Args:
        user_weight(float) - вес человека в килограммах
        user_height(float) - рост человека в метрах

    Returns:
        float - ИМТ
    """
    return round(user_weight / user_height ** 2, 1)


def calculation_water_needed(user_weight):
    """
    Рассчитывает Норму потребления воды в сутки, литров

    Args:
        user_weight(float) - вес человека в килограммах

    Returns:
        float - норма воды
    """
    return round(user_weight * WATER_PER_KG / MILLILITERS_TO_LITERS, 1)


bmi = calculation_bmi(user_weight, user_height)
water_needed = calculation_water_needed(user_weight)

print('-' * 70, f'Привет, {user_name}!', sep='\n')
print(
    f'Отчет по введенным данным: Возраст - {user_age}; '
    f'Вес - {user_weight} кг; '
    f'Рост - {user_height} м')
print(
    f'Твой Индекс Массы Тела - {bmi}',
    f'Рекомендуемая норма воды в сутки - {water_needed} л.',
    sep='\n', end='\n\n')
print("Расчет окончен")
