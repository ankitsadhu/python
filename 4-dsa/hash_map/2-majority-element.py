# An element will be considered a majority if occurs more than [n/2] times

def find_majority_element(arr):
    num_counts = {}

    for num in arr:
        if num in num_counts:
            num_counts[num] +=  1
        else:
            num_counts[num] = 1
    

    return max(num_counts.keys(), key=num_counts.get) # keys =  [1, 2, 3]
        

def main():
    nums = [[2, 2, 3, 2, 2, 1, 2, 3],             
             [3, 2, 3, 3],             
             [3, 11, 10, 11, 11, 14, 11, 10, 11, 11],             
             [1, 2, 1, 2, 1, 1, 1, 1, 3, 2, 2, 2, 1, 1],            
             [5, 2, 1, 5, 5, 5, 5]            
            ]    
    for i in range(len(nums)):       
        print(str(i+1)+".\t The majority element in", nums[i],"is:", find_majority_element(nums[i]))        
        print("-"*100)


if __name__ == "__main__":
    main()


