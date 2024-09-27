import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # TODO: validation input data and fuction docs
    result = set()
    while len(result) < quantity:
        item = random.randint(min, max)
        result.add(item)

    result = list(result)
    result.sort()
    
    return result

print(get_numbers_ticket(1, 35, 5))
print(get_numbers_ticket(1, 49, 6))