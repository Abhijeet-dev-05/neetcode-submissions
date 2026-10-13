class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        mydict={}
        for i in s:
            mydict[i]=mydict.get(i,0)+1
        for i in t:
            if(i not in mydict):
                return False
            else:
                if(mydict[i]==0):
                    return False
                else:
                    mydict[i]-=1
        return True                       
        