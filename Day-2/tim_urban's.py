# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_left = 90-int(age)
#print(age_left)
months = age_left*12
#print(months)
weeks = age_left*52
#print(weeks)
days = age_left*365
#print(days)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")