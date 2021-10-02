def solution(sizes):
    width, height = [], []
    for i in sizes:
        i.sort()
    for i in sizes:
        width.append(i[0])
        height.append(i[1])
    return max(width) * max(height)


if __name__ == '__main__':
    sizes, result = [[60, 50], [30, 70], [60, 30], [80, 40]], 4000
    print(solution(sizes))

    sizes, result = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], 120
    print(solution(sizes))

    sizes, result = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]], 133
    print(solution(sizes))
