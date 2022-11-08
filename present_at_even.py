# accept a string from the user and display characters that are present at an even index number
str = input("String: ")
counter = "even"

for c in str:
    if counter == "even":
        print(c)
        counter = "odd"
    else:
        counter = "even"