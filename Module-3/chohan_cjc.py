"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

Modified by: C.J. Craig
Course: CSD-325, Module 3
Changes:
  1. Input prompt changed to 'cjc:' (initials).
  2. House fee increased from 10% to 12%.
  3. Added notice in intro: rolling a 2 or 7 earns a 10 mon bonus.
  4. Added bonus logic: if dice total is 2 or 7, player receives 10 mon bonus.
  5. Added inline comments documenting all modifications.
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

*** BONUS NOTICE: If the dice total is 2 or 7, you receive a 10 mon bonus! ***
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # CHANGE 1: Prompt changed from '> ' to 'cjc: ' (initials per assignment)
        pot = input('cjc: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        # CHANGE 1 (continued): Prompt changed to initials format here as well
        bet = input('cjc: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # CHANGE 4: Check if the dice total is 2 or 7 for the 10 mon bonus
    diceTotal = dice1 + dice2
    if diceTotal == 2 or diceTotal == 7:
        print(f'The dice total is {diceTotal} -- Lucky roll! You receive a 10 mon bonus!')
        purse = purse + 10  # Add the 10 mon bonus to the player's purse

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot to player's purse.
        # CHANGE 2: House fee changed from 10% (pot // 10) to 12% (pot * 12 // 100)
        houseFee = pot * 12 // 100
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee  # The house fee is now 12%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
