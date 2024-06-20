import math

def binary_search(arr, key, check_prev_elem):
    start, end = 0, len(arr) -1
    key_index = -1

    while start <= end:
        mid = math.floor(start + (end - start)/2)
        if arr[mid] > key:
            end = mid -1
        elif arr[mid] < key:
            start = mid + 1
        else: # key found
            key_index = mid
            if check_prev_elem:
                end = mid -1
            else:
                start = mid + 1
        
    return key_index


def find_1st_n_last_occurence_of_num(arr, key):
    occurance = [-1, -1]
    occurance[0] = binary_search(arr, key, True)
    if occurance[0] != -1:
        occurance[1] = binary_search(arr, key, False)

    return occurance


def main():
    print(find_1st_n_last_occurence_of_num([4, 6, 6, 6, 9], 6))
    print(find_1st_n_last_occurence_of_num([1, 3, 8, 10, 15], 10))
    print(find_1st_n_last_occurence_of_num([1, 3, 8, 10, 15], 12))

if __name__ == "__main__":
    main()