# write a program that calculates the average student height from a List of heights

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

average_height = round(sum(student_heights) / len(student_heights))

print(
    f"There are {len(student_heights)} students and their average height is {average_height}")
