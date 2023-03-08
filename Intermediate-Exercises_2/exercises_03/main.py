import numpy as np
import numpy.random

float_list = np.array(numpy.random.random_sample(10))

print(float_list)
print("Mean: {}, Median: {}, Standard Deviation: {}".format(numpy.mean(float_list), numpy.median(float_list),
                                                            numpy.std(float_list)))
