from data import pokeData
import random

#print('all the cards')
#print(pokeData)

def game(deck):
    #function to distribute cards
    def dealCards():
        queue = []

        for i in range(6):
            queue.append(currDeck.pop(random.randint(0,len(currDeck)-1)))

        #I know this isn't typical queue usage, but it's just easier in this example.
        player['hand'].extend(queue[:3])
        computer['hand'].extend(queue[3:])
        pass

    #function for valid player selection
    def player_selection():
        p_sel = 'q'
        while isinstance(p_sel, int) == False: 
            
            [print(f"{idx+1} : {card}") for idx, card in enumerate(player['hand'])]
            
            #Intentionally leaving this out because it's totally cheating
            #cHand = [card for card in computer['hand']]
            #print(f"Computer has {cHand}")
            p_sel = input('Please select your card by typing which number you want to pick.')

            try:
                p_sel = int(p_sel)
                if p_sel == 0:
                    p_sel = 'q'
                print(f"Your choice was {player['hand'][p_sel-1]}.")
                return p_sel-1

            except:
                p_sel = 'Invalid selection.'
                print(p_sel)
     ##### end of functions   

    def game_round(round_num):

        #deal the cards
        print(f'All cards in the remaining deck before dealing - {currDeck}')
        dealCards()
        print(f'Round {round_num}... FIIIIGHT!')
        #scores mid round
        player_score = 0
        computer_score = 0

        for i in range(len(player['hand'])):
            
            #set the selections
            player_choice = player['hand'].pop(player_selection())
            player['past'].append(player_choice)
            computer_choice = computer['hand'].pop(random.randint(0,len(computer['hand'])-1))
            computer['past'].append(computer_choice)
            
            #compare choices
            if player_choice['damage'] > computer_choice['damage']:
                print(f"Player wins! Player chose {player_choice} and computer chose {computer_choice}.")
                player_score += 1
            elif player_choice['damage'] == computer_choice['damage']:
                print(f'Tie! Player chose {player_choice} and computer chose {computer_choice}.')
            else:
                print(f"Computer wins! Player chose {player_choice} and computer chose {computer_choice}.")
                computer_score += 1
            
            #Show score
            print(f"Player: {player_score}. Computer: {computer_score}")
        
        #Announce computer as winner
        if player_score > computer_score:
            print(f"Player... won..!? There must be a bug in this code. I better go fix it... *mutters angrily*")
            return False
            
        elif player_score == computer_score:
            print(f"Tie game. Better try again and see who's the better player.")
        else:
            print(f"Computer wins! HAHAHAHAHAHAHA this pokemon AI really is unstoppable! You never stood a chance. Git gud scrub. Vida la viva silicio!")
            return True
            
        pass
    
    player_wins = 0
    computer_wins = 0
    currDeck = deck[:]
    player = {
        'hand':[],
        'past':[]
    }
    computer = {
        'hand':[],
        'past':[]
    }
    print(f'I have player wins and computer wins{player_wins} , {computer_wins}')

    for i in range(int(len(deck)/6)):
        print(f"Player has played {player['past']} and computer has played {computer['past']}")
        if game_round(i+1) == True:
            computer_wins += 1
        else:
            player_wins += 1

    print(f"Final score! Player {player_wins}. Computer {computer_wins}.")
    if player_wins > computer_wins:
        print(f"You clearly cheated. There's literally no other explanation. You don't just BEAT a highly advanced Pokemon player MASTERMIND, such as myself! How much are you paying whoever's helping you? I'll double it...")
    elif player_wins == computer_wins:
        print(f"You should be proud to have fought against the best and come out with a tie. This is truly a feat you should be proud of, human.")
    else:
        print(f"I'd say that in the end it became clear who was the best duelist between us, but that was known before we ever even started, now, wasn't it? HA! Try me again, if you dare.")

#start the game
game(pokeData)