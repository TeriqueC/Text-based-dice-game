import random
def main():
#player 1 variables
    name1=input('player 1 what is your name? ')
    player1R1=0
    player1R2=0
    player1total=0
    player1points=0
    rounds=1
#player 2 variables
    name2=input('player 2 what is your name? ')
    player2R1=0
    player2R2=0
    player2total=0
    player2points=0
    while rounds !=6:
        print('!!!!!!!!!!!!!!!!!!!!!Round '+str(rounds)+'!!!!!!!!!!!!!!!!!!!!!')
        rounds = rounds+1
#player 1 half
        print('.....................'+name1+'.........................')
        keypressed=input(name1+' to roll the dice PRESS ANY KEY: ')
        player1R1=DiceROLL()
        player1R2=DiceROLL()
        print(name1+' first roll: '+str(player1R1))
        print(name1+' second roll: '+str(player1R2))
        player1total=player1R1+player1R2
        print(name1+' total: '+str(player1total))
        player1= int(str(player1total))
        if (player1 % 2) == 0:
            print(str(player1total)+' is even '+name1+' gets 10 points'.format(player1))
            player1points=player1points+10
            print(name1+' points: '+str(player1points))
        else:
            print(str(player1total)+' is odd '+name1+' loses 5 points'.format(player1))
            if player1points==0:
                player1points=player1points+0
                print(name1+' points: '+str(player1points))
            else:
                player1points=player1points-5
                print(name1+' points: '+str(player1points))
#player 2 half
        print('.....................'+name2+'.........................')
        keypressed=input(name2+' to roll the dice PRESS ANY KEY: ')
        player2R1=DiceROLL()
        player2R2=DiceROLL()
        print(name2+' first roll: '+str(player2R1))
        print(name2+' second roll: '+str(player2R2))
        player2total=player2R1+player2R2
        print(name2+' total: '+str(player2total))
        player2= int(str(player2total))
        if (player2 % 2) == 0:
            print(str(player2total)+' is even player 2 gets 10 points'.format(player2))
            player2points=player2points+10
            print(name2+' points: '+str(player2points))
        else:
            print(str(player2total)+' is odd player 2 loses 5 points'.format(player2))
            if player2points==0:
                player2points=player2points+0
                print(name2+' points: '+str(player1points))
            else:
                player2points=player2points-5
                print(name2+' points: '+str(player2points))         
#winner is declared
        if player1points>player2points:
            print(name1+' wins with '+str(player1points))
            print(name2+' loses with '+str(player2points))
        elif player1points==player2points:
            print('it is a draw')
            print(name1+' points: '+str(player1points))
            print(name2+' points: '+str(player2points))
        else:
            print(name2+' wins with '+str(player2points))
            print(name1+' loses with '+str(player1points))
def DiceROLL():
    diceroll = random.randint(1,6)
    return diceroll
main()
