def singleNumber_dict(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def SingleNumber_modulo(nums):
    return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    print SingleNumber_modulo([1, 2, 1, 4, 4, 5, 5])
