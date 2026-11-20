from math import *
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        ans=[]
        heapq.heapify(arr)
        for a,b in points:
            distance=sqrt(a**2+b**2)
            heapq.heappush(arr,[distance,a,b])
        for i in range(k):
            distance,a,b=heapq.heappop(arr)
            ans.append([a,b])
        return ans    