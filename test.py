__author__ = 'levitan'

import kNN
import trees
import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import treePlotter

# group, labels = kNN.createDataSet()
# #print group, labels
# print kNN.classify0([0,0],group,labels,3)

# datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
# normMat,ranges,minVals=kNN.autoNorm(datingDataMat)
#
#
#         # print datingDataMat
# # print datingLabels[0:10]
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(normMat[:, 0], normMat[:, 1], s=15*array(datingLabels),c=array(datingLabels))
# plt.show()

#kNN.datingClassTest()

#kNN.classifyPerson()

# testVector=kNN.img2vector('testDigits/0_13.txt')
# print testVector[0,0:31]

# kNN.handwritingClassTest()

# myDat,labels=trees.createDataSet()
# #print trees.chooseBestFeatureToSplit(myDat)
# myTree=trees.createTree(myDat,labels)
# myTree=treePlotter.retrieveTree(0)
# # print treePlotter.getNumLeafs(myTree), treePlotter.getTreeDepth(myTree)
# myTree['no surfacing'][3]='maybe'
# treePlotter.createPlot(myTree)
# print  trees.classify(myTree,labels,[1,1])
# trees.storeTree(myTree,'classifierStorage.txt')
# print trees.grabTree('classifierStorage.txt')

fr=open('lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age','prescript','astigmatic','tearRate']
lensesTree=trees.createTree(lenses,lensesLabels)
print lensesTree
treePlotter.createPlot(lensesTree)