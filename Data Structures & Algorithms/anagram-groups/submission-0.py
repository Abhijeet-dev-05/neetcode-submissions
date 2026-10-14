class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict={}
        for word in strs:
            temp="".join(sorted(word))
            if(temp not in mydict):
                mydict[temp]=[]
            mydict[temp].append(word)    
        return list(mydict.values())    
        