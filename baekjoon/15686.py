# Gold 5
# Brute Force
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().strip().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            houses.append((i, j))
        if array[i][j] == 2:
            chickens.append((i, j))

# [((1, 2), (2, 2)), ((1, 2), (4, 4)), ((2, 2), (4, 4))]
def get_city_chicken(houses, chicken):
    # houses: 집들 좌표 목록
    # chicken: 선택된 치킨 집들 목록
    city_chicken = 0
    for house in houses:
        house_chicken = 2*N # 최대값 초기화
        for c in chicken:
            house_chicken = min(abs(c[0]-house[0])+abs(c[1]-house[1]), house_chicken)
        city_chicken += house_chicken
    return city_chicken

result = int(1e9)
answer = M
for m in range(1, M+1):
    combination = list(combinations(chickens, m))
    for chicken in combination:
        city_chicken = get_city_chicken(houses, list(chicken))
        if city_chicken < result:
            answer = m
            result = city_chicken
        if city_chicken == result: # 거리는 같으나 개수 많은 경우
            if answer < m:
                answer = m
print(result)