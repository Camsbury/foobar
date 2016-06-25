# -*- coding: utf-8 -*-
"""
Line up The Captives Revisited
"""

def line_up(x,y,n):
    count = len(construct_base_lines(x,y))
    for n_curr in range(x+y,n+1):
        count *= n_curr - 2
    return count

def construct_base_lines(x,y):
    lines = {1:[[(1,1),[1]]]}
    nex = 2
    while nex < x + y:
        lines[nex] = []
        for line in lines[nex-1]:
            if line[0][0] < x:
                lines[nex].append([(line[0][0]+1,line[0][1]),[nex] + line[1]])
            if line[0][1] < y:
                lines[nex].append([(line[0][0],line[0][1]+1),line[1] + [nex]])
        nex += 1
    return [line[1] for line in lines[nex-1]]