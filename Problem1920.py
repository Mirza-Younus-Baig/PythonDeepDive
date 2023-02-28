from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res


res = Solution()
inp = [0,2,1,5,3,4]
print(res.buildArray(inp))