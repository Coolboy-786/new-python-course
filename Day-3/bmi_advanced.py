# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height2 = height**2
#print(height2)
bmi = round(weight/height2)
#print(bmi)
if bmi < 18.5:
    print('Your BMI is'+ " " + str(bmi)  +', you are underweight.')
elif bmi <25:
    print('Your BMI is'+ " " + str(bmi)  +', you have a normal weight.')
elif bmi <30:
    print('Your BMI is'+ " " + str(bmi)  +', you are slightly overweight.')
elif bmi <35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinicaly obese")