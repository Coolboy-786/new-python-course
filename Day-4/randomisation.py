import random
import pi_value

random_integer = random.randint(1,10)
print(random_integer)
print(pi_value.pi)

#random.random() -> Returns the next random floating point number between [0.0 to 1.0)
random_float = random.random()
random_float*=10
#random numbers from 1-10
print(random_float)

love_score = random.randint(1,100)
print(f'Your love score is {love_score}')