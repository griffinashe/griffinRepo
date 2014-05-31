#!/usr/bin/env python

#Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found.


def count_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u'] # "Y" not considered a vowel here. 
    string = raw_input("Please enter a sentence. ").lower()
    number_of_vowels = 0
    for i in string:
        for v in vowels:
            if i == v:
                number_of_vowels += 1
    return number_of_vowels

print count_vowels()
