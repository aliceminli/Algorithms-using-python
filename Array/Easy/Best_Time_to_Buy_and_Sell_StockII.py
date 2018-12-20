import math

def maxProfit(nums):
    maxfpt = 0
    for x in range(1, len(nums)):
        if nums[x] > nums[x-1]:
            maxfpt += nums[x] - nums[x-1]
    return maxfpt


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    print maxProfit(a)
    print res(a)
