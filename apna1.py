name="Rupam"
age=19
print(name)
print(age)
print(name,age)

x=input("What is your SuperHero? ")
print(x)
print("Your SuperHero is "+x)
print("Your SuperHero is",x)

old_age=input("Enter your old age: ")
#new_age=(float(old_age))+5
new_age = int(old_age)+5
print("Now Your Age is ",new_age)

#string calculate
first=input("enter the first number: ")
second=input("enter the second number: ")
#sum=first+second
print(sum)   #here output is 36 bcoz we clculate two string number

#Interger number calculate
first=input("enter the first number: ")
second=input("enter the second number: ")
sum=int(first)+int(second)
print(sum)  #output is 9 bcoz here we calculate two integer number

first=input("enter the first number: ")
second=input("enter the second number: ")
sum=int(first)+int(second)
print("The sum is "+str(sum))

#index location
rupam="Spider Man"
print(rupam.upper())
print(rupam.lower())
print(rupam.find('M'))
print(rupam.find('x'))

#Replace case
rupam="Spider Man"
print(rupam.replace("Spider","Iron"))
print(rupam.replace('Spider Man','Iron Man'))

#search in string
x="Spider Man"
print('S' in x)
print('K' in x)
print("Spider" in x)
print("Iron" in x) 

#python follows the bodmas rule during the multiplication
sum=2+3*10
sum=(2+3)*10
print(sum)

#comparation operator
print(2>3)
print(2<3)
print(2>=3)
print(2<=3)
print(2==3)
print(3==3)
print(2!=3)   #not equal to

