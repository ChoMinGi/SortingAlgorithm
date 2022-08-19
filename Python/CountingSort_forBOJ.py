# input 대신에 속도가 빠른 readline을 사용
import sys
input = sys.stdin.readline
# n값을 가져온다.
n = int(input())
# 0부터 10000까지의 10001 개의 리스트를 만들어준다.
result = [0]*10001
# 0부터 10000까지의 반복을 통하여 각 n번째에 존재하는 경우 +1 을 해준다.
for i in range(n):
    a = int(input())
    result[a] += 1
# 또 다시 10000까지의 반복을 통해서 각 숫자가 0 이 아닐경우
# 앞에서 부터 출력을 하도록 도와준다.
for j in range(10001):
    if result[j] != 0:
        for k in range(result[j]):
            print(j)
