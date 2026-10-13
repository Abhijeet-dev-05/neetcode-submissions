class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict={}
        for i in range(len(nums)):
            mydict[nums[i]]=mydict.get(nums[i],0)+1
        for key,value in mydict.items():
            if(value>1):
                return True
        return False        

        