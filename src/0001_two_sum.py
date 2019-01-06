"""
Question:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Solution:
Store target-num as key, and index as value. Return current index and value if num==key
"""


class Solution:
    def twoSum(self, nums, target):
        hm = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if hm.get(comp) is not None:
                return [i, hm.get(comp)]
            hm[num] = i


if __name__ == "__main__":
    res1 = Solution().twoSum([2, 7, 11, 15], 9)
    res2 = Solution().twoSum([1, 3, 4, 5, 6, 7, 2], 11)
    assert(sorted(res1) == [0, 1])
    assert (sorted(res2) == [3, 4])
