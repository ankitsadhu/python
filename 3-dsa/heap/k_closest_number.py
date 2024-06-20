import heapq
sorted_arr = [5,6,7,8,9]
k = 3
num = 7

# 5 -7, 6 -7, 7 - 7, 8 -7, 9 -7
# 2, |1, 0, 1 |, 2

heap = []

'''
the heapq module implements a min-heap by default. This means that the smallest element is kept at the root of the heap and the parent nodes are always smaller or equal to the child nodes.
If you want to use a max-heap in Python, you can invert the values before pushing them onto the heap. This is what we did in the previous code by pushing -num onto the heap.
When we retrieve the elements and invert them again, we effectively have a max-heap.
'''

for element in sorted_arr:
    heapq.heappush(heap, (-abs(element - num), -element)) #inverting so it works as max heap (diff_num, -num)
    if len(heap) > k:
        heapq.heappop(heap)
    
print(sorted(-num for _, num in heap))


class Solution:
  def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
    return sorted(heapq.nsmallest(k, arr, key=lambda i: abs(i-x+.1)))