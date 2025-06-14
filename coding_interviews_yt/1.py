# https://www.youtube.com/watch?v=_LMsWiHu-Dk&ab_channel=CodingwithMinmer

"""
Q2:
    Give an array of integers and a target interger, determine if it has subarray of integers that add up to exactly the target.
    For example, with a target of 9 and an array of [4, 2, 5, 2, 6, 1], we return true.
"""
from utils import generate_subarrays


def main(nums, target):
    sub_arrays = generate_subarrays(nums)
    print(sub_arrays)
    sub_array_sum = 0
    for i in range(len(nums)):
        print(f"{i = }")
        for j in range(i, len(nums)):
            print(f"{j = }")
            sub_array_sum += nums[j]
            print(f"{sub_array_sum = }")
            if sub_array_sum > target:
                sub_array_sum = 0
                break
            if sub_array_sum == target:
                return True
    return False

if __name__ == "__main__":
    nums = [4, 2, 5, 2, 6, 1]
    target = 9
    print(main(nums, target))
