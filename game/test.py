def solution(arr, k):
    arr = [j for i in arr for j in i]
    arr.sort()
    return arr[k-1]

print(solution([[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]], 4))