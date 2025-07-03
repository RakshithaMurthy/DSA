#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

#S1
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_arr = set(nums)
        return True if len(set_arr) != len(nums) else False
#TC = O(n), SC = O(n), no early exit when duplicate is found

#Efficient Solution
#S2
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen: #O(1) lookup
                return True
            seen.add(i)
        return False
#TC = O(n), SC = O(n), early exit when duplicate is found


#S3 - In space sorting, space optimized algo
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sorts in-place
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
#TC = O(nlogn), SC = O(n),


#🔍 Why not use a list?
#Using a list for duplicate detection means you're doing a linear search every time, which becomes very slow as the list grows. 
#In contrast, a set gives you constant-time lookups, which is why it’s ideal here.
#Using list/arr
output = []
for num in nums:
    if num in output:  # O(n) lookup
        return True
    output.append(num)  # O(1)
#TC = O(n^2), SC = O(n)