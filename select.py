def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[mini] > arr[j]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
    print(" sorted array is")
    for item in arr:
        print(item,end=" ")
        
        
        
        
my_arr = [5,3,2,4,1]
selection_sort(my_arr)