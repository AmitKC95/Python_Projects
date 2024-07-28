import random
l=["Rock","Paper","Scissor"]

while True:
    PCCount=0
    userCount=0
    userChoice=int(input('''
Rock Paper Scissor - Go! 
Game Start 1 Yes
           2 No  | EXIT
           
                 '''))
    if userChoice==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock                                
2 Paper                                
3 Scissor                                
                                '''))
            if userInput==1:
                userChoice="Rock"
            elif userInput==2:
                userChoice="Paper"
            elif userInput==3:
                userChoice="Scissor"
            PCChoice=random.choice(l)
            if PCChoice==userChoice:
                print("Your Value", userChoice)
                print("Computer Value", PCChoice)
                print("Game Draw")
                userCount=userCount+1
                PCCount=PCCount+1
            elif (userChoice=="Rock" and PCChoice=="Scissor") or (userChoice=="Paper" and PCChoice=="Rock") or (userChoice=="Scissor" and PCChoice=="Paper"):
                print("Your Value", userChoice)
                print("Computer Value", PCChoice)
                print("You Win")
                userCount=userCount+1
            else:
                print("Your Value", userChoice)
                print("Computer Value", PCChoice)
                print("Computer Win")
                PCCount=PCCount+1
        if userCount==PCCount:
            print("Final Game Draw")
            print("Your Score", userCount)
            print("Computer Value", PCCount)
        elif userCount>PCCount:
            print("Final Game, You win the Game")
            print("Your Value", userCount)
            print("Computer Value", PCCount)
        else:
            print("Final Game, You loose the Game")
            print("Your Value", userCount)
            print("Computer Value", PCCount)
            
            
    else:
        break
            
            
         