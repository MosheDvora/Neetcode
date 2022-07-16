from typing import List
import time

nums_ls = list(range(1,10000000))

class ContainsDuplicate:
    def is_duplicate(self, chk_ls):
        if len(chk_ls) == len(set(chk_ls)):
            return "False, There is a no duplicate item"
        else:
            return f"True, There is a duplicate item"




start = time.time()
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

start = time.time()
y = Solution()
print(y.containsDuplicate(nums_ls))
end_for = time.time()
print(f"Runtime of the program is {end_for - start}")


start = time.time()
x = ContainsDuplicate()
print(x.is_duplicate(nums_ls))
end_len = time.time()
print(f"Runtime of len(Set) program is {end_len - end_for}")

