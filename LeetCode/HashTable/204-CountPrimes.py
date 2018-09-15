class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        sqrt_n = int(round(n**0.5))
        for i in xrange(2, sqrt_n + 1):
            if s[i]:
                s[i*i: n : i] = [0] * len(xrange(i*i, n, i))
        return sum(s)

        '''
        def isPrime(n):
            if n <= 1:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        '''