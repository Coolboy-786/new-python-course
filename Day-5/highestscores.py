# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
num=0
maximum=0
for student in student_scores:
    num+=1
for scores in range(0,num):
    if maximum<student_scores[scores]:
        maximum=student_scores[scores]
#print(max(student_scores))
print(f'The maximum number among the above given array is: {maximum}')