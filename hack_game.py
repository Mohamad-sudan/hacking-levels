money =9999999999999999990

print("=== لعبة Mohmad للتهكير ===")
print(f"معاك {money} جنيه")
print("1 - اشتري سلاح (50 جنيه)")
print("2 - اهكر اللعبة")

choice = input("اختار: ")

if choice == "1":
    money = money - 50
    print(f"اشتريت! باقي معاك {money}")
elif choice == "2":
    print("ههههه بتحاول تهكر؟ افتح الكود وغير قيمة money!")
else:
    print("اختيار غلط")

print(f"رصيدك النهائي: {money}")
