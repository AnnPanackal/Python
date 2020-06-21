#--------Length of substring which is not a vowel-------
def isvow(no):
    if no in ['a','e','i','o','u']:
        return True
    return False

def len_str(n):
    cnt=0
    lt=len(n)
    for i in range(1,lt):
        if (isvow(n[i]) == True) and (isvow(n[i-1]) ==True):
            cnt=cnt+1
        if (isvow(n[i]) != True):
            cnt=cnt+1
    return cnt
    
