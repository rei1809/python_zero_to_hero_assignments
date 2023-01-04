#check Palindrome

def checkPalindrome(strings):
    flag = 0
    for i in range(len(strings)):
        if strings[-1-i] != strings[i]:
            flag = 1
            
    if flag == 0:
        return True
    
    else:
        return False
    
strings = 'AppA'
checkPalindrome(strings)
