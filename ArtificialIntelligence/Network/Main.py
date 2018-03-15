
#encoding: utf-8

import datetime
import ImageLoader,Network

def get_training_data_set():
    '''
    获得训练数据集
    '''
    image_loader = ImageLoader('train-images.idx3-ubyte', 60000)
    label_loader = ImageLoader('train-labels.idx1-ubyte', 60000)
    return image_loader.load(), label_loader.load()
def get_test_data_set():
    '''
    获得测试数据集
    '''
    image_loader = ImageLoader('t10k-images.idx3-ubyte', 10000)
    label_loader = ImageLoader('t10k-labels.idx1-ubyte', 10000)
    return image_loader.load(), label_loader.load()
def get_result(vec):
        max_value_index = 0
        max_value = 0
        for i in range(len(vec)):
            if vec[i] > max_value:
                max_value = vec[i]
                max_value_index = i
        return max_value_index
def evaluate(network, test_data_set, test_labels):
    error = 0
    total = len(test_data_set)
    for i in range(total):
        label = get_result(test_labels[i])
        predict = get_result(network.predict(test_data_set[i]))
        if label != predict:
            error += 1
    return float(error) / float(total)
def train_and_evaluate():

    last_error_ratio = 1.0
    epoch = 0
    train_data_set, train_labels = get_training_data_set()
    test_data_set, test_labels = get_test_data_set()
    network = Network([784, 300, 10])
    while True:
        epoch += 1
        network.train(train_labels, train_data_set, 0.3, 1)
        print '%s epoch %d finished' % (datetime.datetime.now(), epoch)
        if epoch % 1 == 0:
            error_ratio = evaluate(network, test_data_set, test_labels)
            print '%s after epoch %d, error ratio is %f' % (datetime.datetime.now(), epoch, error_ratio)
            if error_ratio > last_error_ratio:
                break
            else:
                last_error_ratio = error_ratio
if __name__ == '__main__':
    train_and_evaluate()