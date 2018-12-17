def remove_duplicates_use_set(nums):
    return len(set(nums))


def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    nl = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[nl] = nums[i]
            nl += 1
    return nl


if __name__ == '__main__':
    a = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
    print remove_duplicates_use_set(a)
    print remove_duplicates(a)
