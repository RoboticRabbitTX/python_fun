weight = float(input("Weight: "))
lbs_or_kg = input("(K)g or (L)bs: ")
if lbs_or_kg == "L" or "l":
    othr_weight = weight / 2.2
    final_text = "Weight in Kg: "
elif lbs_or_kg == "K" or "k":
    othr_weight = weight * 2.2
    final_text = "Weight in lbs: "
othr_weight_str = "{:.1f}".format(othr_weight) # How u change floats decimal place
print(final_text + othr_weight_str)