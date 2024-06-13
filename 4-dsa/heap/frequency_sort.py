nums = [1,1,1,2,2,3]
def frequency_sort(nums: list[int]):
    if len(list) == 0:
        return nums
    
    num_freq = {}
    for num in nums:
        num_freq[num] = 1 + num_freq.get(num, 0)

    
    

print(frequency_sort(nums))