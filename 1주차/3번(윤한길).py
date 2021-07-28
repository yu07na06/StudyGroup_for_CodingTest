"""
n	    computers	                            return
3	    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	    2
3	    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	    1
"""

"""
def solution(n, computers):
    visited = [False for _ in range(n)]
    global answer
    answer = 0

    def DFS(computers, v, visited):
        global answer
        stack = []
        if not visited[v]:
            visited[v] = True
            answer += 1
            stack.append(v)
        while stack:
            tmp = stack.pop()
            for i, v in enumerate(computers[tmp]):
                if v == 1 and not visited[i]:
                    visited[i] = True
                    stack.append(i)

    for i in range(n):
        DFS(computers, i, visited)

    return answer
"""

"""
def DFS(computers, v, visited):
    if visited[v]:
        return False
    else:
        stack = []
        visited[v] = True
        stack.append(v)
    while stack:
        tmp = stack.pop()
        for i, v in enumerate(computers[tmp]):
            if v == 1 and not visited[i]:
                visited[i] = True
                stack.append(i)
    return True

def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if DFS(computers, i, visited):
            answer += 1
    return answer
"""

answer = 0
def solution(n, computers):
    visited = [False for _ in range(n)]

    def DFS(computers, v, visited):
        stack = []
        global answer
        if not visited[v]:
            visited[v] = True
            answer += 1
            stack.append(v)
        while stack:
            tmp = stack.pop()
            for i, v in enumerate(computers[tmp]):
                if v == 1 and not visited[i]:
                    visited[i] = True
                    stack.append(i)

    for i in range(n):
        DFS(computers, i, visited)

    return answer

# test
n = 4
computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]
print(solution(n, computers))
