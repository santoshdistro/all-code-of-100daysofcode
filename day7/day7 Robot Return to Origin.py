class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        countU = moves.count('U')
        countD = moves.count('D')
        countL = moves.count('L')
        countR = moves.count('R')
        return countU == countD and countL == countR