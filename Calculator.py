import math 
#Taking User input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))

while(1):
    print("\n\tArithmetic Operations:\n\t\t1.Addition\n\t\t2.Substraction\n\t\t3.Multiplication\n\t\t4.Division\n\t\t5.Modulus\n\t\t6.Exit")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:print("The Addition: ",num1," & ",num2," is: ",num1+num2)
        case 2:print("The Substraction: ",num1," & ",num2," is: ",num1-num2)
        case 3:print("The Multiplication: ",num1," & ",num2," is: ",num1*num2)
        case 4:print("The Division: ",num1," & ",num2," is: ",num1/num2)
        case 5:print("The modulous: ",num1," & ",num2," is: ",num1%num2)
        case 6:break
        case _:print("Wrong Choice")
print("BYE!!!! BYE!!!!!")
