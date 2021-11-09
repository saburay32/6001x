import numpy # импортируем библиотеку
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]
d = [int(s) for s in input().split()]
M1 = numpy.array([a[:4],b[:4],c[:4],d[:4]])
v1 = numpy.array([a[-1],b[-1],c[-1],d[-1]])
if numpy.linalg.det(M1)!=0:
    z =numpy.linalg.solve(M1,v1)
    print(float(z[0]),float(z[1]),float(z[2]),float(z[3]))
else:
    print( "Матрица системы вырожденная")

#------------
# import numpy
# a11, a12, b1 = input().split()
# ....
# M1 = numpy.array([...]) # Матрица (левая часть системы)
# v1 = numpy.array([...]) # Вектор (правая часть системы)
# r = numpy.linalg.solve(...) #Находим решение системы
# print (r[0], r[1])
#---------
# L1 = [['one', 'two', 'three'], [1, 2, 3, 4, 5, 6]]
# # L3 = list()
# # for i in L1:
# #     x = len(i)
# #     for y in range(x):
# #         L3.append(i[y])
# L2=[j for i in L1 for j in i]
# # L2 = [i for i in L3 if i!='']
#
# print(L2)


# import re
# z =re.split('[^a-z]',input())
# print(z)

#print(input().lower())

#print(' '.join([line[0] for line in open(r'dataset_48784_9.txt', 'r')]))

#     y=0
#     f = file.read()
#     z+=(f[0]+' ')
#     for i in f:
#         if y==1:
#             z += (i + ' ')
#             y = 0
#         elif i =='\n':
#             y+=1
#
# f = open('newfile.txt', 'w')
# f.write(str(z))
# f.close()

        # if y==0:
        #     pass
        # else:
        #     z+=(i+' ')
        #     y=0
        # if i =='\n':
        #     y+=1



#print(z)

#S = 'Some string'
#L = input().split() # ['Some', 'string']
# ans = str()
# for i in input().split():
#     ans+=(i[0]+" ")
#
# print(ans)
