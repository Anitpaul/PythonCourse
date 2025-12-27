from datetime import date,timedelta

today = date.today()
interview = today + timedelta(days=9)
name = input("Enter your name:  ").strip().lower().capitalize()

letter = f"""Dear {name}, 
You are selected!
Interview Date: {interview}
"""

print(letter)