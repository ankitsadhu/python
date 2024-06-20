from collections import Counter
import heapq
import numpy as np

def kth_smallest_sort(arr, k):
    arr.sort()
    return arr[k-1]


def kth_smallest_heap(arr, k):
    heapq.heapify(arr)
    for _ in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr)


def topKFrequent(self, nums, k):
    counter = Counter(nums)
    return [num for num, _ in counter.most_common(k)]



def kth_smallest_np(arr, k):
    return np.partition(arr, k-1)[k-1]




def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = {}
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)

    heap = []
    for num, freq in freq.items():
        heapq.heappush(heap, (freq, num))
        
    print(heap)
    most_freq = heapq.nlargest(k, heap)

    result = [num for freq, num in most_freq]
    return result


def main():
    # print(kth_smallest_heap([1,1,1,2,2,3],2))
    # print(kth_smallest_np([1,1,1,3,2,2,4], 2))
    print(topKFrequent([1,1,1,2,2,3], k=2))

if __name__ == "__main__":

    main()