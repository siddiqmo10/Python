# Project
w = input("Weight: ")
scale = input("(L)bs or (k)g: ")

# we could have used scale.upper() and check for only "L"

if scale == "L" or scale == "l":
    conv = 0.45 * int(w)
    print(f"You are {conv} kilos")

else:
    conv = int(w) / 0.45
    print(f"You are {conv} lbs")