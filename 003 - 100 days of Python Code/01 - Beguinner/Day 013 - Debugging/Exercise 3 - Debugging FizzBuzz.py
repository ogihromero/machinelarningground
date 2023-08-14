for number in range(1, 101):
    # if number % 3 == 0 or number % 5 == 0: # should be 'and' and it's missing elif in the comparisons
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # print([number]) # printing a list
        print(number)
