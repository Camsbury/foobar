def answer(n):
    base=2
    while True:
        ans = convert(n,base)
        if pal_check(ans):
            return base
        else:
            base += 1
    
def convert(n,base):
    k=n
    c=1
    ans=0
    while True:
        ans = (k%base)*c+ans
        c=c*10
        k=k/base
        if k == 0: break
    if str(ans)[0] == "0":
        ans=int(str(ans)[1::])
    return ans
    
def pal_check(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False