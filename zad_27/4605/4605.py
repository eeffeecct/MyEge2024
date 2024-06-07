from math import ceil

f = open('zad_27/4605/27A_4605.txt')
N = int(f.readline())
K = 9999994
road = [0] * K
for l in f: 
    km, p = map(int, l.split())
    road[km - 1] = ceil(p / 36)

cost = 0
for i in range(1, K):
    cost += i * road[i]

right = sum(road[1:])
total = sum(road)
costs = [cost]
for i in range(1, K):
    cost = cost - right + (total - right)
    if road[i] != 0:
        costs.append(cost)
    right -= road[i]
print(min(costs))
