#try catch using input statement

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Cannot divide a number by zero")
    
print("Programs continues")
'''
output:
Enter first number :10
Enter second number :5
2.0
Programs continues

or

Enter first number :200
Enter second number :0
Cannot divide a number by zero
Programs continues
'''

a=int(input("Enter first number :"))
b=[1,2,3]
try:
    c=a/b[4]
    print(c)
except ZeroDivisionError:
    print("Cannot divide a number by zero")
except IndexError:
    print("Index out of bound")
print("Programs continues")

'''
output:
Enter first number : 10
Index out of bound
Programs continues
'''

try:
    try:
        s=input("Enter any string :")
        print(s[5])
        print(s//2)
    except IndexError:
        print("Index out of bound")
        
except TypeError:
    print("Wrong String Operation")

'''
output:
Enter any string :Abhishek
h
Wrong String Operation
'''    
