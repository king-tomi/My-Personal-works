def create_list(filename):
    file = open(filename,"r")
    res = []
    for lines in file.read():
        res.append(lines)
    word = "".join(res)
    new = word.split(" ")
    my_list = []
    for i in new:
        if i.isdecimal():
            my_list.append(int(i))
    return my_list



def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j > 0 and arr[j] > key: 
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    if i % 10:
        print()


algo1 = create_list("random21.txt")
algo2 = create_list("random22.txt")
algo3 = create_list("random23.txt")
algo4 = create_list("random24.txt")


def counting_sort(arr,place):
    size = len(arr)
    count = [0] * 10
    output = [0] * size

    for i in range(size):
        index = arr[i] // place
        count[index%10] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = size - 1
    while i > 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index%10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]


def radix_sort(arr):
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        counting_sort(arr,place)
        place *= 10



def fib(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
    return b
    

import re

reg = re.compile(r"^[A-Za-z(\d)*_]{5,}")
