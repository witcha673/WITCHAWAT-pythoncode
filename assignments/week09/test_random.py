import random

# def test_random():
#     random_number = random.randint(1, 100)
#     print(random_number)
    
# test_random()


print("game random number")

rand_int = random.randint(1,10)


while True:
    number_random = int(input("enter your num: "))
    if number_random > rand_int:
        print("more than")
        break
    elif number_random == rand_int:
        print("you win")
    else:
        print("less than")

