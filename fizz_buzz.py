class solution:
    def fizz_buzz(self,n:int) -> list[str]:
        ans = []
        for i in range(1,n+1):
            if i%3 ==0 and i%5==0:
                ans.append("fizz_buzz")
            elif i % 3 == 0:
                ans.append("fizz")
            elif i % 5 == 0:
                ans.append("buzz")
            else:
                ans.append(str(i))
        return ans
k = int(input("enter number : "))
obj = solution()
output = obj.fizz_buzz(k)
print(output)
