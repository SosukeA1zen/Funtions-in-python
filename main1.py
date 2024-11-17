def add(x,y):
    return x+y
 
def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y
num1=int(input("Enter number1:"))
num2=int(input("Enter number2"))

print("Add number1 and number2",add(num1,num2))
print("Subtract number1 and number2",subtract(num1,num2))
print("Divide number1 and number2",divide(num1,num2))
print("Multiply number1 and number2",multiply(num1,num2))