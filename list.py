l = [1, 2, 3, [4, 5, 6]]
print (l)
print(type(l))
print (l[3][1])

m = [2, 3, "Hello", [3, 4, 5]]
print(m)
print(m[2])
print(m[1:3])
print(m[2:])

n=[10, 20, 30, 40, 50, 60]
print(n)
print(n[0::2])
print(n[-1::-1])

t = len(n)
print(t)
for a in range (t):
    print(n[a])

for a in range(t-1, -1, -1):
    print(n[a])

for b in n:
    print(b)

o=[]
for s in range(1, 101):
    o.append(s)
print(o)

r = [e for e in range(1,101)]
print(r)

x = [f for f in range(1,101) if f%2==0]
print(x)

i=[25, 50, 75, 100, 125]
del i[1]
print(1)

i.pop(2)
print(i)

print(i.pop(2))
print(i)

i.remove(75)
print(i)

i.clear()
print(i)

j = [20,30, 30, 30, 40,50,60]
j[0]=80
print(j)

j.insert(0,5)
print(j)

j.append(70)
print(j)

k=[230,250, 270]
j.append(k)
print(j)

j.extend(k)
print(j)

c = j.count(30)
print(c)

d=max(j)
print(d)

e=['Hello', 'Cello', 'Dhillon', 'Millon', 'Nallo']
print(e)
f=min(e)
print(f)

g=max(j)
print(g)

for v, g in zip(i,j):
    print(v,g)