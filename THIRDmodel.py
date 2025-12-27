import random 
import time 

print(random.randrange(-1 , 11)) # "randrange" does not include last number but "randient" 'must include the last number

top_of_range = input("Type a number :- ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

random_number = random.randint()