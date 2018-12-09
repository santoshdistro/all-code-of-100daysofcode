class Solution(object):
    def lenLongestFibSubseq(self, A):
        dp = collections.defaultdict(lambda : 2)
        ret, idx = 0, { A[0] : 0 }
        for i in xrange(1, len(A)-1):
            idx[A[i]] = i
            for j in xrange(i+1, len(A)):
                x = A[j] - A[i]
                if x >= A[i] : break
                elif x not in idx: continue
                dp[i,j] = dp[idx[x], i] + 1
                ret = max(ret, dp[i,j])
        return ret 