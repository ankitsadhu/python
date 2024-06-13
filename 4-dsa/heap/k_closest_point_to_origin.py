from heapq import heappush as push, heappop as pop

class Solution:
    def euclidian_distance(nums):
        return nums[0] ** 2 + nums[1] ** 2


    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            push(heap, (-Solution.euclidian_distance(point), point))
            if len(heap) > k:
                pop(heap)
        
        return [point[1] for point in heap]
    
points = [[1,3],[-2,2]]
k = 1

print(Solution().kClosest(points=points, k=k))
print(Solution().kClosest(points=[[3,3],[5,-1],[-2,4]], k = 2))
    
