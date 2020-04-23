def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n-1)


def selection_sort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[small]:
                small = j
        temp = arr[small]
        arr[small] = arr[i]
        arr[i] = temp