


# min heap

'''
|2|(pop smallest)   |3| (pop)  | 5  | (pop)  | 6  | (pop)
|3|3 -> size k = 3  |5|        | 6  |        | 8  |
|5|2                |6|        | 8  |        | 9  |
|6|1                |8|        | 10 |        | 10 | 
'''


import heapq

def sort_k_sorted_arr(arr, k):
    sorted_arr = []
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            sorted_arr.append(heapq.heappop(heap))
    
    for num in heap:
        sorted_arr.append(num)
    print(sorted_arr)

nearly_sorted_arr = [6,5,3,2,8,10,9] # k sorted arr
k = 3
sort_k_sorted_arr(nearly_sorted_arr,k)