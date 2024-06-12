from datetime import datetime, date, timedelta
from random import sample
import re
# Завдання №1
def get_days_from_today(user_date):
    try:
        return (datetime.today() - datetime.strptime(user_date, "%Y-%m-%d")).days
    except ValueError:
        new_date = input('Неправильний формат дати. Будьласька введіть дату в форматі "РРРР-ММ-ДД":')
        return get_days_from_today(new_date)
    
print (get_days_from_today(input('Будьласька введіть дату в форматі "РРРР-ММ-ДД":')))

# Завдання №2

def get_numbers_ticket(min, max, quantity):
    if 1 <= min < max <= 1000 and quantity in range(min, max + 1): 
        generated_numbers = sample(range(min, max + 1), quantity)
        sorted_generated_numbers = sorted(generated_numbers)
        return sorted_generated_numbers
    else:
        empty_list = []
        return empty_list

print(get_numbers_ticket(1,10,2))

# Завдання №3

def normalize_phone(phone_number):
    #phone_cleaned = re.sub(r'\D','', phone_number)
    phone_cleaned = re.sub(r'[^\d+]', '', phone_number)
    if phone_cleaned.startswith('0'):
        total_number = '+38' + phone_cleaned
    elif phone_cleaned.startswith('38') and len(phone_cleaned) == 12:
        total_number = '+' + phone_cleaned
    elif len(phone_cleaned) == 9:
        total_number = '+380' + phone_cleaned  
    else: 
        total_number = phone_cleaned
    return total_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+48- 12 .//3456789"
]

sanitized_numbers = list(map(normalize_phone, raw_numbers))
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
