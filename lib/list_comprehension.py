#!/usr/bin/env python3

def return_evens(num_list):
    for n in num_list:
        
        if n % 2 != 0:
            return []
        else:
            return [n for n in num_list if n % 2 == 0]           
    pass

def make_exclamation(sentence_list):
    if len(sentence_list) == 0 :
        return []
    else:
        return [s + '!' for s in sentence_list]
    
         
    pass