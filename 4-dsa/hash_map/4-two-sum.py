def two_sum(nums: list[int], target: int):
    processed_nums =  {}
    for index, num in enumerate(nums):
        left_over_sum = target - num
        if left_over_sum in processed_nums:
            return [index, processed_nums[left_over_sum]] 
        else:
            processed_nums[num] = index
    return [-1, -1]


def main():
    print(two_sum( [2, 4, 6, 8, 10, 19], 21))
    print(two_sum( [-4, -8, 0, -7, -3, -10], -15))
    print(two_sum([-1, 9, 56, 12, -13, -6, 23, 19, 71, -56, -14],  -44))
    print(two_sum([3,3], 6))
    print(two_sum([49, 17, 15, 22, -45, 29, 18, -15, 11, 37, 12, -52], 0))

if __name__ == "__main__":
    main()
