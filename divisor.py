# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

## First method of doing this example..

num = int(input('Enter any number:'))
listRange = list(range(1, num+1))
divisor = []

for number in listRange:
    if num % number == 0:
        divisor.append(number)

print(divisor)



## second method of doing same example.

number1 = int(input('Enter a number:'))
lst = []

for i in range(2, number1):
    if number1 % i == 0:
        lst.append(i)

print(lst)
