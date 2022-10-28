#if else statement
age=int(input('enter your age: '))
if age >=18:
    print('You can Vote')
elif age <= 18 and age >=13:
    print('You age in teenagers')
else:
    print('You are not adult')
    