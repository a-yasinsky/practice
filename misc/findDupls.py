def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    indList = [0] * len(nums)
    for x in nums:
        indList[x] += 1
        if indList[x] > 1:
            return x
    return 0

print(findDuplicate([1,3,4,2,2]))
