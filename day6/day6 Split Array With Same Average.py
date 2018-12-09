class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        avg_tgt = float(sum(A)) / len(A)
        deadends = set()
        def dfs(start, cnt, total):
            if (cnt, total) in deadends: return False
            if cnt:
                avg_cur = float(total)/cnt
                if avg_cur == avg_tgt:
                    return True
                elif avg_cur > avg_tgt:
                    deadends.add((cnt, total))
                    return False
            for i in xrange(start+1, len(A)):
                if dfs(i, cnt+1, total+A[i]): 
                    return True
            deadends.add((cnt, total))
            return False
        return dfs(0, 0, 0)