#program to tell u how many vowels are in a word
def split(word): #converts word into list
    return list (word.upper())

#variables
word = input("Word: ")
split = split(word)
vowels = ["A", "E", "I", "O", "U"]
counter = 0

for letter in split:
    if letter in vowels:
        counter += 1

print("Number of Vowels: " + str(counter))
