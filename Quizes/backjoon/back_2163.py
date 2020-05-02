# 다이내믹 프로그래밍 기초
# 규칙 찾아서 바텀업 방식으로 공식을 만듬 - 쉬운문제라 규칙 금방 암

#   | 1 2 3 4 5 6 ..
# -----------------
# 1 | 0 1 2 3 4 5 ...
# 2 | 1 3 5 7 9 ...
# 3 | 2 5 8 11 ...
# 4 | 3 ...
# ..

N, M = map(int, input().split())

print((N-1) + N * (M-1))