def moveZeroes_oneline(nums):
    nums.sort(key=lambda x: x == 0)
    return nums


def moveZeroes(nums):
    i = 0
    lt = len(nums)
    while i < lt:
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append("x")
        else:
            i = i + 1
    i = 0
    while i < lt:
        if nums[i] == "x":
            nums.remove("x")
            nums.append(0)
        else:
            i = i + 1
    return nums


if __name__ == '__main__':

    print moveZeroes_oneline([0,1,0,3,12])

    mylist = [(3, 5, 8), (6, 2, 8), (2, 9, 4), (6, 8, 5)]
    print sorted(mylist)
    print sorted(mylist, key=lambda x: x[1])

