def solution(N, fry, clean, C):
    left = 0
    right = C * max([x+y for x, y in zip(fry, clean)])
    answer = right
 
    while left <= right:
        mid = (left + right) // 2
 
        val = 0
        for f, c in zip(fry, clean):
            val += (mid + c) // (f + c)
 
        if val >= C:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
 
    return answer
 
N = 2
fry = [3, 6]
clean = [2, 1]
C = 20
print(solution(N, fry, clean, C))
 
N = 4
fry = [2, 2, 1, 3]
clean = [2, 4, 3, 2]
C = 2
print(solution(N, fry, clean, C))