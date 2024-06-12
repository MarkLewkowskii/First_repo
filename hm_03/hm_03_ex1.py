from datetime import datetime, date, timedelta
# Завдання №1
def get_days_from_today(user_date):
    try:
        return (datetime.today() - datetime.strptime(user_date, "%Y-%m-%d")).days
    except ValueError:
        new_date = input('Неправильний формат дати. Будьласька введіть дату в форматі "РРРР-ММ-ДД":')
        return get_days_from_today(new_date)
    
print (get_days_from_today(input('Будьласька введіть дату в форматі "РРРР-ММ-ДД":')))