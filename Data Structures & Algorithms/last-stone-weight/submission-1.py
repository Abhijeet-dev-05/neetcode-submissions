import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while(len(stones)>1):
            num1=heapq.heappop_max(stones)
            num2=heapq.heappop_max(stones)
            if(num1<num2):
                new_weight=num2-num1
                heapq.heappush_max(stones,new_weight)
            elif(num1==num2):
                continue
            else:
                new_weight=num1-num2
                heapq.heappush_max(stones,new_weight)
        return 0 if len(stones)==0 else stones[0]       
        