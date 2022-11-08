numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
previous = 0

for current in numbers:
    sum = current + previous
    print(f"Current Number {current} Previous Number {previous} Sum: {sum}")
    previous = current