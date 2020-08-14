def take(arr,n):
    if n > len(arr):
        return None
    return [arr[i] for i in range(n)]
    
    
    
print(take([1,2,3,4,5,6,7,8,9,10],12))