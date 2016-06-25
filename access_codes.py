'''

There is a list of codes.
Codes can only be used once.
Codes are duplicates if they are the reverse of eachother.

Your job is to compare a list of the access codes and find the number
of distinct codes, where two codes are considered to be "identical"
(not distinct) if they're exactly the same, or the same but reversed.
The access codes only contain the letters a-z, are all lowercase,
and have at most 10 characters. Each set of access codes provided
will have at most 5000 codes in them.

For example, the access code "abc" is identical to "cba" as well as "abc."
The code "cba" is identical to "abc" as well as "cba." The list
["abc," "cba," "bac"] has 2 distinct access codes in it.

Write a function answer(x) which takes a list of access code strings, x,
and returns the number of distinct access code strings using this
definition of identical.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) x = ["foo", "bar", "oof", "bar"]
Output:
    (int) 2

Inputs:
    (string list) x = ["x", "y", "xy", "yy", "", "yx"]
Output:
    (int) 5

PROPOSED SOLUTION:

I will count the number of duplicates in the list with a for loop and
nested if loops seeing if the element or the reverse is present.
I will then return the difference of the length of the list and this count.

'''

def answer(x):
    return len(x) - dups(x)
    
def dups(codes):
    count = 0
    for i, code in enumerate(codes):
        comp_codes = codes[i+1:len(codes)]
        if code in comp_codes:
            count += 1
        elif code[::-1] in comp_codes:
            count += 1
    return count
        
        