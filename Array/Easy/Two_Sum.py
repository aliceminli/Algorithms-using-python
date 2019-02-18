def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum_dict(nums, target):
    d = dict()
    for index, num in enumerate(nums):
        if d.get(num) == None:
            d[target - num] = index
        else:
            return [d.get(num), index]


if __name__ == '__main__':

    print twoSum([2, 7, 11, 15], 9)
    print twoSum_dict([2, 7, 11, 15], 9)
