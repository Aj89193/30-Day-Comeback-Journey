
def two_sum_hash_map(nums,target):
    target_seem={}

    for i,num in enumerate(nums):
        complement=target-num
        if complement in target_seem:
            return [target_seem[complement],i]
        target_seem[num]=i







nums = [2, 7, 11, 15]
target = 9
result=two_sum_hash_map(nums,target)
print(result)
