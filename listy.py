l=[10,20,30,40]
l1=[11,22,33,44,55]

t = len(l)

for a,b in zip(l,l1):
    print(a,b)

for h in range(t):
    print(l[h],l1[h])


n=input("Enter The Value")
print(n)





l = []
print(l)

l = ['apple', 'pizza', 'shawarma', 'patties', 'chowmien']

print(len(l))

print(l[0])
print(l[2])
print(l[4])

mixed_data_types = ['Amit', 29, '165cms', 'Married', '167/11, artap Nagar, Gurgaon']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
print(it_companies)

Num_of_comp = len(it_companies)
print(Num_of_comp)

First = it_companies[0]
Middle = it_companies[len(it_companies) // 2-1]
last = it_companies[-1]
print(First, Middle, last)

it_companies[0] = 'Nvidia'
it_companies[2] = 'OpenAi'

it_companies.append('Oracle')
it_companies.append('Infosys ' 'Zerodha')

print(len(it_companies))
it_companies.insert(4, 'Sun Microsystems')

it_companies[0] = 'NVIDIA'
print(it_companies)

S = f"# {it_companies}"
print(S)

exis = 'NVIDIA' in it_companies
print(exis)

it = ['NVIDIA', 'Google', 'OpenAi', 'Apple', 'Sun Microsystems', 'IBM', 'Amazon', 'Oracle', 'Infosys', 'Zerodha']
print(it)
srt = it.sort()
print(it)
srt = it.sort(reverse=True)
print(it)

it_Start3 = it[:3]
print(it_Start3)

del it[0]
print(it)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index('Redux')+ 1, 'Python')
full_stack.insert(full_stack.index('Python')+ 1, 'SQL')
print(full_stack)





'''Fruits = ('Pineapple', 'Strawberry', 'Papaya')
Vegetables = ('Eggplant', 'Cauliflower', 'Okra')
Animal = ('Sheep', 'Goat', 'Elephant')

Food_Stuff = Fruits + Vegetables + Animal
print(Fruits, Vegetables, Animal)
print(Food_Stuff)

FSL = list[Food_Stuff]
print(FSL)

FS_length = len(Food_Stuff)

FS_1st3 = Food_Stuff[:3]
print(FS_1st3)
FS_L3 = Food_Stuff[-3:]
print(FS_L3)

mid = FS_length // 2
if FS_length % 2 == 0:
  mid_num = Food_Stuff[mid-1:mid+1]
else:
  mid_num = [Food_Stuff[mid]]
print(mid_num)

del Food_Stuff'''

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''if 'Estonia' in nordic_countries:
  print("True")
else:
  print('False')

if 'Iceland' in nordic_countries:
  print("True")
else:
  print('False')'''
  
print('True' if 'Estonia' in nordic_countries else 'False')
print('True' if 'Iceland' in nordic_countries else 'False')

'''
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
countries_to_check = ['Estonia', 'Iceland']
for country in countries_to_check:
    print('True' if country in nordic_countries else 'False')

'''

