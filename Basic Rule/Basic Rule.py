# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:45:25 2017 

@author: lijunli
"""

import os 
os.chdir('D:/学生成绩预测李军利')

def Weight_score():
    file_score = open("data/Score Predict.csv") # 将原来的txt文件按学号从大到小排序后保存为csv文件
    file_result = open("Basic Rule/result/35 and 65 of rank.txt", "w")
    factor = [0.35, 0.65]#列表
    stu = {}#集合
    first_line = 0
    for line in file_score:
        if first_line == 0:
              first_line = 1
              continue # 第一行是 学期 学号 排名，要先排除第一行
        sem, id, rank = line.strip("").split(",")
        stu.setdefault(id, 0)
        # 第一学期：rank * 0.35, 第二学期：rank * 0.65
        stu[id] += int(rank) * factor[int(sem)-1]
    Ranked = sorted(zip(stu.values(), stu.keys()))  # 按得到的名次排序，id在后
    file_result.write("id,rank\n")
    i = 1
    for line in Ranked:
        file_result.write(line[1] + "," + str(i) + "\n")
        i = i + 1
    file_score.close()
    file_result.close()
'''
变量类型：
    file_score: file object
    file_result: file object
    factor: list of floats
    stu: dictionary with string keys and integer values：键是学生的id，键值是对应的成绩
    first_line: integer
    sem: string
    id: string
    rank: string
    Ranked: list of tuples, with integer values and string keys
    i: integer
1.' sem, id, rank = line.strip("").split(",")'的语法是什么？分别是 学期、学号、排名 三个都是string类型
2. setfault函数的使用：
stu.setdefault(id, 0)解释
stu是一个字典，id是一个字符串，查找是否有id这个字符串对应的键，有就把对应的键值变成0，没有就把这对添加进去

3.sorted函数的使用方式：
zip函数的用法：
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
sorted函数对元组进行排序：
>>> a = [(2, 3), (6, 7), (3, 34), (24, 64), (1, 43)]
>>> sorted(l, key=getKey)
[(1, 43), (2, 3), (3, 34), (6, 7), (24, 64)]

4.write函数：
ranked是一个个元组组成的列表，line就是每一个元组（名次，id），line[1]就是id，str(i)就是这个id对应的名次
'''
if __name__ == '__main__':
    Weight_score() # 第一二学期排名乘以权重
