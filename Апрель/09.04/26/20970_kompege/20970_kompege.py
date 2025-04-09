# f = open('26_20970.txt')
# n, k = map(int, f.readline().split())
# m = [[] for _ in range(k)]
# clients = [list(map(int, line.split())) for line in f.readlines()]
# clients.sort()
# util = 0
# for i in range(len(clients)):
#     start, duration, need_num = clients[i]
#     if need_num == 0:
#         min_queue_num = 10000
#         min_queue_ind = None
#         for j in range(len(m)):
#             queue_num = 0
#             for k in range(len(m[j])):
#                 if start < m[j][k]:
#                     queue_num += 1
#             if queue_num < min_queue_num:
#                 min_queue_num = queue_num
#                 min_queue_ind = j
#         if min_queue_num < 5:
#             if m[min_queue_ind] == []:
#                 cur_end = start + duration
#             else:
#                 cur_end = max(max(m[min_queue_ind]), start) + duration
#             m[min_queue_ind].append(cur_end)
#         else:
#             util += 1
#     else:
#         queue_num = 0
#         for k in range(len(m[need_num - 1])):
#             if start < m[need_num - 1][k]:
#                 queue_num += 1
#         if queue_num < 5:
#             if m[need_num - 1] == []:
#                 cur_end = start + duration
#             else:
#                 cur_end = max(max(m[need_num - 1]), start) + duration
#             m[need_num - 1].append(cur_end)
#         else:
#             util += 1
# print(len(max(m, key=len)))
# print(util)



























f = open('26_20970.txt')

