
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
    assert(sorted(res1) == [0, 1])
