# Write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each num from 1 to 100 in turn.
# When the num is divisible by 3 then instead of printing the num it should print "Fizz".
# When the num is divisible by 5, then instead of printing the num it should print "Buzz".`
#   And if the num is divisible by both 3 and 5 e.g. 15 then instead of the num it should print "FizzBuzz"

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
