def space_optimized_dp(n):
    prev=0
    curr=1
    if n==0:return prev
    elif n==1:return curr
    else:
        count=1
        while(count<n):
            next = prev+curr
            count+=1
            prev=curr
            curr=next
        return next

print(space_optimized_dp(5)) 
#time complexity = O(N)
# space complexity = O(1)       