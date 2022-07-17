
def k_most_frequent(nums, k):
    nums_set = set(nums)
    count_list = {}
    for item in nums_set:
        count_list[nums.count(item)] = item

    list_map = sorted(list(count_list.items()), reverse=True)
    print(f"The max num is: {list_map[0][1]} \n"
          f"The second max num is {list_map[1][1]}")


def k_most_frequent2(nums, k):
    # Sort by largest recurrence

    # sort_freq_nums = sorted(nums, reverse=True, key=nums.count)
    sort_freq_nums = sorted(nums, reverse=True, key=lambda x: nums.count(x))
    # Sort the set by the largest recurrence from sort_freq_nums
    order_freq_nums = sorted(set(sort_freq_nums), key=sort_freq_nums.index)
    # Printing the k most frequent from order_freq_nums

    print(order_freq_nums[:k])


def k_most_frequent3(nums, k):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    tuples = sorted(d.items(), key=lambda x: x[1], reverse=True)

    return [x[0] for x in tuples][:k]


nums = [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = 2
print(k_most_frequent2(nums, k))
