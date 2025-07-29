"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

personal = []
for x in range(1,5):
    in_personal = input("enter information personal 4time 1name, 2age, 3city, 4country. ")
    personal.append(in_personal)

hobbies = []
for i in range(1,3):
    in_hobbies = input("enter hobbies 2 time. ")
    hobbies.append(in_hobbies)

print(f"you data is now {personal} {hobbies}")

coppyage  = personal.copy()

action = input("what delete hobbies index choose 0,1 if enter another exit program. ")
if action == "0":
    hobbies.pop(0)
    print(f"hobbies is now {hobbies}")
    age_new = input("enter new age-")
    coppyage.insert(1,age_new)
    print(f"informatio update {coppyage}")
elif action == "1":
    hobbies.pop(1)
    age_new = input("enter new age-")
    coppyage.insert(1,age_new)
    print(f"informatio update {coppyage}")
else:
    print(f"you data {personal} and hobbies {hobbies}")
    print("no delete hobbies and update new age")



  