#A buffet style restaurant offers only five basic foods. Think of five simple 
#foods, and store them in a tuple
simple_foods = ('shrimp', 'chicken', 'broccoli', 'mac', 'potatoes')
for food in simple_foods:
    print(food.title())

# attempt to change
#simple_foods[-1] = 'corn'

#replace values
print("\nThis is the modified menu:")
simple_foods = ('shrimp', 'chicken', 'broccoli', 'spinach', 'texas toast')
for food in simple_foods:
    print(food.title())


