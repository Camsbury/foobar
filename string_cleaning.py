#String cleaning fast version

def answer(chunk, word):
    if len(word) == 1:
        return chunk.replace(word,'')
    solutions = cleaner(chunk, word)
    return lexify(shortify(list(set(solutions))))
    
    
def cleaner(chunk,word):
    solutions = [chunk]
    if counter(chunk,word) == 0:
        return solutions
    else:
        for n in range(counter(chunk,word)):
            solutions += cleaner(clean_nth(chunk,word,n+1),word)
        return solutions

def counter(chunk,word):
    if word in chunk:
        n = 1
    else:
        return 0
    while finder(chunk, word, n) > -1:
        n += 1
    return n - 1

def clean_nth(chunk,word,n):
    #deletes nth occurence of word in chunk
    f = finder(chunk,word,n)
    return chunk[:f] + chunk[f:len(chunk)].replace(word,"",1)
    
def finder(chunk, word, n):
    #finds location of nth occurence of word in chunk
    start = chunk.find(word)
    while start >= 0 and n > 1:
        start = chunk.find(word, start+1)
        n -= 1
    return start
    
def shortify(solutions):
    min_length = 21
    new_sols = []
    for sol in solutions:
        if len(sol) < min_length:
            new_sols = [sol]
            min_length = len(sol)
        elif len(sol) == min_length:
            new_sols.append(sol)
    return new_sols

def lexify(solutions):
    return lex_score(solutions)[0][0]
    
def lex_score(solutions):
    sols2 = []
    for sol in solutions:
        sol = list(sol)
        score = [ord(x) for x in sol]
        sols2.append(("".join(sol),score))
    return sorted(sols2,key = lambda x: x[1], reverse = False)
        
    