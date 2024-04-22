#program to shuffle deck of card

import random, itertools
deck=list(itertools.product(range(1,14),["Spade","Club","hearts","Diamond"]))
random.shuffle(deck)
print(deck)