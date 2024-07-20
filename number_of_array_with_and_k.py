'''Given an array of integers nums and an integer k, return the number of 
subarrays
 of nums where the bitwise AND of the elements of the subarray equals k.

 

Example 1:

Input: nums = [1,1,1], k = 1

Output: 6

Explanation:

All subarrays contain only 1's. '''


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        count = 0 

        for n in nums:
            current_count = defaultdict(int)
            current_count[n] += 1

            for val, a in prefix_counts.items():
                 current_count[n & val] += a

            count += current_count[k]
            prefix_counts = current_count
            print(prefix_counts, count, current_count[k],k)
        return count
