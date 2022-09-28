# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TRUE LOVE

name1_lower = name1.lower()
name2_lower = name2.lower()

new_name = name1_lower + name2_lower

#TRUE
count_t = new_name.count('t')
count_r = new_name.count('r')
count_u = new_name.count('u')
count_e = new_name.count('e')

#LOVE
count_l = new_name.count('l')
count_o = new_name.count('o')
count_v = new_name.count('v')

total1 = count_t + count_r + count_u + count_e
total2 = count_l + count_o + count_v + count_e
score = str(total1) + str(total2)

if score<'10' or score>'90':
    print(f'Your score is {total1}{total2}, you go together like coke and mentos.')
elif score<'50' and score>'40':
    print(f'Your score is {total1}{total2}, you are alright together.')
else:
    print(f'Your score is {total1}{total2}.')