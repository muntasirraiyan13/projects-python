operator=input("Enter an operator + - * / =")
num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2nd number:"))
if(operator=="+"):
    result=num1+num2
    print("The summation of the two numbers=",result)
elif(operator=="-"):
    result=num1-num2
    print("The subtraction of the two numbers=",result)
elif(operator=="*"):
    result=num1*num2
    print("The multiplication of the two numbers=",result)
elif(operator=="/"):
    result=num1/num2
    print("The division of the two numbers=",result)
else:
    print("Invalid input")
