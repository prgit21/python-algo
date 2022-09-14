class Solution:
    def romanToInt(self, s: str) -> int:
        ROM={ 'I' : 1,'V': 5, 'X':10,'L':50,'C':100,'D':500,'M':1000 }
        num= 0
        
        for i in range (len(s)-1):  
            if ROM[s[i+1]]>ROM[s[i]]:
                num-=ROM[s[i]]
            else:
                num+=ROM[s[i]]
        num+= ROM[s[len(s)-1]]
        
        return num
    
    
    #create dictionary with key val for all ele
    
    # loop len of string input 
    #if dict[s[i+1]]> dict[s[i]]???
    # handling last number differently why?