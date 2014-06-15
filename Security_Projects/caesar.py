"""
Caesar cipher - Implement a Caesar cipher. 
The key is an integer from 1 to 25. This cipher rotates the letters 
of the alphabet (A to Z). The encoding replaces each letter with the 
1st to 25th next letter in the alphabet (wrapping Z to A). 
So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". 
This simple "monoalphabetic substitution cipher" provides almost no security, 
because an attacker who has the encoded message can either use frequency 
analysis to guess the key, or just try all 25 keys.
"""

import string

message = input("Enter the message: ")
shift = int(input("Enter the shift: "))

#create shifted alphabet
shifted_alpha = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]

#create translation table
trans_table = str.maketrans(string.ascii_lowercase, shifted_alpha)

print(message.translate(trans_table))

