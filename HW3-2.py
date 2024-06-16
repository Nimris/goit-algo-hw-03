import random
import re

def get_numbers_ticket(min = 1, max = 999, quantity = 5):
    
    try:
        #Отримуємо данні від користувача та розпаковуємо в мін, макс, кількість
            #pattern = r"[#@;!]"
            #fruits = re.split(pattern, text)
        min, max, quantity = input("Min, max, quantity: ").split(",") 
    
        #Переводимо в int
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        
        # Перевіряємо відповідність параметрів
        if min >= 1 and max <= 1000 and (min < quantity < max):
            
            #Додаємо рандомні числа в список numbers
            numbers = []
            for i in range(quantity):
                numbers.append(random.randrange(min, max)) 
                
            #Сортуємо та видаляємо повторні значення
            unique_numbers = list(set(numbers))
            unique_numbers.sort()

            print(unique_numbers)
            return unique_numbers
    
        else:
            print("Invalid value")
            return []
        
    except:
        print("Try again")
        return []
    
get_numbers_ticket()