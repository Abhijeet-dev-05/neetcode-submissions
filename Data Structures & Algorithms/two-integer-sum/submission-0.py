class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}
        for i in range(len(nums)):
            x=target-nums[i]
            if(x in mydict):
                return [mydict[x],i]
            mydict[nums[i]]=i    
        