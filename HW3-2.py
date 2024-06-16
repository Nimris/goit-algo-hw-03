import random

def get_numbers_ticket(min = 1, max = 1000, quantity = 10):
    
    try:
        #Отримуємо данні від користувача та робимо список
        user_input = input("Min, max, quantity: ").split(",")
    
        #Переводимо в int
        min, max, quantity = map(int, user_input)
        
        # Перевіряємо відповідність параметрів
        if max > 1000:
            print("Max value is 1000")
            get_numbers_ticket()
        
        if quantity < min or quantity > max:
            print("Quantity value is incorrect")
            get_numbers_ticket()
            
        if min >= 1 and max <= 1000 and (1 <= quantity <= max):
            
            #Додаємо рандомні числа в множину numbers
            numbers = set()
            while len(numbers) < quantity:
                numbers.add(random.randrange(min, max)) 
                
            #перетворюємо в список та сортуємо
            unsorted_list = list(numbers)
            sorted_list = sorted(unsorted_list)
            
            print(sorted_list)
            return sorted_list
        
        else:
            print("Enter 3 numbers in format '1, 999, 10'")
            get_numbers_ticket()
    
    except:
        print("Enter 3 numbers in format '1, 999, 10'")
        get_numbers_ticket()
    
    finally:
        print("* " *10)
    
get_numbers_ticket()