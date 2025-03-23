def add(P,Q):
    #This function is used for adding two numbers
    return P + Q
def Subtract(P,Q):
    #This function is used for subtracting two numbers
    return P - Q
def multiply(P,Q):
    #This function is used for multiplying two numbers
    return P * Q
def divide(P,Q):
    #This function is used for dividing two numbers
    return P / Q

#Now we will take input from user
print("Please slect the operation.")
print("a. add")
print("b. subtract")
print("c. Multiply")
print("d. divide")

choice = input("please enter your choice (a/ b/ c/ d):")

num_1 = int(input("please enter the first number"))
num_2 = int(input("please enter the Second number"))

if choice == 'a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
    
elif choice == 'b':
    print(num_1,"-",num_2,"=",Subtract(num_1,num_2))
    
elif choice == 'c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
    
elif choice == 'd':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("This is an invalid input")