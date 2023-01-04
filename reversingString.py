#reverse a string

def reverseString(strings):
    for i in range(len(strings)-1,-1,-1):
        print(strings[i], end = "")
        
        
      
strings = "heelo How Are you DoIng"
reverseString(strings)
