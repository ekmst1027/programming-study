def search(aList):
    print(visited)
    if isVisit(visited):
        result.append(queue)
        return result

    for i in range(len(aList)):
        if visited[aList[i][0]] or visited[aList[i][1]]:
            continue

        queue.append(aList[i])
        print("i는 %s" %i)
        print("aList[i]는 %s" %aList[i])
        print("큐는 %s" %queue)
        
        visited[aList[i][0]] = True
        visited[aList[i][1]] = True
        search(aList)
        visited[aList[i][0]] = False
        visited[aList[i][1]] = False
        queue.pop()

def isVisit(visited):
    t_count = 0
    for i in visited:
        if i:
            t_count += 1
    if t_count == len(visited):
        return True
    return False

student = '6 10'.split()
student = list(map(int, student))
N, COUPLE = student
visited = [False] * N
input_num = '0 1 0 2 1 2 3 1 4 1 2 3 2 4 3 4 3 5 4 5'.split()
input_num = list(map(int, input_num))
result = []
queue = []

aList = []
list_0 = []
a = []
for i in range(len(input_num)):
    a.append(input_num[i])
    if i % 2 != 0:
        a.sort()
        aList.append(a)
        a = []
aList.sort()
print(search(aList))

#aList = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]]

# ## 그래프형식으로 만들기
# b = []
# for i in range(N):
#     a = []
#     for j in range(len(aList)):
#         if i in aList[j]:
#             for k in range(len(aList[j])):
#                 if i != aList[j][k]:
#                     a.append(aList[j][k])
#     b.append(a)

# print(b)

# for i in range(N):
#     if not visited[i]:
#         search(i)
# print(result)