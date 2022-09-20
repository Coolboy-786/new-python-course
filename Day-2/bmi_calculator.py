#BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#height = input("enter your height: ")
#weight = input("enter your weight: ")
#print(type(height))
#print(type(weight))

height2 = float(height)**2
#print(height2)

bmi = int(weight)/height2
print(int(bmi))