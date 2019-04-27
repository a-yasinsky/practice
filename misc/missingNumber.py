def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    ln = len(nums)
    for k in range(ln+1):
        if k >= ln or k != nums[k]:
            return k

print(missingNumber([1]))
