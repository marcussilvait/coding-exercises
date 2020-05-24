class Solution:
    def max_sub_array(self, nums: [int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.
        Example:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        Follow up:
        If you have figured out the O(n) solution, try coding another solution using the divide and
        conquer approach, which is more subtle.

        >>> Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        :param nums: list of int
        :return: int
        """

        total_sum = max_sum = nums[0]
        for i in nums[1:]:
            total_sum = max(i, total_sum + i)
            max_sum = max(max_sum, total_sum)

        return max_sum


if __name__ == '__main__':
    lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution()
    print(res.max_sub_array(lst))
