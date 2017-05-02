# -*- coding: utf-8 -*-
def update(mean1, var1, mean2, var2):
    new_mean = (1.0 / (var1 + var2)) * ((mean1 * var2) + (mean2 * var1))
    new_var = 1.0 / ((1.0 / var1) + (1.0 / var2))
    return [new_mean, new_var]

def predict (mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)

print (mu, sig)