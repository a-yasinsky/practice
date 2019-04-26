def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = [0] * (len(nums) + 2)
    for num in nums:
        if num >=0 and num <= len(nums):
            arr[num] = 1
    for k,v in enumerate(arr):
        if k>0 and v == 0:
            return k


print(firstMissingPositive([7,8,9,11,11]))
