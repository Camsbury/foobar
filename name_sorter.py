#Beastly name point sorter

def answer(names):
    
    names2 = scorer(names,True)
    scores = score_lister(names2)
    return sorter(names2,scores)
    
    
def scorer(names,option):
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    names2 = []
    if option:
        for name in names:
            score = 0
            for letter in name:
                score += ABC.index(letter) + 1
            names2.append((name,score))
    else:
        for name in names:
            name = list(name)
            score = [ord(x) for x in name]
            names2.append(("".join(name),score))
    return names2
    
def score_lister(names2):
    scores = [x[1] for x in names2]
    return sorted(list(set(scores)), reverse=True) 
    
def sorter(names2,scores):
    ans = []
    for score in scores:
        ans_part = []
        for name2 in names2:
            if name2[1] == score:
                ans_part.append(name2)
        if len(ans_part) > 1:
            ans_part = tie_breaker([x[0] for x in ans_part])
        [ans.append(x[0]) for x in ans_part]
    return ans
    
def tie_breaker(names_list):
    names_list2 = scorer(names_list,False)
    return sorted(names_list2,key=lambda x: x[1],reverse=True)
