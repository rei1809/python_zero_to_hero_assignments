#reversing only word in a string 

def reverseOnlyWord(strings):
    word = strings.split(" ")
    for item in word:
        res = item[::-1]
        print(res , end=" ")
        
strings = "heelo How Are you DoIng"
reverseOnlyWord(strings)
