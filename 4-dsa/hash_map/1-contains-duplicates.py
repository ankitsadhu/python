def contains_duplicate(nums):
    records = set()
    for num in nums:
        if  num in records: 
            return True
        records.add(num)
        
    return False


def main():
    arrays =  [[1, 2, -3, 2, 1], [2, 5, 7, 9], [5, 6, 4, 7, 6, 11], [1, 4, 6, 10, 18, -2, -4], [3, 4, 8, 20, 34, 89, 3]]    
    for i in range(len(arrays)):        
        result = contains_duplicate(arrays[i])        
        print(str(i+1)+".\tDoes the given array", arrays[i], "contains duplicates?", result)        
        print("-"*100)


if __name__ == '__main__':    
    main()