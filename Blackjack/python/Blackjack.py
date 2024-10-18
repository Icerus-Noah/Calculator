import random

ReferenceDeck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
]
print('Welcome to Blackjack!\nThe goal is to get as close to 21 as possible without going over.')

DealerWins = 0
PlayerWins = 0

GameRestart = False
HasStood = False
Betting = False

while True:
    if not Betting:
        Bet = input('Would you like to bet? (yes/no): ')
        if Bet == 'yes':
            BetValue = int(input('How much would you like to bet: '))
            Betting = True
        else:
            Betting = True
    if not GameRestart:
        DeckOfCards = ReferenceDeck.copy()
        random.shuffle(DeckOfCards)
        PlayersHand, DealersHand = [], []
        PlayersHand.append(DeckOfCards.pop())
        PlayersHand.append(DeckOfCards.pop())
        DealersHand.append(DeckOfCards.pop())
        DealersHand.append(DeckOfCards.pop())
    if not HasStood:
        GameRestart = True
        print(f'Your hand: {PlayersHand} (Total:{sum(PlayersHand)})')
        HitStand = input('Do you want to hit or stand? ').lower()
        if HitStand == 'hit':
            PlayersHand.append(Draw := DeckOfCards.pop())
            print(f'You drew a {Draw}')
            if PlayersHand.count(11) > 0:
                if sum(PlayersHand) > 21:
                    PlayersHand.remove(11)
                    PlayersHand.append(1)
                else:
                    continue    
            if sum(PlayersHand) > 21:
                DealerWins += 1
                if Bet == 'yes':
                    BetValue = 0
                    Betting = False
                    print(f'Your total bet is {BetValue}')
                PlayAgain = input(f'BUST, YOU LOSE\nPlayer wins {PlayerWins}\nDealer wins {DealerWins}\nDo you want to play again? (yes/no): ').lower()
                GameRestart = False
                if PlayAgain == 'no':
                    break                 
        elif HitStand == 'stand':
            HasStood = True
    if HitStand == 'stand':
        print(f'Dealer\'s hand: {DealersHand} (Total:{sum(DealersHand)})')
        if sum(DealersHand) < 17:
            DealersHand.append(Draw := DeckOfCards.pop())
            print(f'Dealer hits and draws a {Draw}')
            if DealersHand.count(11) > 0:
                if sum(DealersHand) > 21:
                    DealersHand.remove(11)
                    DealersHand.append(1)
        elif sum(DealersHand) > 21:
            HasStood = False
            PlayerWins += 1
            if Bet == 'yes':
                    BetValue = BetValue * 2
                    print(f'Your total bet is {BetValue}')
            PlayAgain = input(f'Dealer Bust, YOU WIN\nPlayer wins {PlayerWins}\nDealer wins {DealerWins}\nDo you want to play again? (yes/no): ').lower()
            GameRestart = False
            if PlayAgain == 'no':
                break 
        else:
            if sum(DealersHand) > sum(PlayersHand):
                DealerWins += 1
                print('Dealer has won!!!!')
                if Bet == 'yes':
                    BetValue = 0
                    Betting = False
                    print(f'Your total bet is {BetValue}')
            elif sum(DealersHand) < sum(PlayersHand):
                PlayerWins += 1
                print('Player has won!!!!')
                if Bet == 'yes':
                    BetValue = BetValue * 2
                    print(f'Your total bet is {BetValue}')
                
            elif sum(DealersHand) == sum(PlayersHand):
                print('Game is a tie')
            HasStood = False
            GameRestart = False
            PlayAgain = input(f'Player wins {PlayerWins}\nDealer wins {DealerWins}\nDo you want to play again? (yes/no): ').lower()
            if PlayAgain != 'yes':
                continue
