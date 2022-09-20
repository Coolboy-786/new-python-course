#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("what is the total bill? $"))
#print('$' + str(bill))
tip = float(input("What percentage of the tip would you like to give?"))
#print(tip)
total_bill = (1+(tip)/100)*bill
#print(total_bill)
num_person = int(input("How many people to split the bill? "))
per_person_cost = round(total_bill/num_person,2)
#print(per_person_cost)
print(f"Each person should pay: ${per_person_cost}")