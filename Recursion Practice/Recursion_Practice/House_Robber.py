def rob(arr1,idx):
    if idx>=len(arr1):
        return 0
    sp1=arr1[idx]+rob(arr1,idx+2)
    sp2=rob(arr1,idx+1)
    return max(sp1,sp2)
arr1=[1,2,3,1]
print(rob(arr1,0))
    