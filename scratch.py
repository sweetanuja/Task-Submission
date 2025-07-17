print ("Hello World")
a= input('Enter the first number= ')
a= int(a)
b= input('Enter the second number= ')
b=int(b)
c= a+b
c= print("Addition= ", c)
d= a-b
d= print("Subtraction= ", d)
m= a*b
m= print("Multiplication= ", m)
e= a/b
e= print("Division= ", e)

A= input('Enter the first name= ')
A= str(A)
B= input('Enter the second name= ')
B= str(B)
C= A + ' ' + B
C= print("Hello, "+ C + '! Welcome to the python program')
...

age = int((input("Enter your age: ")))
if age >= 18:
    print('you can vote')
else:
    print('you cannot vote')

Marks = int((input("Enter your marks: ")))
if (Marks >= 40):
    print('passed')
else:
    print('failed')

for i in range(5):
    print('i')

    counter = 1
    while counter <= 6:
        print('a')
        counter = counter + 1

    counter = 6
    while counter >= 1:
        print('a')
        counter = counter - 1

Number= int(input('Enter a number: '))
if (Number % 2== 0):
    print('Number is even')
else:
    print('Number is odd')

    a = 0
    for c in range(1, 51):
        a += c
    print('The sum of numbers from 1 to 50 is', a)