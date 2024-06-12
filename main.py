import re
elements = [
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-1111",
"38050 111 22 11   ",
"'+48    736-241*295'",
"+1 800-555-5555", 
"+44 20 7946 0958",  
    "+49 30 123456",
]

  
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


list_of_numbers = list(map(normalize_phone, elements))
print(list_of_numbers)



