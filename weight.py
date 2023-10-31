weight = float(input("Weight "))
KorL = input("(K(g) or (L)bs: ")

if KorL == 'K' or KorL == 'k':
    print("Weight in Kg: " + str(weight))
elif KorL == "L" or "l":
    result = weight * 0.45359237 
    print("Weight in Lbs " + str(result))
else:
    print("Invalid input")

