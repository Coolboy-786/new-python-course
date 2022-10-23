# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(len(student_heights))
total=0
num=0
for n in range(0, len(student_heights)):
    total+=int(student_heights[n])
for student in student_heights:
    num+=1
average = total/num
#print(f'sum is equal to {sum}')
print(round(average))
