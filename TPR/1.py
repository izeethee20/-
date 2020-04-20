# import numpy as np
#
# print("enter number of alternatives:")
# num = int(input())
#
#
#
# print("enter your ",num,"x 3 alternatives:")
# for i in range(num):
#     for j in range(3):
#         x = input()
#         k = float(x - 1.2)/(3.5-1.2)
#
#
#
#
import numpy as np

a = [[1.2,1.5,1.6,1.6,1.8,1.8,1.9,2.0,2.4,3.5],
     [101,110,120,142,133,121,124,152,213,232],
     [6800,7200,6900,7700,6400,6700,6700,8000,7500,9500]]
# res = a[2][0]
# print("Неплохие варианты по второстепенным критериям:")
# for i in range(3):
#     for j in range(10):
#         if i == 0:
#             if a[i][j] >=1.6 and a[i+1][j] >=133:
#                 print(a[i][j],a[i+1][j])
#                 print()
#                 if a[i+2][j] < res:
#                     res = a[i+2][j]
#                     k1 = a[i][j];
#                     k2 = a[i + 1][j]
#
# print("Но лучший выбор это авто с такими характеристиками:",k1,k2,res)


print("k1:")
for i in range(3):
    for j in range(10):
        if i == 0:
            k_1 = np.array((a[i][j]-1.2)/(3.5-1.2))
            print("%.2f" % k_1)

print("k2:")
for i in range(3):
    for j in range(10):
        if i == 1:
            k_2 = np.array((a[i][j] - 101) / (232 - 101))
            print("%.2f" % k_2)

print("k3:")
for i in range(3):
    for j in range(10):
        if i == 2:
            k_3 = np.array((a[i][j] - 6400) / (9500 - 6400))
            print("%.2f" % k_3)




















# # print("enter your alternatives:")
# # for i in range(1,10):
# #     print("x",i,"=")
# #     x[i]=float(input())
# #
# print("enter number of alternatives:")
# num = int(input())
#
# print("enter your ",num,"x3 alternatives:")
# x=[]
# x_new=[]
# for i in range(3):
#     x = []
#     for j in range(num):
#         x[i].append(float(input()))
#         if(x[i]<3):
#             x_new = (x[i]-x[0]/x[num]-x[0])
# # x_new=[[]]
# # for i in range(3):
# #     x.append([])
# #     for j in range(num):
# #         x_new=x[[]]
#
# print(x)
# print(x_new)
# #
# # x = [[ float(input()) for i in range(num)] for j in range(3)]
#
#
# #         x = float(input())
#
# # for i in range (1,num):
# #     for j in range(1,3):
# #         x_new = max()
#
# # for i in range (0,num):
# #     for j in range(0,3):
# #         print(x[i][j])