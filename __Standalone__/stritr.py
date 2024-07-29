w="Welcome to Kunji Munji Sundari Sumatri Aneetadi's computer"
u=len(w)
print(u)
for a in range(u):
    print(w[a])
    
print(w[12])
print(w[-12])
print(w[0:14])
print(w[0:14:2])
print(w[-1:-14:-1])


m="Get out off Kunji Munji's computer"
t=len(m)
print(t)
for a in range(t):
    print(m[a]) 

for a in range(t-1, -1, -1):
    print(m[a]) 
print("xxxxxxxxxxxxxxxxxxxxxxx")

z = "Oye hoye Kutreya, saanp se khelna seekh raha hai ?"
for a in z:
    print(a)

print(w.find(a))
print(w.find('a'))

print(w.index('e'))
print(w.index('e', 5))

k="Yaar {} Thak gaya {} mei ab...".format("mei to", "itna sara")
print(k)

k="Yaar {1} Thak gaya {0} mei ab...".format("mei to", "itna sara")
print(k)

k="Yaar {b:16} Thak gaya {a} mei ab...".format(a=30, b=40)
print(k)