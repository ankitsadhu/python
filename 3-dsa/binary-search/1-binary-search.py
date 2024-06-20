import math


def binary_search(arr: list[int], key):
    start = 0
    end = len(arr) - 1

    isAsending = arr[start] < arr[end]
    
    while start <= end:
        mid = math.floor(start + ((end - start)/2)) 
        if arr[mid] == key:
            return mid
        
        if isAsending:
            if arr[mid] > key:
                end = mid - 1
            else:
                start = mid +1
        else:
            if arr[mid] > key:
                start = mid + 1
            else:
                end = mid -1

    return -1







def main():
    print(binary_search([4, 6, 10], 10))#2
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5)) # 4
    print(binary_search([10, 6, 4], 10)) # 0
    print(binary_search([10, 6, 4], 4)) # 2


if __name__ == "__main__":
    main()
