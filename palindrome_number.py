class solution :
    def palindrome_number(self,n):
        temp = n
        k=0
        while temp>0:
            r = temp%10
            k=k*10+r
            temp//=10
        if k == n:
            return "palindrome"
        else:
            return "not_a_palindrome"
