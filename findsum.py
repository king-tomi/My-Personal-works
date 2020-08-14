def find_intersection(arr):
    if len(arr) == 0:
        return "False"
    word1 = arr[0]
    word2 = arr[1]
    new = [word for word in word1 if word in word2]
    new.sort()
    return new
    
words = ["1,2,3,4,13","3,5,4,13"]
new = find_intersection(words)