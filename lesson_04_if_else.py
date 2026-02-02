age = int(input("ile masz lat?"))

if age < 13:
    category = "Dziecko"
elif age < 18:
    category = "Nastolatek"
else:
    category = "Dorosly"
print(f"category: {category}")

