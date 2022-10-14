import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma:- ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(names)
#sleected_name = random.choice(names)
#print(sleected_name + " is going to buy a drink today")

i = random.randint(0,len(names)-1)
selected_name = names[i]

print(selected_name +" is going to buy a drink today")