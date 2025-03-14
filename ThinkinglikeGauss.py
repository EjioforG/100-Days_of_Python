# students_heights = input("Enter an students height").split()
# for n in range(0, len(students_heights)):
#     students_heights[n] = int(students_heights[n])
# print(students_heights)
sum = 0
for total in range(2, 101, 2):
    sum += total
print(sum)

sum2 = 0
for total in range(1, 101):
    if total % 2 == 0:
        sum2 += total
print(sum2)
         
