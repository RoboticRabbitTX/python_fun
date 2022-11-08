num_1 = int(input("First: "))
num_2 = int(input("Second: "))
product = num_1 * num_2
sum = num_1 + num_2

def cmpr_1000():
    if product <= 1000:
        print(product)
    else:
        print(sum)

cmpr_1000()