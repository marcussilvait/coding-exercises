class Solution:
    def smaller_numbers_than_current(self, nums):
        """ 1365. How Many Numbers Are Smaller Than the Current Number
        Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
        That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
        Return the answer in an array.

        Example 1:
        Input: nums = [8, 1, 2, 2, 3]
        Output: [4, 0, 1, 1, 3]

        Example 2:
        Input: nums = [6, 5, 4, 8]
        Output: [2, 1, 0, 3]

        Example 3:
        Input: nums = [7, 7, 7, 7]
        Output: [0, 0, 0, 0]

        Constraints:
        2 <= nums.length <= 500
        0 <= nums[i] <= 100

        >>> Solution().smaller_numbers_than_current([8,1,2,2,3])
        [4, 0, 1, 1, 3]
        >>> Solution().smaller_numbers_than_current([6, 5, 4, 8])
        [2, 1, 0, 3]
        >>> Solution().smaller_numbers_than_current([7, 7, 7, 7])
        [0, 0, 0, 0]

        :param nums: list of int
        :return: list of int
        """

        lst = []
        for i in nums:
            c = 0
            for j in nums:
                if i > j:
                    c += 1
            lst.append(c)

        return lst



if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    print(Solution().smaller_numbers_than_current(nums))
    nums = [6, 5, 4, 8]
    print(Solution().smaller_numbers_than_current(nums))
    nums = [7, 7, 7, 7]
    print(Solution().smaller_numbers_than_current(nums))
