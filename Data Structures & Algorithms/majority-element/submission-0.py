class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=len(nums)//2
        mydict={}
        for i in nums:
            mydict[i]=mydict.get(i,0)+1
        for key,value in mydict.items():
            if(value>count):
                return key

        