import sys

total = 1
for argument in sys.argv:
    try:
        number = int(argument)
        total *= number
    except:
        pass

print(total)

'''
total = 1
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = int(argument)
        total *= number
    except Exception as e:
        print(e)
        print("Only numbwea can be provided")
        sys.exit(1)

print(total)
'''