num1=int(input("Enter your value - "))
num2=int(input("Enter your value - "))
opr=input("Enter your operator")

if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="/":
     print(num1/num2)
elif opr=="*":
    print(num1*num2)

else:
    print("invalid operator entered...")
