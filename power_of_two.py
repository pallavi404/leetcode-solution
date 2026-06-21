class solution:
    def power(self,n):
        if n==1:
            return True
        if n <=0:
            return False
        if n%2==0:
            return self.power(n//2)
        else :
            return False
k = int(input("enter a number : "))
obj = solution()
output = obj.power(k)
print(output)