def els(origem , i , j , text , word , n , k):
    if i <= len(text)-1:
        if text[i] == word[j]:
            if j == len(word)-1:
                return els(0 , 0 , 0 , text[1:] , word , n , k+1)
            else:
                return els(origem , i+n+1 , j+1 , text , word , n , k)
        else:
            return els(origem , origem+1 , 0 , text , word , n , k)
    else:
        return k

print(els(0,0,0,"a","a",0,0,)==1)
print(els(0,0,0,"ab","a",0,0,)==1)
print(els(0,0,0,"abcde","ace",1,0,)==1)
print(els(0,0,0,"ababacab","ab",0,0,)==3)
print(els(0,0,0,"ababab","a",1,0,)==3)
