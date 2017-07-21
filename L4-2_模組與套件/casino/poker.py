from random import choice

def deal_card():
	spades = []
	hearts = []
	diamonds = []
	clubs = []
	denominations = list(map(str, range(2, 11))) + ['J', 'Q', 'K', 'A']
	for i in range(len(denominations)):
		spades.append(denominations[i] + "Spade")
		hearts.append(denominations[i] + "Heart")
		diamonds.append(denominations[i] + "Diamond")
		clubs.append(denominations[i] + "Club")
		
	poker_cards = spades + hearts + diamonds + clubs
	return choice(poker_cards)
	
print(deal_card)