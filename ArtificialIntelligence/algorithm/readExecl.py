# -*- encoding: utf-8 -*-
import xlrd
def getData(Dataroute):
  data =xlrd.open_workbook('F:/py_workpace/dataTest/test.xlsx')
  table = data.sheets()[0]
  return table
#   nrows = table.nrows #行数
#   ncols = table.ncols #列数
#   for i in xrange(0,nrows):
#     rowValues= table.row_values(i) #某一行数据
#     for item in rowValues:
# 　　　  print item
