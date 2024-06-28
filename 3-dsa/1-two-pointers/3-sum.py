class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicates
                continue
            self.searchPair(i + 1, nums, nums[i], triplets)
        return triplets

    def searchPair(self, left, nums, target, triplets: list[list[int]]):
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right] + target
            if curr_sum == 0:
                triplets.append([target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:  # skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right + 1]:  # skip duplicates
                    right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1

print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
