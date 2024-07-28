d={
    'Name':'Python',
    'Fees':8000,
    'Duration':'2 Months'
    }

print(d)
print(type(d))

f=d['Fees']
print(f)

for n in d:
    print(n)
    print(d[n])

m = d.get('Name')
print(n)

for a in d.keys():
    print(a)

for b in d.values():
    print(b)

for a,b in d.items():
    print(a,b)

for index, (key, value) in enumerate(d.items(), start=1):
    print(f"{index}. {key} - {value}")

del d['Fees']
print(d)

p=d.pop('Name')
print(p)
print(d)

c=d.get('Duration')
c1=d['Duration']
print(c, c1)

e=dict(name='Machine Learning', Fees=12000, Duration='8 Weeka')
print(e)

e.update({'Duration':'2 Months'})
e.update({'name':'Course'})
print(e)

e.update({'name':'Course'})
e.update({'Course':'Machine Learning'})
print(e)

del e['Course']
e['Name'] = 'Machine Learning'
del e['name']
print(e)

e = {'Name': 'Machine Learning', **e}
print(e)

e['Desc']="Machine Learning Course for Beginners"
e['Fees']=10000
print(e)

Course={
    'PHP':{'Duration':'2 Months','Fees':'8999'},
    'Python':{'Duration':'2 Months','Fees':'11999'},
    'Java':{'Duration':'2 Months','Fees':'13999'}    
}
print(Course)
print(Course['PHP'])

Course['Java']['Fees']=15000

for k,v in Course.items():
    # print(k,v)
    print(k,v['Duration'],v['Fees'])