class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for i in strs:
            ans+=str(len(i))+'#'+i
        return ans    

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        n=len(s)
        while(i<n):
            j=i
            while(s[j]!='#'):
                j+=1
            l=int(s[i:j])
            i=j+1
            ans.append(s[i:i+l])
            i+=l
        return ans    
