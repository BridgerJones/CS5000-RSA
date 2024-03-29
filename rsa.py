#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa.py
# description: RSA
# YOUR NAME Bridger Jones
# YOUR A-NUMBER A02314787
##############################################################


import numpy as np
from rsa_aux import xgcd, mod_exp
from rsa_aux import mult_inv, euler_phi, is_prime, find_primes_in_range
import math
import random

class rsa(object):

    ### Assign 12, subproblem 1.5
    @staticmethod
    def choose_e(eu_phi_n):
        ### your code here
         primes = find_primes_in_range(11, eu_phi_n - 1)
         rel_primes = list(filter(lambda x: xgcd(eu_phi_n, x)[0]==1, primes))
         r_num = random.randint(0, len(rel_primes)-1)
         return rel_primes[r_num]

    ### Assign 12, subproblem 1.6
    @staticmethod
    def generate_keys_from_pqe(p, q, e):
        ### your code here
        return (e, p*q), (mult_inv(e, euler_phi(p*q)), p*q)

    ### Assign 12, subproblem 1.7
    @staticmethod
    def encrypt(m, pk):
        ### your code here
        return (m**pk[0]) % pk[1]

    ### Assign 12, subproblem 1.7
    @staticmethod
    def decrypt(c, sk):
        ### your code here
        return (c**sk[0]) % sk[1]

    ### Assign 12, subproblem 1.8
    @staticmethod
    def encrypt_text(text, pub_key):
        ### your code here
        encrypted_char_list = []
        for char in text:
            encrypted_char_list.append(rsa.encrypt(ord(char), pub_key))
        return encrypted_char_list
    ### Assign 12, subproblem 1.8
    @staticmethod
    def decrypt_cryptotexts(cryptotexts, sec_key):
        ### your code here
        decrypted_string = ""
        for char in cryptotexts:
            decrypted_string += chr(rsa.decrypt(char, sec_key))
        return decrypted_string
