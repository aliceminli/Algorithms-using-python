class Solution(object):
    def containsDuplicate_set(self, nums):
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

    def containsDuplicate(self, nums):
        lenth = len(nums)
        for i in range(0, lenth):
            for j in range(i+1, lenth):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate_sort(self, nums):
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

    def containsDuplicate_dict(self, nums):
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = i
        return False




if __name__ == '__main__':
    a = Solution()
    print a.containsDuplicate_set([1, 2, 3, 4])
    print a.containsDuplicate([1, 2, 3, 4, 3, 5])
    print a.containsDuplicate_sort([1, 2, 3, 4, 3, 5])
    print a.containsDuplicate_dict([1, 2, 3, 4, 3, 5])
