a=5
print(a,"a is a type of ",type(a))

a=5.5
print(a,"a is a type of ",type(a))

a=2+1j
print(a,"a is a type of ",type(a))

a='10'
print(a,"a is a type of ",type(a))

s = "Hello@123"
print(s,type(s))

s='''
Hello
Welcome to Amit's computer
'''

print(s)

l=[10,'ws',5.5,40,50]
print(l)

l[2]=7.5
print(l,"l is a type of ",type(l))

t=(5,'Hello',7.5)
# t[1]=30 wont work because t is immutable 
# and cant change, however lists can
print(t,"t is a type of ",type(t))

d={
    'course_name':'Python',
    'course_duration':'2 Months'
}
print(d, "d is a type of ",type(d))

s={10,20,30,10}
print(s, "s is a type of",type(s))

p=eval(input("Enter your Value1:= "))
q=eval(input("Enter your Value1:= "))

print(p+q)
r = int(p+q)

u = int(r+a)
print (u)
