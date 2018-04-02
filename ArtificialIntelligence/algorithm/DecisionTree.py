# -*- encoding: utf-8 -*-
import math
def getEntropy(Probability):
    result = float(0.0)
    for it in Probability:
        # print math.log(it,2)
        # print it
        result += float((-1)*it*math.log(float(it),2))
    return  round(result,4)
def getInfoGain (nowProb,lastProb):
     return  nowProb-lastProb
def getIndexProb(entropy):
    result = 0.0
    for (item,ownentropy) in entropy:
       result+=item*ownentropy
    return round(result,4)
if __name__ =='__main__':
    entropy_outlook = []
    Probability_sunny = [2/float(5),3/float(5)]
    Probability_overcast = [1]
    Probability_rainy = [2 / float(5), 3 / float(5)]
    Probability_play = [5 / float(14), 9 / float(14)]
    entropy_outlook.append(getEntropy(Probability_sunny))
    entropy_outlook.append(getEntropy(Probability_overcast))
    entropy_outlook.append(getEntropy(Probability_rainy))
    proportion = [5/float(14),4/float(14),5/float(14)]
    Entropy = zip(entropy_outlook,proportion)
    nowProb =  getIndexProb(Entropy)
    lastProb = getEntropy(Probability_play)
    print  getInfoGain(nowProb,lastProb)

