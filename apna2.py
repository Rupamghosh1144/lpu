#if else statement
age=int(input('enter your age: '))
if age >=18:
    print('You can Vote')
elif age <= 18 and age >=13:
    print('You age in teenagers')
else:
    print('You are not adult')
    
    # create a mini calculator using if/else condition
x=input('Enter the first number: ')
z=input('Choose the operator(+,-,*,/,%): ')
y=input('Enter the second number: ')
x=int(x)
y=int(y)
if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    print(x/y)    
elif z=="%":
    print(x%y)
else:
    print('Invalid Syntax')
    
    
