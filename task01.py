from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''Calculate difference between desired date sent as a string
    and current date\n
    ARGS:
        String expressing the desired date
    RETURNS:
        Number of days between two dates, desired date and today.
    '''
    today = datetime.today()   
    try:
        desired_date = datetime.strptime(date, '%Y-%m-%d')
        print((desired_date - today).days)
    except ValueError:
        print(f"Date should be in the correct YYYY-MM-DD format")  

    
get_days_from_today("2024-11-05")  # voting in the USA
get_days_from_today("2026-08-26")  # graduation from Neoversity
get_days_from_today("2023-12-31")  # New Year's Eve
get_days_from_today("2023-12-25")  # last Christmas
get_days_from_today("2023-13-25")  # exception
get_days_from_today("2025-04-32")  # exception
get_days_from_today("20221225")    # exception
