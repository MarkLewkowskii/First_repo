from random import sample
# Завдання №2

def get_numbers_ticket(min, max, quantity):
    if 1 <= min < max <= 1000 and quantity in range(min, max + 1): 
        generated_numbers = sample(range(min, max + 1), quantity)
        sorted_generated_numbers = sorted(generated_numbers)
        return sorted_generated_numbers
    else:
        empty_list = []
        return empty_list

print(get_numbers_ticket(1,45,5))