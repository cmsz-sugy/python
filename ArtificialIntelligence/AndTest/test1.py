

input_v =[1,0]
weights = [0.1,0.1]
rate =0.1
delta=-1
weight = map(
            lambda (x, w): w + rate * delta * x,
            zip(input_v, weights))
print weight