import random
random_number = random.randint(1,100)
balance = 5
low = 1
high = 100

while True:
    try:
        guess = int(input(f"Guess Number ({low}-{high}): "))
    except ValueError:
        print("please key in Value Number")
        continue

    if guess < low or guess > high:
        print(f"please guess number between ({low}-{high})")
        continue


    if guess > random_number:
        high = min(high, guess - 1)
        print(f"Too high ({low}-{high})")
    elif guess < random_number:
        low = max(low, guess + 1)
        print(f"Too low ({low}-{high})")
    else:
        print(f"Correct!")
        break

    balance -= 1
    print(f"Remaining tries: {balance}")

    if balance == 0:
        print(f"Game Over\nThe Number is {random_number}")
        break