#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: hack_rsa.py
# description: obtaining RSA's secrete key from messages,
# cryptotexts, and public keys.
# YOUR NAME
# YOUR A-NUMBER
#############################################################

import math
from rsa_aux import xgcd, mod_exp
from rsa_aux import mult_inv, euler_phi, is_prime, find_primes_in_range
from rsa import rsa

class hack_rsa(object):

    ### Assign 12, subproblem 1.9
    @staticmethod
    def get_sec_key(message, cryptotext, pub_key):
        ### your code here
        e, n = pub_key[0], pub_key[1]
        primes = find_primes_in_range(0,n)
        divisors = []

        for p in primes:
            if n % p == 0:
                divisors.append(p)

        # check if prime
        both_prime = False
        for div in divisors:
            if is_prime(div):
                both_prime = True
            else:
                both_prime = False
                break
        p = 0
        q = 0
        if len(divisors) == 2 and is_prime:
            p,q = divisors[0], divisors[1]

        is_valid = euler_phi(n) == (p-1)*(q-1)
        if is_valid:
            is_valid = xgcd(e, euler_phi(n))[0] == 1
        if is_valid:
            d = mult_inv(e, euler_phi(n))
            decrypted_text = rsa.decrypt(cryptotext, (d,n))
            if decrypted_text == message:
                return (d,n)
            else:
                print("FAILED HACK")
        else:
            return (0, 0)
