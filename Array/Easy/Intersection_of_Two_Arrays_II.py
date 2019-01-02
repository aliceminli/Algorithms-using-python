def intersect(nums1, nums2):
    dt = {}
    res = []

    for num in nums1:
        dt[num] = dt.get(num, 0) + 1
    for num in nums2:
        if num in dt and dt[num] > 0:
            res.append(num)
            dt[num] -= 1
    return res


if __name__ == '__main__':
    print intersect([1, 2, 3, 4, 5], [1, 2, 3])
