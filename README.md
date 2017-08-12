# README<br>For Fight the Landlord card game<br>Brought by Frank and Jones         
This README is writren by Jones LeBron and modified by Frank.        
        
## What is this?        
For our final project, we made a traditional Chinese card game, called Fight the Landlord. The name is based on Land Reform Movement raised by China Communist Party from 1950 to 1953. This game is really popular in China mainland, especially during the Spring Festival — the Chinese new year, when family members gather together and have reunion, this card game is one important entertainment activity. There are many different "modes"(rules) for Fight the Landlord in different areas in China, like "sky ground laizi" mode or 4-player mode, but in our program, we made the classic version.        
Here are some basic rules for the game:         
It is a three-player game, landlord, who has 20 cards versus two farmers who has 17 cards each.          
Everyone can only see his（her) own cards, even the two farmers are teammate, they cannot see each other’s cards or talk about what to hand, but sophisticated player to predict other’s cards.        
If the landlord hands all his(her) cards first, he(she) wins and the two farmers lose; if any of the farmers hands all his(her) cards, both two framers win equally, and the landlord loses.        
        
# Environment requirement and portability
This program is programed in Python 3.5.3, GCC 6.3.0 20170118 using Ubuntu 17.04 zesty. Do keep in mind that some features does not support non-POSIX systems, such as Microsoft Windows.  
What? You don't have any POSIX system? Get one! It's good for you.   
For OS X users, be sure afplay can be executed by Terminal. For Linux users, be sure aplay is available.   
For Windows users, if you want to hear the background music, you may modify sond.py by adding os.system("start BGM.wav").   
This program requires no additional external library.   
Proudly using VIM to edit all py files.        

# To run this program
Simply type python3 main.py in your terminal.

# Dos and donts
Dos:  
- Play the game happily
- Press ENTER if it's not your turn to hand and something else appeared.
Donts:
- Input strange things that may crash the program.

# Implementation        
Here are a step by step cycle for a whole Fight the Landlord game:        
Shuffles all 54 cards; (On program level, we made a function called “shuffle”, which takes a new set of cards(A,A,A,A,2,2,2,2,......,3,3,3,3, joker, JOKER）as input, and shuffle it using random.random(), then output.        
        
Gives cards to players, each player get 17 cards at first, and the last three cards are called “landlord card”, which decides who the landlord is.the first player get the first 17 cards of the shuffled cards(its supposed to be like player number one get the first card and player number two get the second card, player number three get the third card and player number one get the forth card when played in reality, but the shuffle function is really great, so this is OK);(On program level, we made a function called handOut().         
        
 Decide the landlord, start from player number one, ask him(her) if he want to be the landlord(if his(her) cards are good enough to against two), if he(she) wants, he(she) gets the three cards and become the landlord, else ask player number two, if he(she) does not want, ask player number three ;        
        
The landlord hands card first, and the cards must be one of “cardtype”,         
        
the player on the landlord’s right hand(counter clockwise) has to hand cards that output true for function “legal”  or he(she) choose “not to hand”         
If one player choose “not to hand”, the last player (the one one his left hand) can hand any cards that is one of “cardtype”, and the next player has to hand cards that output true for function “legal”  or he(she) choose “not to hand” .         
Repeat 6.7        
When anyone hands out all his(her) cards, the game over.        
        
#Simple introduction        
Cardtype():        
The function that input a list of cards (numbers), can return false if the cards does not fit any of card types, and return the card type of those cards:        
Card types:        
Single: a single card like3        
Pair: two cards that have same value like 3,3        
Triple: three cards that have same value like 3,3,3        
Bomb: four cards that have same value like ,3,3,3,3        
Rocket: Two jokers.
3+1: three cards that have same value and one single  like 3,3,3,4        
Fullhouse :three cards that have same value and one pair like 3,3,3,4,4        
4+2:  four cards that have same value and one pair like 3,3,3,3,4,4        
Straight: straight singles like 3,4,5,6,7,8,9        
Straight 2: straight pairs like 3,3,4,4,5,5,6,6,7,7        
Airplane: straight triples for example 3,3,3,4,4,4        
Airplane with small: straight 3+1s like 3,3,3,4,4,4,5,5,5,6,8,J        
Airplane with big: straight full houses like 3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,9,9,J,J        
        
#Further Reading        
You can find whole rules [here](https://en.wikipedia.org/wiki/Dou_dizhu).         
Do keep in mind that since "spaceshuttle" is too rare, we did not implement this handing.        
