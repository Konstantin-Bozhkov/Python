
"""
Tip 1:
To check import paths, you can place the following code inside Python Shell
>> import sys;
>> sys.path;
"""

"""
Python BlackJack implementation
"""

from random import shuffle;

def say(msg):
    print(msg);

def say_welcome(player = "Player"):
    say("Hello %s and Welcome to our Casino" % player);


def init_shoe(num_decks = 1):
    #Generate a shuffle lists of cards from num_deck number of decks
    suits = ['s','h','d','c'];
    ranks = ['J','Q','K','A'] + [ str(i) for i in range(2,11) ]; 
    cards = [ x + y for x in ranks for y in suits] * num_decks;
    # Check if cards length is num_decks * 52
    assert len(cards) == num_decks * 52;
    # Build in python function
    shuffle(cards);
    print( "Shuffle %s cards into the dealer shoe. Good luck!" % cards );
    return cards;


def hand_score(hand):
    # Doctest in Linux 
    # $ python -m doctest -v blackjack.py
    """
    >>> hand_score(['As','Js'])
    21
    >>> hand_score(['As','Ah','Ad'])
    13
    >>> hand_score(['As','Ah','Ad','10c']) # All aces are now counted as 1 point
    13
    >>> hand_score(['Qs','2s','3h','4c'])
    19
    >>> hand_score(['10s','2c','10c'])
    22
    """
    
    score  = 0;
    aces = 0;
    for card in hand:
        # if the first char is digit
        if card[0].isdigit():
            score += int(card[:-1]); # take out last char, so the output will always be a number 10a = 10; 2a = 2
        # if the first char is one of the letters
        elif card[0] in ('J','Q','K'):
            score +=10;
        elif card[0] == 'A':
            aces +=1;
        else:
            assert False, "Unvalid input";
    
    # All aces after the first one are counted as 1 points
    score += max([aces-1,0]) * 1;
    score += min([aces,1]) * (1 if score >= 11 else 11); 
    return score;

def deal_card(shoe):
    """
    >>> deal_card([2,3,4,5,6,7,8,9,10]);
    ([10, 9], [8]) #tupel
    """
    # take out 2 cards for the player and one for the dealer
    return [shoe.pop() for i in range(2)], [shoe.pop()];


def ask_for_bet(balance,min_bet):
    """
    Ask the player to bet some amount
    """
    while True:
        say("How much would you want to wager this time?");
        try:
            bet = input("I want to bet "); # Expect console user input.Display the message inside the brackets;
            bet = float(bet);
            if bet > balance:
                say("You don't have enough money on your account");
            elif bet < 0:
                say("Negative bets are not allowed you... cheater");
            elif bet < min_bet:
                say("Bet must be above %s" % min_bet);
            else:
                balance -= bet;
                say("Bet of %.2f accepted!" % bet);
                return bet,balance;
        except ValueError as e:
            say("%s is not a valid bet! Please enter a floating point number." % bet);

# If not main file dont run;
# Main function similar to C#
if __name__ == "__main":
    say_welcome();
    init_shoe(5);
    ask_for_bet(100,10);
     
    
 

