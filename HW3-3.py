import re

def phone_number() -> str:
    
    unformated_number = input("Your number: ")
    
    #Видаляємо все крім плюса та цифр
    pattern = r"[^\d+]"
    formated_number = re.sub(pattern, "", unformated_number)
    
    #Додаємо +38
    if not formated_number.startswith("+38"):
        if formated_number.startswith("38"):
            final_number = "+" + formated_number 
        else:
            final_number = "+38" + formated_number
    else:
        final_number = formated_number
        
    print(final_number)
    return final_number
    
phone_number()