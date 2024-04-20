def Chori(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==2:
        return max(arr[0],arr[1])
    dp=[0]*(len(arr)+1)
    dp[0]=arr[0]
    dp[1]=arr[1]
    dp[2]=arr[0]+arr[2]
    for i in range(3,len(arr)):
        dp[i]=max(dp[i-2],dp[i-3])+arr[i]
    return max(dp[len(arr)-1],dp[len(arr)-2])
print(Chori([1,2,3,1]))