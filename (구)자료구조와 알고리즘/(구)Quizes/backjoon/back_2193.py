# 우선 이친수의 특징을 파악한다.
# 필연적으로 왼쪽부터 1번째와 2번째는 1, 0 이 올수 밖에 없다.
# 이후 0이면 다음 값은 0, 1 둘다 될수있고
# 1이면 다음 값은 무조건 0밖에 될수 없다.
# 규칙 : n값에 따라 수가 1, 1, 2, 3, 5, 8 .. 순으로 증가 (피보나치수열)
# + dp로 풀려면 t1,t2를 배열의 형태로 이전값다 다 저장하는 형태로 하면된다.

import sys

n = int(sys.stdin.readline().rstrip())
t1, t2 = 1, 1

for i in range(3, n+1):
    t1, t2 = t2, t1+t2

print(t2)



