# def find(parent, x):
#     if parent[x] != x:
#         return find(parent, parent[x])
#     return parent[x]
#
#
# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
#
# n, k, m = map(int, input().split())  # 창고 수, 회사 수, 도로 수
#
# arr = list(map(int, input().split()))  # i번 창고 Ci번 회사
# house = defaultdict(list)
# parent = [i for i in range(n + 1)]
# edges = []
#
# for i in range(len(arr)):
#     house[arr[i]].append(i + 1)
#
# print(house)
#
# for _ in range(m):
#     x, y, w = map(int, input().split())  # x번 y번 창고 연결 비용 w
#     edges.append((w, x, y))
#
# # A 창고 1, 3, 4 / B 창고 2, 5
# # 1번 10, 2번 3
# # (1번) : 1 -> 5 -> 3, 4 = 6 + 1 + 3 = 10
# # (2번) : 2 -> 3 -> 5 = 2 + 1 = 3
#
# edges.sort()
# print(edges)
# answer = 0
#
# for cost, a, b in edges:
#     if find(parent, a) != find(parent, b):
#         union(parent, a, b)
#
# print(limits)
#
#
#
# 물류창고가 1번 회사는 1,3,4번 창고를 갖고 있어서
# 창고 1 -> 5 연결하면 6
# 5번에서 3번, 4번 연결할 수 있고 각각 비용이 1, 3 해서
# 총합 10이 나온다
#
# 2번 회사는 2,5 창고를 갖고 있고
# 2 -> 3번까지 연결 후
# 3번에서 5번연결해서 2 + 1 = 3 나온다 코드 수정해줘