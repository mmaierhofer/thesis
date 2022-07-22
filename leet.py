
from numpy import sort


def twoSum(nums):
    """
       :type x: int
       :rtype: bool
       """

    rightSum = sum(nums)

    leftSum = 0

    for idx, val in enumerate(nums):
        if leftSum == rightSum:
            return idx
        elif idx == len(nums)-1:
            return -1

        rightSum -= val
        leftSum += val


print(twoSum([2, 1, -1]))
