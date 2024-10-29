def solution(start: int, goal: int):
    res = start ^ goal
    while res != goal:
        res = res ^ goal
        res = res + goal
        print(res)
    return res

print(solution(10, 7))