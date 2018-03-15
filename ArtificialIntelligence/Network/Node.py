#encoding: utf-8
#节点类，负责记录节点的层数，节点的index，以及输出，上下游链接，实现输出值和误差值
import numpy as np
class Node(object):
    def __init__(self,layer_index,node_index):
      '''构造节点对象'''
      self.layer_index = layer_index #层数
      self.node_index = node_index #节点index
      self.upstream = []
      self.downstream = []
      self.output = 0
      self.delta = 0

    def sigmoid(inputs):
        """
        Calculate the sigmoid for the give inputs (array)
        :param inputs:
        :return:
        """
        sigmoid_scores = [1 / float(1 + np.exp(- x)) for x in inputs]
        return sigmoid_scores
    def set_output(self,output):
        '''
                设置节点的输出值。如果节点属于输入层会用到这个函数。
                '''
        self.output = output

    def append_downstream_connection(self, conn):
        '''
        添加一个到下游节点的连接
        '''
        self.downstream.append(conn)

    def append_upstream_connection(self, conn):
        '''
        添加一个到上游节点的连接
        '''
        self.upstream.append(conn)

    def calc_output(self):
        '''
        根据式1计算节点的输出
        '''
        output = reduce(lambda ret, conn: ret + conn.upstream_node.output * conn.weight, self.upstream, 0)
        self.output = self.sigmoid(output)

    def calc_hidden_layer_delta(self):
        '''
        节点属于隐藏层时，根据式4计算delta(节点的误差)
        '''
        downstream_delta = reduce(
            lambda ret, conn: ret + conn.downstream_node.delta * conn.weight,
            self.downstream, 0.0)
        self.delta = self.output * (1 - self.output) * downstream_delta

    def calc_output_layer_delta(self, label):
        '''
        节点属于输出层时，根据式3计算delta
        '''
        self.delta = self.output * (1 - self.output) * (label - self.output)

    def __str__(self):
        '''
        打印节点的信息
        '''
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.output, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        upstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.upstream, '')
        return node_str + '\n\tdownstream:' + downstream_str + '\n\tupstream:' + upstream_str