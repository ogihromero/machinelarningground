from os import path


# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result
# which contains the numbers that are common in both files.
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


with open(dir("file1.txt"), "r") as file1:
    list1 = file1.read().splitlines()

with open(dir("file2.txt"), "r") as file2:
    list2 = file2.read().splitlines()


result = [int(n) for n in list1 if n in list2]
# Write your code above 👆

print(result)
