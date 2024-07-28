def call():
    print("Welcome to Kunji Munji's Mad House")

call()

def sum(a,b):
    print(a+b)

sum(10,20)
sum(20,30)

def sum1(a,b=1):
    print(a+b)

sum1(10)
sum1(20,30)

def square(x):
    return x*x,x*2
s=square(5)
print(s)