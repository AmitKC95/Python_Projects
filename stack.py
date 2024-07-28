l=[]
while True:
    c=int(input('''
            1 Push Elements
            2 Pop Elements
            3 Peek Element
            4 Display Stack
            5 Exit    
                '''))
    
    if c==1:
        n=input("Enter the Value")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("You have an Empty Stack! Enter your list values")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("You have an Empty Stack! Enter your list values")
        else:
            print("Last Stack Value",l[-1])
    elif c==4:
        print("Display Stack", l)
    elif c==5:
        break
    else:
        print("Invalid Option. Try from Range 1-5")