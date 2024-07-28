l=[10,20,30]
print(l)

ss=set(l)
print(ss)

s={10,20,30, 40, 50, 60}
print(s)

s.add(40)
s.add(70)
print(s)

s.remove(50) # If no item to remove exists, error will come
print(s)

s.discard(40) # If no item to remove exists, error will NOT come
print(s)

s.pop() # randomly removes
print(s)

s.clear()
print(s)

s.add(40)
print(s)

s.update(l)
print(s)

s.update({50})
print(s)

for a in s:
    print(a)