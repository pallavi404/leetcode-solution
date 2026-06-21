class soltion:
    def count_digit(self,n):
        c = 0
        temp = n
       
        while temp > 0:
            r = temp%10
            if n %r ==0:
                c+=1
            temp//=10
        return c