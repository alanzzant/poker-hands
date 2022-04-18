import collections
import random

SUITS = ['spades', 'hearts', 'clubs', 'diamonds']
RANKS = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

from selection_sort import sort

def create_deck():
    deck = [] 
    for suit in SUITS:
        for rank in RANKS:
            deck.append((suit, rank))

    return deck

def get_hand(deck):
    # 5 cards per hand is a standard
    return random.sample(deck, 5)

def look_up_hand(hand):
    hand_counter = {
        'royal_flush': 0,     # consecutive bigger cards,      same_suit
        'straight_flush': 0,  # consecutive cards,             same suit
        'full_house': 0,      # a pair and a three of a kind
        'flush': 0,           # any cards,                     same suit
        'straight': 0,        # consecutive cards,             any suit
        'three_of_a_kind': 0, # three of the same rank,        any suit
        'double_pair': 0,     # two pairs                      any suit
        'pair': 0,            # two of the same rank,          any suit 
    }

    ranks_counter = dict(collections.Counter(card[1] for card in hand))
    suits_counter = dict(collections.Counter(card[0] for card in hand))
    
    ### Flush hand
    if len(suits_counter) == 1: # all cards are the same suit
        hand_counter['flush'] = 1

    ### Pair, double pair and three of a king hands
    for quantity in ranks_counter.values():
        if quantity == 2:
            if hand_counter['pair'] == 1:
                hand_counter['double_pair'] = 1

            hand_counter['pair'] = 1

        if quantity == 3:
            hand_counter['three_of_a_kind'] = 1

    ### Full house
    if hand_counter['three_of_a_kind'] == 1and hand_counter['pair'] == 1:
        hand_counter['full_house'] = 1

    # Sort rank's indexes list in ascendent order
    ord_rank_index_list = sort([RANKS.index(card[1]) for card in hand])
    
    ### Straight 
    for i in range(1, len(ord_rank_index_list)):
        curr_minus_previous_card = ord_rank_index_list[i] - ord_rank_index_list[i - 1]
        ace_follows_jack = (curr_minus_previous_card == 9 and ord_rank_index_list[i] == 9)
        if not (curr_minus_previous_card == 1 or ace_follows_jack):
            break
        
        if i == len(ord_rank_index_list) - 1: # if we reached last element
            hand_counter['straight'] = 1

    ### Straight flush and royal flush
    if hand_counter['straight'] == 1 and hand_counter['flush'] == 1:
        hand_counter['straight_flush'] = 1

        if ord_rank_index_list[0] == 0 and ord_rank_index_list[4] == 12:
            hand_counter['royal_flush'] = 1

    return hand_counter

def simulate_hands(attempts):
    deck = create_deck()
    hands = []
    counter = {}

    for _ in range(attempts):
        hand = get_hand(deck)
        hands.append(hand)

        hand_counter = look_up_hand(hand)
        
        for hand_type in hand_counter:
            if hand_type in counter:
                counter[hand_type] += hand_counter[hand_type]
            else:
                counter[hand_type] = hand_counter[hand_type]

    return {hand_type: n/attempts for (hand_type, n) in counter.items()}

if __name__ == '__main__':
    attempts_input = input('How many attempts (default 10000)? ') or '10000'
    attempts = int(attempts_input)
    #hand_type = input('What hand (comma-separated) '))

    probabilities = simulate_hands(attempts)

    print('\n--- DIFFERENT HAND\'S PROBABILITIES ---\n')
    for (hand_type, probability) in probabilities.items():
        normalized_name = ' '.join(hand_type.split('_')).capitalize()
        normalized_spaces = ' ' * (17 - len(hand_type))
        print('* {}{}= {}'.format(normalized_name, normalized_spaces, probability))
