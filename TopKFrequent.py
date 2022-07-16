nums1 = [1]



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
    sort_freq_nums = sorted(nums, reverse=True, key=nums.count)
    # Sort the set by the largest recurrence from sort_freq_nums
    order_freq_nums = sorted(set(sort_freq_nums), key=sort_freq_nums.index)
    # Printing the k most frequent from order_freq_nums
    for i in range(k):
        if i <= len(order_freq_nums):
            print(f"{order_freq_nums[i]} ", end="")

    # freq = [1 for i in range(10)]
    # print(freq)
    # count = {}
    # for n in nums:
    #     count[n] = 1 + count.get(n, 0)
    # print(count)
    # count.get()
    # for item in count.values():
    #     freq.append(item)




nums = [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = 2
k_most_frequent2(nums, k)



# k_most_frequent(nums,k)