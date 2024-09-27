# Homework #03

### Algorithm for task04
- get real_birthday_date
- make datetime object from real_birthday string
- make datetime object for today
- update real_birthday with current year - save result in birthday_this_year
- find what is less - birthday_this_year or today
- if birthday has already been, update birthday_this_year to next_birthday datetime object
- find difference between next_birthday and today
- if difference <= 7 days check if next_birthday isn't a weekend day
    - if YES, add congratulations_day to next MONDAY
    - if NO, add congratulations_day to the new structure upcoming_birthday
- if difference > 7 days, skip this collegue