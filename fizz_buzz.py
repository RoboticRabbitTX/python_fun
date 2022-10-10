# This will be fizz-buzz
# For every number between 1 - 100
# If the number is divisable by 3 print 'fizz'
# If the number is divisable by 5 print 'buzz'
# If the number is divisable by 3 and 5 print 'fizz-buzz'
# If the number is not divisable by either, then print the number
# Example: 1,2,fizz,4,buzz...14,fizz-buzz,16...
for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print("fizz-buzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)


