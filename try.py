from datetime import datetime
from dateutil.parser import parse

def get_days_from_today(date_str):
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print('Будь ласка, введіть дату у форматі "РРРР-ММ-ДД" або в іншому форматі, який може бути автоматично виправлений.')
        new_date_str = input()
        corrected_date_str = correct_date_format(new_date_str)
        return get_days_from_today(corrected_date_str)
    
    return (datetime.today() - parsed_date).days

def correct_date_format(date_str):
    try:
        # Парсимо введену дату
        parsed_date = parse(date_str, fuzzy=True)
        # Повертаємо дату у правильному форматі
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError:
        # У випадку, якщо дату не вдається парсити
        return None

# Виводимо кількість днів з введеної дати до сьогодні
input_date_str = input("Введіть дату: ")
corrected_date_str = correct_date_format(input_date_str)

if corrected_date_str:
    days = get_days_from_today(corrected_date_str)
    print(f"Кількість днів з дати {corrected_date_str} до сьогодні: {days}")
else:
    print("Неможливо виправити дату")
