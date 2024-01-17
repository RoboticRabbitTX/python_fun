import random


def has_duplicates(my_list):
    # Use a set to check for unique elements
    unique_elements = set()

    for element in my_list:
        # If the element is already in the set, it's a duplicate
        if element in unique_elements:
            return True
        # Otherwise, add it to the set
        else:
            unique_elements.add(element)
    return False


def has_collision(num_people):
    birthdays = []
    for _ in range(num_people):
        # Generate a random integer between 1 and 365 (inclusive)
        random_integer = random.randint(1, 365)

        # adds random integer to list
        birthdays.append(random_integer)

    return has_duplicates(birthdays)


def run_simulation():
    for x in range(2, 366):
        num_collisions = 0
        for _ in range(10000):
            if has_collision(x):
                num_collisions += 1
        print(f'{x},{num_collisions}')


run_simulation()