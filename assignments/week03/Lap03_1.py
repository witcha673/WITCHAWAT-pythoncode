# Complete this program to classify people by age


# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

print("program check age")
age = int(input("enter your age"))

if age >= 60:
    print("you is Senior")

elif age >=20 and age <=59:
    print("you is adult")

elif age >=13 and age <=19:
    print("you is Teenager")

elif age >=0 and age <=12:
    print("you is child")

else:
    print("you no have age")



