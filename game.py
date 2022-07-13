from data import pokeData
import random

print('all the cards')
print(pokeData)

player = []
auto = []

def dealCards(cards, p1 , p2):

    cardArr = cards[:]
    queue = []

    for i in range(6):
        queue.append(cardArr.pop(random.randint(0,len(cardArr)-1)))

    #I know this isn't typical queue usage, but it's just easier in this example.
    p1.extend(queue[:3])
    p2.extend(queue[3:])


def game_round(p1, p2):
    p_choice = 'q'

    while isinstance(p_choice, int) == False: 
        
        [print(f"{idx+1} : {card}") for idx, card in enumerate(player)]
        p_choice = input('Please select your card by typing which number you want to pick.')

        try:
            p_choice = int(p_choice)
            print(f"Your choice was {player[p_choice-1]}.")
        except:
            p_choice = 'Invalid selection.'
    
    pass

    

dealCards(pokeData, player, auto)
print('Player, auto')
print(player,auto)

game_round(player,auto)