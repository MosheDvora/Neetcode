nums = [1, 2, 3, 9, 4, 5, 11]


def twosum(nums, target):
    # we sort and slice the souce list for not checkin
    # out of range numbers
    sort_nums = sorted(nums)
    work_nums = sort_nums[:sort_nums.index(target)]
    for i, num in enumerate(work_nums):
        for next_num in work_nums[i + 1:]:
            if (num + next_num) == target:
                return (nums.index(num), nums.index(next_num))
                break

def twosum2(nums, target):
    for num in nums:
        diff = target - num
        if ((nums.index(diff) if diff in nums else -1) + num) == target:
            return nums.index(num), nums.index(diff)
print(twosum(nums,9))
print(twosum2(nums,9))
