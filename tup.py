t=(10,20,30,30,40,60,30)

print(t)
print(type(t))

n=t[3]
print(n)

l=len(t)

for a in range(l):
    print(a)
    print(t[a])

for b in t:
    print(b)

mm=min(t)
m=max(t)
c=t.count(30)
i=t.index(30)
s=sum(t, 10) # t + 10

print(m,mm,c, i, s)