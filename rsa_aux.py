#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa_aux.py
# description: auxiliay functions for RSA
# YOUR NAME Bridger Jones
# YOUR A-NUMBER A02314787
##############################################################

import numpy as np
import math

### Assign 12, subproblem 1.1
def xgcd(a,b):
    '''
    extended gcd that returns d, x, y such that
    d = ax + by.
    '''
    ### your code here
    prevx, x = 1, 0
    prevy, y = 0, 1
    aa, bb = a, b
    while bb != 0:
        q = aa // bb
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        aa, bb = bb, aa % bb
    return aa, prevx, prevy

### Assign 12, subproblem 1.2
def mult_inv(a, n):
    """
    multiplicative inverse of a in Z^{*}_{n}.
    """
    ### your code here
    d, x, y = xgcd(a,n)
    return x % n

### A tool you may want to use in your code.
### it's used in rsa_uts.py.
def z_star_sub_n(n):
    """
    compute the elements of Z^{*}_{n}; same as z_star_sub_n_elts.
    """
    return np.array([i for i in range(n) if xgcd(i, n)[0] == 1])

### A tool you may want to use in your code (e.g., euler's totient)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 2:
        for d in range(3, int(math.floor(math.sqrt(n)))+1, 2):
            if n % d == 0:
                return False
        return True

### A tool you may want to use in your tests (e.g., euler's totient)
def find_primes_in_range(a, b):
    return [i for i in range(a, b+1) if is_prime(i)]

### Assign 12, subproblem 1.3.
def mod_exp(a, b, n):
    """
    this function computes a^b mod n.
    """
    ### your code here
    c = 0
    d = 1

    for i in bin(b)[2:]:
        c = 2 * c
        d = (d * d) % n
        if i == '1':
            c = c + 1
            d = (d * a) % n
    return d

### Assign 12, subproblem 1.4
def euler_phi(n):
    """ Euler's Totient """
    ### your code here
    primes = find_primes_in_range(0,n)
    divisors = []
    for p in primes:
        if n % p == 0:
            divisors.append(p)
    print("DIVISORS",divisors)
    for p_divisor in divisors:
        n *= (1-1/p_divisor)
    print("N", n)
    return n
