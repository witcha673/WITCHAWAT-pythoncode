"""
Week 1 Lab - Additional Practice Exercises (SOLUTIONS)
Complete these exercises to reinforce your learning.
"""

# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
hobby = input("Enter your favorite hobby: ")

print("\n--- PROFILE ---")
print("Name:", full_name)
print("Age:", age)
print("Email:", email)
print("Phone:", phone)
print("Hobby:", hobby)

# Exercise 2: Shopping Receipt
print("\n=== Shopping Receipt ===")
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: $"))
quantity = int(input("Enter quantity: "))
total_cost = item_price * quantity

print("\n--- RECEIPT ---")
print("Item:", item_name)
print("Price: $" + str(item_price))
print("Quantity:", quantity)
print("Total: $" + str(total_cost))

# Exercise 3: Student Grade Calculator
print("\n=== Student Grade Calculator ===")
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))
average = (score1 + score2 + score3) / 3

print("Test 1:", score1)
print("Test 2:", score2)
print("Test 3:", score3)
print("Average:", round(average, 2))

# Exercise 4: Time Converter
print("\n=== Time Converter ===")
total_minutes = int(input("Enter number of minutes: "))
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(total_minutes, "minutes =", hours, "hours and", remaining_minutes, "minutes")

# Exercise 5: Circle Calculator
print("\n=== Circle Calculator ===")
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159

diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius

print("Radius:", radius)
print("Diameter:", diameter)
print("Circumference:", round(circumference, 2))
print("Area:", round(area, 2))

# Exercise 6: String Manipulator
print("\n=== String Manipulator ===")
sentence = input("Enter a sentence: ")
word_count = sentence.count(' ') + 1

print("Original:", sentence)
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Character count:", len(sentence))
print("Word count:", word_count)

# Exercise 7: Password Strength Checker (Basic)
print("\n=== Password Strength Checker ===")
password = input("Enter a password: ")
length = len(password)
is_strong = length > 8

print("Password length:", length)
print("Longer than 8 characters:", is_strong)
print("First character:", password[0])
print("Last character:", password[-1])

# Exercise 8: Distance Calculator
print("\n=== Distance Calculator ===")
speed = float(input("Enter speed (mph): "))
time = float(input("Enter time (hours): "))
distance = speed * time

print("Distance traveled:", distance, "miles")

# Exercise 9: Age in Days
print("\n=== Age in Days Calculator ===")
age_years = int(input("Enter your age in years: "))
age_days = age_years * 365
age_hours = age_days * 24
age_minutes = age_hours * 60

print("Age in days:", age_days)
print("Age in hours:", age_hours)
print("Age in minutes:", age_minutes)

# Exercise 10: Bill Splitter
print("\n=== Bill Splitter ===")
bill_amount = float(input("Enter total bill amount: $"))
num_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = bill_amount * (tip_percentage / 100)
total_with_tip = bill_amount + tip_amount
amount_per_person = total_with_tip / num_people

print("Bill amount: $" + str(bill_amount))
print("Tip amount: $" + str(round(tip_amount, 2)))
print("Total with tip: $" + str(round(total_with_tip, 2)))
print("Amount per person: $" + str(round(amount_per_person, 2)))

# Bonus Challenge: Mad Libs Game
print("\n=== Mad Libs Game ===")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")

story = f"The {adjective1} {noun1} decided to {verb1} over the {adjective2} {noun2}. It was quite an adventure!"
print("\nYour Mad Libs story:")
print(story)