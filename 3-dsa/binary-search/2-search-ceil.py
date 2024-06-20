# ceil of the key will be the smallest element in the given array greater than or equal to the key

import math


def search_ceil(arr: list[int], key: int):
    start, end  = 0, len(arr) -1
    if key > arr[end]:
        return -1
    
    while start <= end:
        mid = math.floor(start + (end - start) / 2)

        if arr[mid] == key:
            return mid
 
        if arr[mid] > key:
            end = mid -1
        elif arr[mid] < key:
            start = mid + 1

    return start

print(search_ceil([1, 3, 8, 10, 15], 12))
print(search_ceil([4, 6, 10], 17))
print(search_ceil([4, 6, 10], -1))