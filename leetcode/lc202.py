class Solution:
    def isHappy(self, n: int) -> bool:
        """ Write an algorithm to determine if a number n is "happy".
        A happy number is a number defined by the following process: Starting with any positive integer,
        replace the number by the sum of the squares of its digits, and repeat the process until
        the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy numbers.
        Return True if n is a happy number, and False if not.
        Example:
        Input: 19
        Output: true
        Explanation:
        1*1 + 9*9 = 82
        8*8 + 2*2 = 68
        6*6 + 8*8 = 100
        1*1 + 0 + 0 = 1

        >>> Solution().isHappy(19)
        True

        :param n: int
        :return: bool
        """

        def sqsum(num):
            result = 0
            while num > 0:
                r = num % 10
                result = result + r * r
                num = num // 10
            return result

        seen = set()
        while sqsum(n) not in seen:
            sum1 = sqsum(n)
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1
        return False


if __name__ == '__main__':
    Solution().isHappy(19)
