def generate_subarrays(nums):
    sub_arrays = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = []
            for k in range(i, j + 1):
                sub.append(nums[k])
            sub_arrays.append(sub)
    return sub_arrays
