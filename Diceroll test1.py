import random

def main():
#player 1 variables
    name1=input('player 1 what is your name? ')
    player1R1=0
    player1R2=0
    player1total=0
    player1points=0
    rounds=1
    while rounds !=6:
        print('!!!!!!!!!!!!!!!!!!!!!Round '+str(rounds)+'!!!!!!!!!!!!!!!!!!!!!')
        rounds=rounds+1
#player 1 half
        player1R1=DiceROLL()
        player1R2=DiceROLL()
        print('.....................'+name1+'.........................')
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
        
    
def DiceROLL():
    diceroll = random.randint(1,6)
    return diceroll

main()
