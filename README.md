# Homework #03

### Algorithm for task04
- get birthday_this_year from string in user "birthday" key and change it to this year
- make datetime object for birthday_this_year
- make datetime object for today
- find what is less - birthday_this_year or today
- if birthday has already been, update birthday_this_year with next year
- find difference between birthday_this_year and today
- if difference <= 7 days check if birthday_this_year isn't a weekend day
    - if YES, add congratulations_day to next MONDAY
    - if NO, add congratulations_day to the new structure upcoming_birthday
- if difference > 7 days, skip this user