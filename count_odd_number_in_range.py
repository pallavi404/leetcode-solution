class solution:
    def odd_number(self,n:int,m:int) -> list[int]:
        count= 0
        ans = []
        for i in range(n,m+1):
            if i % 2==1:
                count += 1
                ans.append(i)
        print(count)
        print("The odd number between",n,"and",m,"are",ans,".")
low = int(input("enter range starting number : "))
high = int(input("enter range ending number : "))
obj = solution()
output = obj.odd_number(low,high)
 