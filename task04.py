from datetime import datetime as dt, timedelta

def get_upcoming_birthdays(users: list[dict[str: str]]) -> list:
    upcoming_birthdays = []
    today = dt.today().date()
    
    for user in users:
        birthday_this_year = (dt.strptime(user["birthday"], "%Y.%m.%d")).date().replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  

        if (birthday_this_year - today).days < 7:
            if birthday_this_year.weekday() < 5:  # weekday
                upcoming_birthday = {
                    "name": user["name"],
                    "congratulation_date": dt.strftime(birthday_this_year, '%y.%m.%d')
                }
            elif birthday_this_year.weekday() == 5:  # Saturday
                upcoming_birthday = {
                    "name": user["name"],
                    "congratulation_date": dt.strftime(birthday_this_year + timedelta(days=2), '%y.%m.%d')
                }   
            else:  # Sunday
                upcoming_birthday = {
                    "name": user["name"],
                    "congratulation_date": dt.strftime(birthday_this_year + timedelta(days=1), '%y.%m.%d')
                }
        else: 
            continue

        upcoming_birthdays.append(upcoming_birthday)

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.11.27"},
    {"name": "Ralf Ericsson", "birthday": "1977.06.11"},
    {"name": "Mike Johnson", "birthday": "1987.09.27"},
    {"name": "Nikolas Ripke", "birthday": "1987.09.28"},
    {"name": "Olivia Tacasa", "birthday": "1987.09.29"},
    {"name": "Donald Pitbull", "birthday": "1967.10.2"},
    {"name": "Gerald Tartar", "birthday": "2004.10.3"},
    {"name": "Elizabeth Malkovich", "birthday": "1996.10.4"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's congratulations list:", upcoming_birthdays)
