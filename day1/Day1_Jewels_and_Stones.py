class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for stone in S:
            for jewel in J:
                if jewel == stone:
                    count += 1
        return count