class solution:
    def subtraction(self,n):
        sum = 0
        mult = 1
        temp = n
        while temp > 0:
            r = temp%10
            sum+=r
            mult*=r
            temp//=10
        return mult-sum