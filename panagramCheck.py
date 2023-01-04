#check if a string is panagram or not
###panagram: panagrams are words or sentences containing every letter in the alphabet atleast once
import string

def panagram(strings, alpahabet=string.ascii_lowercase):
    pan = set(strings.lower())
    
    return set(alpahabet) - pan == set([])
    
string = 'The quick brown fox jumps over the lazy dog'
if(panagram(string)==True):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")
