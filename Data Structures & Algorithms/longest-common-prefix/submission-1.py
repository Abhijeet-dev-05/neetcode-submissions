class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        if(len(strs)==0):
            return res
        base=strs[0]    
        for i in range(len(base)):
            for word in strs[1:]:
                if(i==len(word) or base[i]!=word[i]):        
                    return res
            res+=base[i]        
        return res