#encoding: utf-8
class preceptron(object):
    def __init__(self):
        self.bias = 0.0
        self.weights = [0.0 for _ in range(2)]

    def  step_function(self,level):
        if level >0.0:
            return 1
        else:
            return 0
    def  parameter_accumulation(list2,weights):
         return  reduce(lambda x, y: x + y, map(lambda (x,y):x*y,zip(list2,weights)))

    # def __str__(self):
    #     return  'weights: %s\nbias: %f ' %(self.weight,self.bias)
    def activiact(self,input_vec):
        product =0.0
        for i in range(len(input_vec)):
            product += input_vec[i] * self.weights[i]
        product += self.bias
        output = self.step_function(product)
        return output
    def train(self,rate,lable,input_vec,output):
        # self.bias = 0.0
        # self.weights = []
        for i in range(len(input_vec)):
            self.weights[i] += (rate*(lable-output)*input_vec[i])
        self.bias+=(rate*(lable-output))
        # print self.bias,self.weights
        return self
    def train_time(self,input_vec,lables):
       sample = zip(input_vec,lables)
       for (input_vec,lable) in sample:
           output = self.activiact(input_vec)
           self.train(0.1,lable,input_vec,output)
           # print '改变之前：'
           # print self.weights,self.bias
           # output = self.activiact(input_vec,self.weights,self.bias)
           # print '改变之后：'
           # print self.weights, self.bias
       return self
    def _one_iteration(self,iteration,input_vec,lables):
        for i in range(iteration):
            # print'第%s次改变' % str(i+1)
            self.train_time(input_vec,lables)

if __name__ == '__main__':
    preceptron_main =preceptron()
    input_vec = [[1,1],[1,0],[0,1],[0,0]]
    lables = [1,0,0,0]
    preceptron_main._one_iteration(10,input_vec,lables)
    print 'bias:' + str(preceptron_main.bias)
    print 'weights:' + str(preceptron_main.weights)

    print '1 and 1 = ' +str(preceptron_main.activiact([1,1]))
    print '1 and 0 = ' +str(preceptron_main.activiact([1,0]))
    print '0 and 1 = ' +str(preceptron_main.activiact([0,1]))
    print '0 and 0 = ' +str(preceptron_main.activiact([0,0]))


  # #===============================开始训练
  #   preceptron_main.train(rate,lables[0],input_vec,output)
  #   print  preceptron_main.weights
  #   print  preceptron_main.bias
    # print zip(input_vec,weights)
    # print map(lambda (x,y):x*y,[([1, 1], 0.0)])
    # # product =  reduce(lambda x, y: x + y, map(lambda (x,y):x*y,zip(input_vec,weights)))
    # print product
    # output = product +bias
