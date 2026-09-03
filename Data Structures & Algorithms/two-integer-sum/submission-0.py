class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for ind, val in enumerate(nums):
            rem = target - val
            if rem in hash:
                return [hash[rem], ind]
            hash[val] = ind
        return []