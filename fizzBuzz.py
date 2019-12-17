
#take user input
userInput = input("Input a range to run :")

for x in range(int(userInput)):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue

    elif x % 5 == 0:
        print("Buzz")
        continue
        print(x)
