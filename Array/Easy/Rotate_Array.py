def rotate_insert(nums, k):
    for i in range(k % len(nums)):
        nums.insert(0, nums.pop())


def rotate_list(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


# def rotate(nums, k):
#     for i in range(0, k % len(nums)):
#         for j in range(len(nums) - 1, 0, -1):
#             temp = nums[j]
#             nums[j] = nums[j - 1]
#             nums[j - 1] = temp

def rotate(nums, k):
    k = k % len(nums)
    a = nums[-k:]
    print a
    for i in range(len(nums)-k-1, -1, -1):
        nums[i+k] = nums[i]
    for j in range(0, k % len(nums)):
        nums[j] = a[j]

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 4)
    # rotate_insert(a, 3)
    b = [1, 2, 3, 4, 5, 6, 7]
    rotate_list(b, 8)
    print a
    # print b
