def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ha = {}
        for i,num in enumerate(nums):
            remainder = target - num
            if remainder in ha:
                return [ha[remainder],i]
            else:
                ha[num] = i
