class Solution:
    def nthUglyNumber1(self,n):
        dp = [1]*n
        factor_index_a,factor_index_b,factor_index_c = 0,0,0
        for i in range(1,n):
            a,b,c = dp[factor_index_a]*2,dp[factor_index_b]*3,dp[factor_index_c]*5
            min_ = min(a,b,c)
            dp[i] = min_
            if a == min_:
                factor_index_a += 1
            if b == min_:
                factor_index_b += 1
            if c == min_:
                factor_index_c += 1
        return dp[-1]