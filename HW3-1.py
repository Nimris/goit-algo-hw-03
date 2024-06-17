from datetime import datetime

def get_days_from_today():
    
    date = input("Write date in a format 'YYYY-MM-DD': ")                
    
    try:
        #Переводимо рядок в дату        
        d_obj = datetime.strptime(date, "%Y-%m-%d").date()
        
        #Визначаємо сьогоднішню дату
        now = datetime.today().date()
        
        #Визначаємо різницю
        result = (d_obj - now).days
        
        print(f"Your date: {d_obj}")
        print(f"Today: {now}")
        print(f"Days from today: {result}")
        return result
    
    except:
        print("Format is incorrect. Try again")
        get_days_from_today()
        
    finally:
        print("-" * 20)
        
get_days_from_today()