# -*- coding: utf-8 -*-
"""

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

Write a function answer(str_S) which, given the base-10 string
representation of an integer S, returns the largest n such that
R(n) = S. Return the answer as a string in base-10 representation.
If there is no such n, return "None". S will be a positive integer
no greater than 10^25.

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"

@author: buddha
"""

def answer(str_S):
    n = find_odd(str_S)
    if n == "None":
        n = find_even(str_S)
    return n
    
def find_odd(str_S):
    len_s = len(str_S)
    s = long(str_S)
    bounds = get_odd_bounds(s,len_s)
    check = -1
    while True:
        n_try = make_odd(mean(bounds))
        s_try = R(n_try)
        if s_try == s:
            return str(n_try)
        elif s_try > s:
            bounds[1] = n_try
        else:
            bounds[0] = n_try
        if n_try == check:
            print bounds
            return "None"
        check = n_try
    
def find_even(str_S):
    len_s = len(str_S)
    s = long(str_S)
    bounds = get_even_bounds(s,len_s)  
    check = -1
    while True:
        n_try = make_even(mean(bounds))
        s_try = R(n_try)
        if s_try == s:
            return str(n_try)
        elif s_try > s:
            bounds[1] = n_try
        else:
            bounds[0] = n_try
        if n_try == check:
            return "None"
        check = n_try 
   
def get_odd_bounds(s,len_s):
    if len_s > 1:
        u_bound = long('9'*len_s)
        l_bound = -1
        while l_bound == -1:
            if R(make_odd(long(u_bound/10))) > s:
                u_bound = make_odd(long(u_bound/10))
            else:
                l_bound = make_odd(long(u_bound/10))
        return [l_bound,u_bound]
    else:
        return [1,9]
        
def get_even_bounds(s,len_s):
    if len_s > 1:
        u_bound = make_even(long('9'*len_s))
        l_bound = -1
        while l_bound == -1:
            if R(make_even(long(u_bound/10))) > s:
                u_bound = make_even(long(u_bound/10))
            else:
                l_bound = make_even(long(u_bound/10))
        return [l_bound,u_bound]
    else:
        return [2,10]
        
def make_even(n):
    if n%2 == 0:
        return n
    else:
        return n+1
        
def make_odd(n):
    if n%2 <> 0:
        return n
    else:
        return n+1
        
def R(n):
    if n < 0:
        return "None"
    elif n%2 == 0:
        return R_even(n)
    else:
        return R_odd(n)
        
def R_even(n):
    return R(n/2) + R(n/2 + 1) + n/2
    
def R_odd(n):
    return R((n-1)/2 - 1) + R((n-1)/2) + 1

def memoize(f):
    memo = {0:1,1:1,2:2}
    def helper(x):
        if x not in memo:   
            memo[x] = f(x)
        return memo[x]
    return helper
    
def mean(tuple):
    return long((tuple[0]+tuple[1])/2)
    
R = memoize(R)