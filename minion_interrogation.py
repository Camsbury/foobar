"""
Minion interrogation
====================

Figured out that probability/time gives a good score for ranking

"""

def answer(minions):
    minions_scored = [(x,float(y[2]*y[0])/y[1]) for x,y in enumerate(minions)]
    return [x[0] for x in sorted(minions_scored,key=lambda x: (x[1],x[0]))]