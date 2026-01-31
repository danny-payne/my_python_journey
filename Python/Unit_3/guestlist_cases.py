#Building our list
guest_list=['Otto Rank', 'Earnest Becker', 'Julius Caeser']
#Invite each of current guest through iteration
def send_invites():
    for guest in guest_list:
        print(f"{guest}, you are invited to dinner")
#Invite EACH original guest
print(f"{guest_list[0]}, you are invited to dinner")
print(f"{guest_list[1]}, you are invited to dinner")
print(f"{guest_list[-1]}, you are invited to dinner")

#Julius is can't make it and sends Napoleon as his replacement
print(f"\n{guest_list[-1]}, cannot make it")
guest_list[-1] = 'Napoleon'

#print new line
print()

#Invite each of current guest through function
send_invites()

#we have more space

##print new line
print()
print(f"{guest_list}, we have more space")

#insert new guests
guest_list.insert(0, 'Carl Jung')
guest_list.insert(2, 'Plato')
guest_list.append('Hildegard Von Bingen')
##print new line
print()

#Welcome new guests
print("Welcome new additions and old. Our new guest list:")

##print new line
print()

#Invite each of current guest through function
send_invites()

##print new line
print()

#Not enough Space only two
print(f"{guest_list} We only have room for 2, we will have to see some of you back soon.")

#Pop em out of here
Napoleon_univited = guest_list.pop(5)
Julius_uninvited = guest_list.pop(-1)
Plato_uninvited = guest_list.pop(2)

print(f"\n{Napoleon_univited}, you are uninvited due to space")
print(f"\n{Julius_uninvited}, you are uninvited due to space")
print(f"\n{Plato_uninvited}, you are uninvited due to space")

##print new line
print()

#sort then Invite each of current guest through function
guest_list.sort()
send_invites()

#we have no room
for _ in range(3):
    del guest_list [0]

print (guest_list)
