import csv
import random
from collections import defaultdict
from pathlib import Path


def get_birthday_weights(birth_data_path):
    """
    Process a CSV file with columns: year, month, day, and number of people born.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - List[int]: An array containing the total number of people born on each day of the year.
    """
    # Dictionary to store the total number of people born on each day of the year
    births_by_day = defaultdict(int)

    with open(birth_data_path, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)

        # Skip the header if present
        next(csv_reader, None)

        # Loop through rows and update the dictionary
        for row in csv_reader:
            year, month, day, _, births = row

            # Combine year, month, and day into a tuple to represent the date
            birthday = (int(month), int(day))

            # Increment the total number of people born on that date
            births_by_day[birthday] += int(births)

    # Convert the dictionary to a list of integers representing the total number of people born on each day
    total_births_by_day = [births_by_day[date] for date in sorted(births_by_day.keys())]

    return total_births_by_day


BIRTHDAY_WEIGHTS = get_birthday_weights("US_births_2000-2014_SSA.csv")
BIRTHDAY_ARRAY = list(range(1, 367))


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
        chosen_number = random.choices(BIRTHDAY_ARRAY, BIRTHDAY_WEIGHTS)[0]
        birthdays.append(chosen_number)
    return has_duplicates(birthdays)


def run_simulation():
    for x in range(2, 367):
        num_collisions = 0
        for _ in range(10000):
            if has_collision(x):
                num_collisions += 1
        print(f'{x},{num_collisions}')


run_simulation()