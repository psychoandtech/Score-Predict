# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 07:42:33 2017 

@author: lijunli
"""


from operator import itemgetter
import os
os.chdir('D:/学生成绩预测李军利')
'''
os.chdir函数的作用：
将目录更改为路径，路径：通过路径来加载文件
'''
WRITE = 1
Weights = [0.9, 0.1]
                       
file_score1 = open("Lasso Rank/result/LassoRank(0018).txt")
file_score2 = open("Basic Rule/result/35 and 65 of rank.txt")

file_score_write = open("bagging_(Lasso Rank)"+str(Weights[0])+"_Basic Rule"+str(Weights[1])+".txt", "w")
'''
open函数的作用：参数：一个是路径
'w'即使文件存在，也会重新创建一个进行 写 的操作
open函数返回list类型
'''
def Read_Score(file_score):
    first_line = 0
    score = {}
    for line in file_score:
        if first_line == 0:
            first_line = 1
            continue
        line_cur = line.strip().split(", ")
        score[line_cur[0]] = float(line_cur[1])
    file_score.close()
    return(score)
'''
Read_Score对文件进行输入处理
file_score的类型：txt
strip（）：参数为空时默认删除字符串中的空格
split（','）:以传入的参数为分界，对字符串分割成一个个元素，放进列表中（['aaa','bbb','ccc'])
 score[line_cur[0]] = float(line_cur[1])：
 键名是line_cur[0] 将键值设置为line_cur[1]
'''

def Merge(s1, s2, x1, x2):
    new_score = {}
    for stu in s1:
        if stu in s2:
            new_score[stu] = x1 * s1[stu] + x2 * s2[stu]
        else:
            new_score[stu] = s1[stu]
    file_score1.close()
    file_score2.close()
    return(new_score)
'''
综合两次成绩进行加权
返回一个字典，键名是学生名，键值是成绩
'''

def Test(real_rank, predict_rank):
    error = 0.0
    first_line = 0
    predict_rank.seek(0)
    for line in predict_rank:
        if first_line == 0:
            first_line = 1
            continue
        line_cur = line.split(", ")
        id = int(line_cur[0])
        rank = int(line_cur[1])
        error += pow(rank-real_rank[id], 2) * 6
    error = 1 - (error * 1.0) / ((91 * 91 - 1) * 91)
    return(error)



if __name__ == "__main__":
    score1 = Read_Score(file_score1)
    score2 = Read_Score(file_score2)
    score = Merge(score1, score2, Weights[0], Weights[1])
    print(score1)
    print(score2)
    print(score)
    if WRITE == 1:
        I = []#二维列表
        for i in score:
            I.append((i, score[i]))
        I = sorted(I, key = itemgetter(1))
        print(I)
        rank = {}
        for i in range(0, 91):
            rank[I[i][0]] = i + 1
        file_score_write.write("id, rank\n")
        print(len(rank))
        for stu in rank:
            file_score_write.write(str(stu)+", "+str(rank[stu])+'\n')
        print(rank)
    file_score_write.close()
 '''
 列表的append函数：这里添加的是元组：(i, score[i])
 列表的sorted函数：第一个参数是I，即排序的对象；key = itemgetter(1)；默认是升序reverse=False
 itemgetter函数：返回下标为1的元素
 在这里是对score[i]为对象进行排序
 '''
