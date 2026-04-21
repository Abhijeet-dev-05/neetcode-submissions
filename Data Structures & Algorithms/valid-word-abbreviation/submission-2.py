class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        while(i<len(word) and j<len(abbr)):
            w_c=word[i]
            a_c=abbr[j]
            if(a_c.isdigit()):
                if(a_c=='0'):
                    return False
                cur=0
                while(j<len(abbr) and abbr[j].isdigit()):
                    cur=cur*10+int(abbr[j])
                    j=j+1
                i=i+cur
            else:
                if(w_c!=a_c):
                    return False
                i=i+1
                j=j+1           
        return i==len(word) and j==len(abbr)            


        