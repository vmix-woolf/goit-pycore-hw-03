import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    '''Output the list of sorted unique numbers\n
    ARGS:
        min - bottom limit of the lottery
        max - top limit of the lottery
        quantity - quantity of lucky numbers
    RETURNS:
        specific quantity of the lucky numbers in the lottery in the view of sorted list   
    '''
    if min < 1:
        print(f"Value min should be greater or equal than 1")
        return []
    
    if max > 1000:
        print(f"Value max should be less than 1000")
        return []
    
    if quantity > (max - min):
        print(f"Too many winning numbers are set")
        return []
    
    result = set()
    while len(result) < quantity:
        item = random.randint(min, max)
        result.add(item)

    result = list(result)
    result.sort()
    
    return result


lottery_numbers = get_numbers_ticket(1, 35, 5)
print("Your lottery lucky numbers:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery lucky numbers:", lottery_numbers)

lottery_numbers = get_numbers_ticket(0, 35, 5)
print("Your lottery lucky numbers:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 1001, 6)
print("Your lottery lucky numbers:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 20, 50)
print("Your lottery lucky numbers:", lottery_numbers)
