'''
A simplified BlackJack game
'''
class Player:
    '''
    Player class
    '''
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cards = []
        self.minsum = 0
        self.status = 'Play'

    def newgame(self):
        self.cards = []
        self.minsum = 0
        self.status = 'Play'
    
    def play(self, cards):
        while self.status == 'Play':
            playerchoice = input('Do you want a new card? y/n').lower()
            if playerchoice == 'y':
                self.hit(cards)
                print(self.cards)
            elif playerchoice == 'n':
                self.status = 'Stop'
                break
            else:
                playerchoice = input('Do you want a new card? y/n').lower()

    def dealerplay(self, cards, threshold = 17):
        while self.bestscore() < threshold:
            self.hit(cards)
            print(self.cards)
        else:
            self.status = 'Stop'

    def hit(self, cards):
        card = cards.pop(0)
        self.cards.append(card)
        if card <= 10:
            self.minsum += card
        else:
            self.minsum += 10
        if self.minsum > 21:
            self.status = 'Blust'
            print('Blust!')
        elif self.bestscore() == 21:
            self.status = 'Won'
            print('BlackJack!')
    
    def bestscore(self):
        if self.status == 'Blust':
            return 0
        currentbest = self.minsum
        aces = self.cards.count(1)
        for ace in aces:
            if currentbest + 10 == 21:
                return 21
            elif currentbest + 10 > 21:
                return currentbest
            else:
                currentbest += 10
        return currentbest

    def win(self, betamount):
        self.balance += betamount
    
    def lose(self, betamount):
        self.balance -= betamount
        if self.balance <= 0:
            print(f'Player {self.name} gets knocked out!')

class Board:
    def __init__(self, decks):
        self.decks = decks
        self.players = []
        self.cards = []
        self.betamount = 0
        self.addplayer(Player('Dealer', 0))

    def addplayer(self, player):
        self.players.append(player)
        print(f'Player {player.name} entered the game')
    
    def setbetamount(self, betamount = 1):
        self.betamount = betamount

    def shuffle(self):
        import random
        self.cards = list(range(1, 14))*self.decks
        random.shuffle(self.cards)    

    def play(self):
        self.showbalance()
        self.shuffle()
        for player in self.players[1:]:
            player.newgame()
            if len(self.cards) < 6:
                self.shuffle()
            print(f'Player {player.name}"s turn')
            player.play(self.cards)
        print('Dealer"s turn')
        self.players[0].dealerplay(self.cards)
        evaluate(self.players[0].bestscore())
        self.showbalance()

        def evaluate(self, dealerscore):
            if dealerscore == 21:
                print('Dealer gets BlackJack! All players lose')
            elif dealerscore == 0:
                print('Dealer gets blusted!')
            else:
                print(f'Dealer score: {dealerscore}')
            for player in self.players[1:]:
                if player.status == 'Blust':
                    print(f'Player {player.name} is blusted')
                    player.lose(self.betamount)
                    if player.balance <= 0:
                        self.players.pop(player)
                else:
                    playerscore = player.bestscore()
                    if playerscore > dealerscore:
                        print(f'Player {player.name} wins, score = {playerscore}')
                        player.win(self.betamount)
                    else:
                        print(f'Player {player.name} loses, score = {playerscore}')
                        player.lose(self.betamount)
                        if player.balance <= 0:
                            self.players.pop(player)

    def showbalance(self):
        print('Balances:')
        for player in self.players[1:]:
            print(f'{player.name}: {player.balance}')

#if __name__ == '__init__':
board = Board(2)
board.addplayer(Player('a', 3))
board.addplayer(Player('b', 2))
board.addplayer(Player('c', 1))
board.play()
