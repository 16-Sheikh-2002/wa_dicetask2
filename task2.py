#Note1: Finish Output file rule in flowgorithm - not possible
from random import randint
import time
saveFile = open('F:\Documents\exampleFile.txt','w')
saveFile.write("(Round, Player, Total of Dice):\n")
pass1 = "Sheikh"
pass2 = "Haroon"
player1 = input("Player 1, enter your name (Case sensitive): ")
player2 = input("Player 2, enter your name (Case sensitive): ")
point1 = 0
point2 = 0
#Authorisation code below:
if (player1 == pass1 or player1 == pass2) and (player2 == pass2 or player2 == pass1):
    print("\nAuthorised!")
    time.sleep(1)
    print("Welcome",player1,"&",player2,"\n")
    print("You have 5 rounds to throw two dice...")
    print("If you get an even total you recieve 10 points!\nHowever if you get an total number, you lose 5 points!\nBoth players start with 0 points and whoever gets the higher total wins!\n")
    time.sleep(2)
    ready1 = input("Player 1 are you ready?:(y/n} ")
    ready2 = input("Player 2 are you ready?:(y/n} ")
    if ready1 == "y" and ready2 == "y":
        print("\nGreat! Let's Begin!")
        print(player1,"First! Then",player2)
    else:
        while ready1 != "y" or ready2 != "y":
            ready1 = input("Player 1 are you ready?:(y/n} ")
            ready2 = input("Player 2 are you ready?:(y/n} ")
    #ends: Authorisation code
    round = 0
    while round < 5:
        round = round + 1
        print("\nRound",round,": -------------------\n")
        time.sleep(0.5)
        #Player 1 code:
        p1d1 = int(randint(1, 6))
        p1d2 = int(randint(1, 6))
        total1 = 0
        total1 = p1d1 + p1d2
        if total1 == 2 or total1 == 4 or total1 == 6 or total1 == 8 or total1 == 10 or total1 == 12:
            point1 = point1 + 10
        else:
            point1 = point1 - 5
        if point1 < 0:
            point1 = 0
        print("Rolling die for",player1,"...")
        print("The numbers are",p1d1,"&",p1d2)
        print("The total of those numbers were",total1)
        print("So far",player1,"has",point1,"points!\n")
        #Doubles rule for player 1:
        if p1d1 == p1d2:
            while p1d1 == p1d2:
                print("\nBecause Player 1 rolled a double, Player 1 recieves an additional throw!")
                p1d1 = int(randint(1, 6))
                p1d2 = int(randint(1, 6))
                total1 = 0
                total1 = p1d1 + p1d2
                if total1 == 2 or total1 == 4 or total1 == 6 or total1 == 8 or total1 == 10 or total1 == 12:
                    point1 = point1 + 10
                else:
                    point1 = point1 - 5
                if point1 < 0:
                    point1 = 0
                print("Rolling die for",player1,"...")
                print("The numbers are",p1d1,"&",p1d2)
                print("The total of those numbers were",total1)
                print("So far",player1,"has",point1,"points!\n")
        #Doubles rule finishes for P1
        #end Player1, starts: Player2 code:
        p2d1 = int(randint(1, 6))
        p2d2 = int(randint(1, 6))
        total2 = 0
        total2 = p2d1 + p2d2
        if total2 == 2 or total2 == 4 or total2 == 6 or total2 == 8 or total2 == 10 or total2 == 12:
            point2 = point2 + 10
        else:
            point2 = point2 - 5
        if point2 < 0:
            point2 = 0
        print("Rolling die for",player2,"...")
        print("The numbers are",p2d1,"&",p2d2)
        print("The total of those numbers were",total2)
        print("So far",player2,"has",point2,"points!")
        time.sleep(2)
        #Doubles rule for player 2:
        if p2d1 == p2d2:
            while p2d1 == p2d2:
                print("\nBecause Player 2 rolled a double, Player 2 recieves an additional throw!")
                p2d1 = int(randint(1, 6))
                p2d2 = int(randint(1, 6))
                total2 = 0
                total2 = p2d1 + p2d2
                if total2 == 2 or total2 == 4 or total2 == 6 or total2 == 8 or total2 == 10 or total2 == 12:
                    point2 = point2 + 10
                else:
                    point2 = point2 - 5
                if point2 < 0:
                    point2 = 0
                print("Rolling die for",player2,"...")
                print("The numbers are",p2d1,"&",p2d2)
                print("The total of those numbers were",total2)
                print("So far",player2,"has",point2,"points!")
        #Writes round results to file
        if total1 > total2:
            higher = (str(total1))
            roundstr = (str(round))
            filetext = (roundstr, player1, higher)
            saveFile.write(str(filetext))
            saveFile.write("\n")
        elif total2 > total1:
            higher = (str(total2))
            roundstr = (str(round))
            filetext = (roundstr, player2, higher)
            saveFile.write(str(filetext))
            saveFile.write("\n")
        elif total1 == total2 or total2 == total1:
            roundstr = (str(round))
            same = (roundstr,"was a draw")
            filetext = (same, total1)
            saveFile.write(str(filetext))
            saveFile.write("\n")
        #Round writing code ends
        if round == 5:
            print("\nFinished : ------------------")
        #Doubles rule finishes for P2

    #While loop ends:
    print("\nAt the end of 5 rounds, the total points for the players were:")
    print("Player 1:",point1)
    print("Player 2:",point2,"\n")
    #Displays winner:
    if point1 > point2:
        print("The winner is Player 1 which is "+player1+"!")
    elif point2 > point1:
        print("The winner is Player 2 which is "+player2+"!")

    if point1 == point2:
        print("It's a Draw, time for quick fire rounds!")

        #quickfire round starts - for draw: code below is asking if players are ready
        ready1 = input("Player 1 are you ready?:(y/n} ")
        ready2 = input("Player 2 are you ready?:(y/n} ")
        if ready1 == "y" and ready2 == "y":
            print("\nGreat! Let's Begin!")
            #Player first turn switches!!
            print(player2,"First! Then",player1)
        else:
            while ready1 != "y" or ready2 != "y":
                ready1 = input("Player 1 are you ready?:(y/n} ")
                ready2 = input("Player 2 are you ready?:(y/n} ")
        #ready code ends
        #bonus round starts - player 2 starts
        roundb = 0
        while point1 == point2:
            time.sleep(1)
            roundb = roundb + 1
            #p2
            p2d1 = int(randint(1, 6))
            p2d2 = int(randint(1, 6))
            p2 = p2d1 + p2d2
            if p2 == 2 or p2 == 4 or p2 == 6 or p2 == 8 or p2 == 10 or p2 == 12:
                point2 = point2 + 10
            else:
                point2 = point2 - 5
            if point2 < 0:
                point2 = 0
            print("\nQuickfire Round",roundb,": -------------------\n")
            print("Rolling die for",player2,"...")
            print("The numbers are",p2d1,"&",p2d2)
            print("The total of those numbers were",p2)
            print("So far",player2,"has",point2,"points!\n")
            #p1
            p1d1 = int(randint(1, 6))
            p1d2 = int(randint(1, 6))
            p1 = p1d1 + p1d2
            if p1 == 2 or p1 == 4 or p1 == 6 or p1 == 8 or p1 == 10 or p1 == 12:
                point1 = point1 + 10
            else:
                point1 = point1 - 5
            if point1 < 0:
                point1 = 0  
            print("\nRolling die for",player1,"...")
            print("The numbers are",p1d1,"&",p1d2)
            print("The total of those numbers were",p1)
            print("So far",player1,"has",point1,"points!\n")
            time.sleep(2)
        #Quickfire round finishes
    #Code below shows final winner
    if point1 > point2:
        print(player1,"Wins!")
        winner =(player1, point1)
        print(winner)
        
    else:
        print(player2,"Wins!")
        winner = (player2, point2)
        print(winner)

    #Save file code begins:
    text = (winner)

    saveFile.write("\n")
    saveFile.write("The winner (with the most points) is:\n")
    saveFile.write(str(winner))
    saveFile.close()
    #Code finishes
            

#Authorisation code:
else:
    print("Error 403: Forbidden!")


#Code 8298
