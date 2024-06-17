#Генерація випадкових чисел

import random

def get_numbers_ticket(min = 1, max = 1000, quantity = 10):
    
    try:
        #Отримуємо данні від користувача та робимо список
        user_input = input("Min, max, quantity: ").split(",")
        
        if len(user_input) != 3:
            print("Please enter exactly three values separated by commas")
            get_numbers_ticket()
    
        #Переводимо в int
        min, max, quantity = map(int, user_input)
        
        #Перевіряємо відповідність параметрів
        if not (1 <= min < max <= 1000):
            print("Min should be >= 1 and max should be <= 1000.")
            get_numbers_ticket()
        if quantity >= (max - min):
            print("Quantity should be between the range of min and max.")
            get_numbers_ticket()    
        
        if min >= 1 and max <= 1000 and (1 <= quantity < max):
                
            #Отримуємо випадкові числа та сортуємо їх    
            list_of_numbers = random.sample(range(min, max), quantity)
            sorted_numbers = sorted(list_of_numbers)
            
            print(sorted_numbers)
            return sorted_numbers
            
        else:
            print("Invalid input. Try again")
            get_numbers_ticket()
    
    except:
        print("Invalid values. Try again")
        get_numbers_ticket()   
    
get_numbers_ticket()