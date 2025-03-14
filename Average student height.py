students_heights = input("Enter an students height").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height= 0

for height in students_heights:
    total_height+= height
print(total_height)

no_of_student = 0

for length in students_heights:
    no_of_student+= 1
print(no_of_student)

average_height = total_height/no_of_student
average_height = str(average_height)

print("The average heights of the student is: " + average_height)