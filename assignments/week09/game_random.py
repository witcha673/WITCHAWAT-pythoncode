import random

#Q1
print("game random number")

rand_int = random.randint(1,100)


while True:
    number_random = int(input("enter your num: "))
    if number_random > rand_int:
        print("more than try again")
    elif number_random == rand_int:
        print("you win")
        break
    else:
        print("less than again")




#Q2
print("game random number 7 time")

rand_int = random.randint(1,100)

for i in range(1, 7):
    print(f"round {i}")
    print(f"count have 6 time")
    number_random = int(input("enter your num: "))
    if number_random == rand_int:
        print("you win")
        break
    elif number_random > rand_int:
        print("more than try again")
        i += 1
    else:
        print("less than try again")
        i += 1
    

print("you lose")


#Q3
print("game random number")

rand_int = random.randint(1,100)

for i in range(1, 999999999999):
    print(f"Attempt {i}:")
    user_input = int(input("Enter your guess (1-100): "))
    if user_input == rand_int:
        print(f"Congratulations You guessed the number {rand_int} correctly in {i} attempts.")
        break
    else:
        print("Wrong guess")
        if i == 3:
            if rand_int % 2 == 0:
                print("Hint: The number is even")
            else:
                print("Hint: The number is odd")
        elif i == 5:
            if rand_int % 3 == 0:
                print("Hint: The number is divisible by 3")
            elif rand_int % 5 == 0:
                print("Hint: The number is divisible by 5")
            else:
                print("Hint: The number is not divisible by 3 or 5")
        elif i == 7:
            lower_bound = max(1, rand_int - 12)
            upper_bound = min(100, rand_int + 12)
            print(f"Hint: The number is between {lower_bound} and {upper_bound}.")
        elif i == 10:
            first_digit = str(rand_int)[0]
            print(f"Hint: The first digit of the number is {first_digit}.")