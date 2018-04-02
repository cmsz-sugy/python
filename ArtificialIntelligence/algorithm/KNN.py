#encoding: utf-8
from numpy import  *
from sklearn import preprocessing
import  operator

def creatDateSet():
    group = array([[2,2],[1,1],[0.5,0.5],[3,3]])
    group_scale = preprocessing.scale(group, axis=0, with_mean=True,with_std=True,copy=True)#标准化
    group_normalized = preprocessing.normalize(group, norm='l2')#归一化

    labels = ['A','A','B','B']
    return group_normalized,labels

def getDistence(inX,dateSet):#inX为输入的样本，dateSet为测试样本

    dateSetSize = len(dateSet)
    diffMat = tile(inX,(dateSetSize,1))-dateSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortDistance = distance.argsort()
    return  sortDistance

if __name__ == '__main__':
   dateSet , labels = creatDateSet()
   inX = [0,0]
   k =3
   sortDistance = getDistence(inX,dateSet)
   classCount = {}
   for i in range(k):
       voteLabel = labels[sortDistance[i]]
       classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
   sorted(classCount.values())
   print  classCount.keys()
