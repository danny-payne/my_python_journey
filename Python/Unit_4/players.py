#select a slice of list
players= ['charles', 'martina', 'michael', 'florence', 'eli','jacob','richard',
'Zebulon']
#print(players[0:3])
#print(players[:4])
#print(players[2:])
#print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#middle of the list slice
print("\nThree names from the middle are:")
for player in players[3:6]:
    print(player.title())

#last 3 of the list
print("\nThe last three names would be:")
for player in players[-3:]:
    print(player.title())