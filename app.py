weight = float(input("Weight: "))
lbs_or_kg = input("(K)g or (L)bs: ")
if lbs_or_kg == "L" or "l":
    othr_weight = "{:.1f}".format(weight / 2.2)
    final_text = "Weight in Kg: "
elif lbs_or_kg == "K" or "k":
    othr_weight = "{:.1f}".format(weight * 2.2)
    final_text = "Weight in lbs: "
print(f"{final_text}{othr_weight}")