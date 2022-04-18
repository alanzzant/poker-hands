# poker-hands

A python Monte Carlo simulation to calculate the probabilities for each poker hand.

> Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables.

## The simulation

The idea is simple, using randomly-generated poker hands of 5 cards, and observing which poker hands appear in it, repeat the process a number of times specified by the user and then dividing how many times each hand appeared by how many hands were generated. 

8 hands were taken into account, and they are written in the following dictionary:
```
hand_counter = {
    'royal_flush': 0,
    'straight_flush': 0,
    'straight': 0,
    'pair': 0, 
    'flush': 0,
    'three_of_a_kind': 0,
    'full_house': 0,
    'double_pair': 0,
}
```

## Results
According to [Wikipedia](https://en.wikipedia.org/wiki/Poker_probability) these are the following probabilities for each hand:
| Hand        | Probability (%) | Probability |
| ----------- | --------------- | ----------- |
| Royal flush | 0.000154% | 0.00000154 |
| Straight flush | 	0.00139% | 	0.0000139 |
| Full house | 0.1441% | 0.001441 |
| Flush | 0.1965% | 0.001965 |
| Straight | 0.3925% | 0.003925 |
| Three of a kind | 2.1128%	| 0.021128 |
| Two pair | 4.7539% | 0.047539 |
| Pair | 42.2569% |	0.422569 |

After 2,000,000 of attempts/iterations of hands, we obtain the following probabilities for each hand:


| Hand        | Probability (%) | Probability |
| ----------- | --------------- | ----------- |
| Royal flush | 0.00005% | 5E-7 |
| Straight flush | 	0.0017% | 	1.7E-5 |
| Full house | 0.14575% | 0.0014575 |
| Flush | 0.1869% | 0.001869 |
| Straight | 0.39445% | 0.0039445 |
| Three of a kind | 2.25555%	| 0.0225555 |
| Two pair | 4.7539% | 0.047539 |
| Pair | 47.1125% |	0.471125 |

## Selection sort
As an extra, a selection sort algorithm was used for ordering cards to obtain consecutive cards in straight, straight flush and royal flush hands.
