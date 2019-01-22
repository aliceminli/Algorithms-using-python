def plus_one(nums):
    a = str(int("".join([str(i) for i in nums])) + 1)
    return [int(i) for i in a]

def plus_one_recursion(nums):
    n = len(nums)
    if nums[-1] != 9:
        return nums[0:n-1] + [nums[-1] +1]
    elif n > 1:
        return plus_one_recursion(nums[0:n-1]) + [0]
    else:
        return [1,0]


if __name__ == '__main__':

    print plus_one([1,2,3])
    print plus_one_recursion([1, 2, 3])

    a="abc"
    b="123"
    print a.join(b)
    print b.join(a)