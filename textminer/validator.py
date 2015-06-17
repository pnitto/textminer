import re

def binary(v):
    one_or_zero = r'[0-1]'
    if re.match(one_or_zero,v):
        return True
    
def binary_even(v):
    even_binary = r'[0-1]+0$'
    if re.match(even_binary,v):
        return True


def hex(v):
    hex_number = r'[^\da-fA-F]+'
    if re.findall(hex_number, v):
        return True

    ##could not get this one!
def word(v):
    words = r'[0-9--a-z]+'
    if re.findall(words,v):
        return True

    pass