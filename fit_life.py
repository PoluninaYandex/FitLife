# Проект FitLife - MVP версия 1.0


# 1. Знакомство
print("Привет! Добро пожаловать в FitLife — я твой личный помощник по здоровью.")
user_name = input("Как тебя зовут? ") 
user_age = int(input(f"Приятно познакомиться, {user_name}! Сколько тебе полных лет? "))


# 2. Сбор данных
print("\nОтлично! Теперь давай посчитаем твои показатели здоровья.")
user_weight = float(input("Введи свой вес в килограммах (например, 45.9): "))
user_height = float(input("Введи свой рост в метрах (например, 1.75): "))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)


water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER
water_l_rounded = round(water_l, 1)


# 4. Вывод красивого результата
print("\nОтчет для пользователя:", user_name, f"({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l_rounded} л. в день")
print("Расчет окончен. Будьте здоровы!")
