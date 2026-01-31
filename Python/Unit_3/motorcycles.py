# Creating list of motorcycles
motorcycles = []
# adding values to list
motorcycles.append('ducati')
motorcycles.append('indian')
motorcycles.append('honda')

#print list
print(motorcycles)

#adding new entry at the beginning shifiting all other values up
motorcycles.insert(0, 'bmw')
print(motorcycles)

#remove entry with del
del motorcycles[0]
print(motorcycles)

#remove with pop with a little flair
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f"The last motorcycle on the list is {last_owned.title()}")
print(f"But the first one is {first_owned.title()}")
print("\nLet's get those one's off the list")

#add some new items to the list 
motorcycles.append('harley')
motorcycles.append('liberty')
motorcycles.append('ninja')
New_additions = motorcycles

print(f"We have some new additions! Here's our list {New_additions}")

#remove a specific value and let us know what was removed
too_expensive= 'indian'
motorcycles.remove(too_expensive)
print(f"\nOur current list is {motorcycles} with {too_expensive.title()} removed.")