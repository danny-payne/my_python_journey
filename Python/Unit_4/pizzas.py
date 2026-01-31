my_pizzas = ['pepperoni', 'mushroom', 'spinach' ]

#Friend pizza copy
friend_pizzas = my_pizzas [:]

#add distinctions
my_pizzas.append('sausage')
friend_pizzas.append('anchovie')

for pizza in my_pizzas:
    print(f"I like {pizza.title()}")

#spacing

print("\n")
for pizza in friend_pizzas:
    print(f"My friend likes {pizza.title()}")

print("\nWe really like Pizza!")