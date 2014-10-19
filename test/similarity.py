__author__ = 'mac'

import calculate.similarity.core

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

method_str = "euclid, manhattan, chebyshev, minkowski, cos, pearson"

option = [None, None, None, 10, None, None, None]

print(calculate.similarity.core.method(method_str, list_a, list_b, option))