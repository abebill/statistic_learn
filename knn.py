#--*-- coding:utf-8 --*--

from numpy import *

def knn(input, train_datas, label, k, p = 2):
    dataSize = train_datas.shape[0]

    #距离计算
    diff = tile(input,(dataSize,1)) - train_datas
    sqdiff = diff ** p   #默认p为2，即欧式距离
    squareDistance = sum(sqdiff,axis = 1)
    dist = squareDistance ** (float(1) / p)

    sortedDistIndex = dist.argsort() #将dist中的元素从小到大排列,并返回该元素之前的索引值

    classCount = {}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        #对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1

    #选取出现的类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    print '输入实例属于：'+ str(classes) + '类，其该类近邻数有',str(maxCount) + '个'

if __name__ == '__main__':
    x = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    y = ['A','A','B','B']
    i = array([0.1,0.1])
    knn(i, x , y ,k=3,p=1)
