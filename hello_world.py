# %%
name = input('What is your name?')
birth_year =input ('What is your birth year?')

print(f'Hello,{name}!')

from datetime import datetime 
year =datetime.now().year

print(f'You must be {int(year)- int(birth_year)}')
print (f'Goodbye, {name}!')
# %%