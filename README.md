![GA logo](https://camo.githubusercontent.com/6ce15b81c1f06d716d753a61f5db22375fa684da/68747470733a2f2f67612d646173682e73332e616d617a6f6e6177732e636f6d2f70726f64756374696f6e2f6173736574732f6c6f676f2d39663838616536633963333837313639306533333238306663663535376633332e706e67)

# OOP Pokemon

<hr>

Title: Pokemon Game<br>
Type: Lab/HW<br>
Creator: WDI-Archer, WDI-Funke <br>
Adapted + Modified by: Jim Haff and Reuben Ayres then adapted Doireann Herold for Python Version<br>
Topics: Using objects, the keyword `self` and methods to create a game while focusing on OOP, array filter<br>

<hr>

![pokemon cards](https://i.ytimg.com/vi/5pDthGSHo58/maxresdefault.jpg)

<hr>


## Object Oriented Programming
We're going to continue using objects, giving them data and behaviors (methods). They will interact with one another to make our game work!

## The basic idea

You are going to create a simple card game in which a player will be able to battle the autoplayer.  The game will deal 3 cards (each of which has a damage value) to the player and three cards to the autoplayer.  The player will choose a card, and the computer will randomly choose a card, and whichever's card has the highest value will win the point.  A round is finished once this has happened three times. 


## The Cards

Here is the LIST of cards.  Instructions below.

```python
[
  {
    'name': "Bulbasaur",
    'damage': 60
  }, {
    'name': "Caterpie",
    'damage': 40
  }, {
    'name': "Charmander",
    'damage': 60
  }, {
    'name': "Clefairy",
    'damage': 50
  }, {
    'name': "Jigglypuff",
    'damage': 60
  }, {
    'name': "Mankey",
    'damage': 30
  }, {
    'name': "Meowth",
    'damage': 60
  }, {
    'name': "Nidoran - female",
    'damage': 60
  }, {
    'name': "Nidoran - male",
    'damage': 50
  }, {
    'name': "Oddish",
    'damage': 40
  }, {
    'name': "Pidgey",
    'damage': 50
  }, {
    'name': "Pikachu",
    'damage': 50
  }, {
    'name': "Poliwag",
    'damage': 50
  }, {
    'name': "Psyduck",
    'damage': 60
  }, {
    'name': "Rattata",
    'damage': 30
  }, {
    'name': "Squirtle",
    'damage': 60
  }, {
    'name': "Vulpix",
    'damage': 50
  }, {
    'name': "Weedle", 
    'damage': 40
  }
]
```

## Example Play

- There are 18 Pokemon cards in the deck
- Eggbert (the player) is dealt three random cards from the deck
- The computer is dealt three random cards from the deck
- Eggbert chooses a card and plays it! It has a damage of 10.
- The computer randomly chooses a card and plays it! It has a damage of 8.
- Eggbert wins!

The score is displayed: 
- Score: Eggbert: 1, Computer: 0
- Rounds Won: Eggbert: 0, Computer: 0

They do this again two more times. 
The round ends.

The score is displayed.
The rounds won are displayed.


## The `game` class/object

For each part, think about:
* What's the best data type for this property? Number? String? List? Dictionary? boolean? Some crazy combination of these).  
  * Hint/reminder: use a property when you want to "keep track" of something
* Or should you create a method?
  * Hint/reminder: use a method when you want to "do" something

#### The game should be able to:

1. keep a library of all the Pokemon cards that can be played (see the array in the "The Cards" section)
2. know what cards have been played
3. know how many cards are left to be played/dealt overall (Include a graveyard for played cards)
4. track points for both the player and the computer
    Note: Points are determined by the following: If the player's card beats the computer's card, the player gets one point (and vice versa). If there is a tie, no one gets a point.
5. track rounds
6. track number of rounds won for both player and computer
7. automatically deal 3 cards from the library to the player and 3 cards to the computer each round
8. determine the winner of each play
9. stop once there are no cards left or not enough to deal 3 to each the player and computer


## The `player` class/object

### The player should be able to:

1. see their stats: their points and how many rounds they've won.
2. see what cards they have been dealt/see what cards are left in their hand
3. pick a card from the hand that has been dealt to them (thereby playing this card agaist the computer's card). The round ends once this has happened 3 times.
4. receive new cards given to them by the game each round.
5. see the cards that they have played in the past.


## The "UI"

The user should see the following in the console:

- the scoreboard after each round
- the cards in the player's hand
- the cards in the computer's hand
- the cards that are in play
- the winner of each round (or if there was a tie)
- the winner of the game when the game is over 
- the final score when the game is over




# Hungry for More?  


## Expand your game

1. We'll start working with actual web pages in the next couple of days, but see if you can make the UI stuff display/update on the webpage somehow.
2. You could also: 
  * Display the past-played cards.
  * Style your cards to _actually look like cards_ and add an image to each.
  * Do other cool stuff!



## Practice List Methods, Remember to keep things simple, break it down, use print statements, get creative, games are funnn


It's a big list but that's ok. We got tools now to handle big lists. 
