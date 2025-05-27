from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # stole it from comments
        nums = sorted(nums)
        max_sum = 0
        for i in range(len(nums)):
            max_sum = max(nums[i] + nums[len(nums) - 1 - i], max_sum)
        return max_sum
        # pairs = []
        # for i in range(0, len(nums) - 1, 2):
        #     print(i)
        #     pairs.append((nums[i], nums[i + 1]))

        # from itertools import pairwise
        # pairs = pairwise(nums)
        # for i, pair in enumerate(pairs):
        #     x, y = pair[0], pair[1]
        #     for j, pair2 in enumerate(list(pairs[i:])):
        #         if x == pair2[0] or y == pair2[1]:
        #             pairs.pop(j)

        # print([x for x in pairs])

if __name__ == "__main__":
    print(Solution().minPairSum(nums=[3, 5, 2, 3]))
