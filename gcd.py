class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        a = self.myPow(x, n // 2)

        if n % 2 == 0:
            return a * a
        else:
            return x * a * a