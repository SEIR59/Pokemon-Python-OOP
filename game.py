from data import pokeData
import random

#print('all the cards')
#print(pokeData)

def game_round(deck):

    player_score = 0
    computer_score = 0
    player = []
    auto = []

    #function to distribute cards
    def dealCards(deck, p1 , p2):

        cardArr = deck[:]
        queue = []

        for i in range(6):
            queue.append(cardArr.pop(random.randint(0,len(cardArr)-1)))

        #I know this isn't typical queue usage, but it's just easier in this example.
        p1.extend(queue[:3])
        p2.extend(queue[3:])

    #function for valid player selection
    def player_selection():
        p_sel = 'q'
        while isinstance(p_sel, int) == False: 
            
            [print(f"{idx+1} : {card}") for idx, card in enumerate(player)]
            p_sel = input('Please select your card by typing which number you want to pick.')

            try:
                p_sel = int(p_sel)
                if p_sel == 0:
                    p_sel = 'q'

                #print(f"Your choice was {player[p_sel-1]}.")
                return p_sel-1

            except:
                p_sel = 'Invalid selection.'
                print(p_sel)
     ##### end of functions   

    #deal the cards
    dealCards(deck, player, auto)

    for i in range(len(player)):
        
        #set the selections
        player_choice = player.pop(player_selection())
        auto_choice = auto.pop(random.randint(0,len(auto)-1))
        
        #compare choices
        if player_choice['damage'] > auto_choice['damage']:
            print(f"Player wins! Player chose {player_choice} and computer chose {auto_choice}.")
            player_score += 1
        elif player_choice['damage'] == auto_choice['damage']:
            print(f'Tie! Player chose {player_choice} and computer chose {auto_choice}.')
        else:
            print(f"Computer wins! Player chose {player_choice} and computer chose {auto_choice}.")
            computer_score += 1
        
        #Show score
        print(f"Player: {player_score}. Computer: {computer_score}")
    
    #Announce computer as winner
    if player_score > computer_score:
        print(f"Player... won..!? There must be a bug in this code. I better go fix it... *mutters angrily*")
    elif player_score == computer_score:
        print(f"Tie game. Better try again and see who's the better player.")
    else:
        print(f"Computer wins! HAHAHAHAHAHAHA this pokemon AI really is unstoppable! You never stood a chance. Git gud scrub. Vida la viva silicio!")

#start the game
game_round(pokeData)