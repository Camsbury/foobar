"""
Hash it out
===========


digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256

For the first element, the value of message[-1] is 0.

For example, if message[0] = 1 and message[1] = 129, then:
For digest[0]:
129*message[0] = 129
129 XOR message[-1] = 129
129 % 256 = 129
Thus digest[0] = 129.

For digest[1]:
129*message[1] = 16641
16641 XOR message[0] = 16640
16640 % 256 = 0
Thus digest[1] = 0.

Write a function answer(digest) that takes an array of 16 integers and returns
another array of 16 that correspond to the unique message that created this
digest. Since each value is a single byte, the values are 0 to 255 for both
message and digest.

Test cases
==========

 in: [0, 129, 3, 129, 7, 129, 3, 129, 15, 129,  3, 129,  7, 129,  3, 129]
out: [0,   1, 2,   3, 4,   5, 6,   7,  8,   9, 10,  11, 12,  13, 14,  15]

 in: [129, 5, 141, 25, 137,  61, 149, 113, 145,  53, 157, 233, 185, 109, 165]
out: [  1, 4,   9, 16,  25,  36,  49,  64,  81, 100, 121, 144, 169, 196, 225]
bout:[129, 4, 137, 16, 153, 36, 177, 64, 209, 100, 249, 144, 41, 196, 97]
    
 in:  [24, 116, 131, 134,   5,  26, 94, 239, 111, 139, 45]
out:  [24, 108, 111, 105, 108, 118, 40,  71,  40,  35, 14]

 in:  [1, 41, 171,  43,  67, 195, 227,  99]
out:  [1, 40,   3,  40, 235,  40,  75,  40]
    
Took hours to just use my brain and try looking at the binary
relationships in solutions...
Took hours later to figure out the case of comparing evens vs odds.
Since I'm not finding any errors, there must be a problem with my
hasher function...
"""
import random

def unrefined_answer(digest,message):
    answer = [digest[0]]
    answer += [digest[i] ^ message[i-1] for i in range(len(message))[1:]]
    return answer
    

def answer(digest):
    message = digest[:]
    message[-1] = 0
    for i in range(len(message)):
        message[i] = (digest[i] ^ message[i-1])
        if (message[i-1]+digest[i])%2 != 0:
            if message[i] > 128:
                message[i] -= 128
            elif message[i] < 128:
                message[i] += 128
    return message
    
def hasher(message):
    digest = message[:]
    for i in range(len(message)):
        if i == 0:
            digest[i] = (129*message[i])%256
        else:
            digest[i] = ((129*message[i]) ^ message[i-1]) % 256
    return digest
    
def error_check(t):
    errors = []
    for i in range(t):
        message = [int(random.random()*256) for x in range(16)]
        if answer(hasher(message)) != message:
            errors.append(message)
    return errors
    
    
    
    