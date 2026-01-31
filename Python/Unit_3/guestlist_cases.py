#Building our list
guest_list=['Otto Rank', 'Earnest Becker', 'Donald Trump']
#Invite each of current guest through iteration
def send_invites():
    for guest in guest_list:
        print(f"{guest}, you are invited to dinner")
#Invite EACH original guest
print(f"{guest_list[0]}, you are invited to dinner")
print(f"{guest_list[1]}, you are invited to dinner")
print(f"{guest_list[-1]}, you are invited to dinner")

#Trump is can't make it and sends JD Vance as his replacement
print(f"\n{guest_list[-1]}, cannot make it")
guest_list[-1] = 'JD Vance'

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
guest_list.insert(2, 'Julius Caeser')
guest_list.append('Napoleon Bonaparte')
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
print(f"{guest_list} We only have room for 2, all Dicatators or those who are undemocratic will be removed")

#Pop em out of here
Napoleon_univited = guest_list.pop(5)
JD_uninvited = guest_list.pop(-1)
Julius_uninvited = guest_list.pop(2)

print(f"\n{Napoleon_univited}, you are uninvited due to being a sleeze")
print(f"\n{JD_uninvited}, you are uninvited due to being a sleeze")
print(f"\n{Julius_uninvited}, you are uninvited due to being a sleeze")

##print new line
print()

#sort then Invite each of current guest through function
guest_list.sort()
send_invites()

#we have no room
for _ in range(3):
    del guest_list [0]

print (guest_list)
