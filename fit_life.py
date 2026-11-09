# Проект FitLife - MVP версия 1.0


print("Привет! Добро пожаловать в FitLife!")

user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе полных лет? "))

# Шаг 2. Сбор параметров и расчёты
print("\nДавай посчитаем твои показатели здоровья.")

user_weight = float(input("Введи свой вес в кг (например, 61.4): "))
user_height = float(input("Введи свой рост в метрах (например, 1.75): "))

# Расчёт ИМТ
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

# Расчёт нормы воды
water_ml = user_weight * 30
water_l = water_ml / 1000
water_l_rounded = round(water_l, 1)

# Шаг 3. Вывод результата
print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l_rounded} л. в день")
print("Расчет окончен. Будьте здоровы!")
