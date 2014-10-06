__author__ = 'ict'

import random
from calculate.distance.core import method


def kmeans(data_dict, k, distance="euclid", seed=None):
    cluster = {}
    c_cluster = {}
    dim = None
    if seed is not None:
        seed_set = set(seed)
    else:
        seed_set = set(data_dict)
    for i in range(k):
        choose = random.choice(list(seed_set))
        seed_set.remove(choose)
        c_cluster[i] = data_dict[choose]
    for key, data in data_dict.items():
        min_dist = float("inf")
        dim = len(data)
        nearest = None
        for i in range(k):
            dist = method(distance, data, c_cluster[i])
            if dist < min_dist:
                min_dist = dist
                nearest = i
        if nearest not in cluster:
            cluster[nearest] = []
        cluster[nearest].append(key)
    change = True
    while change:
        change = False
        for i in range(k):
            c_cluster[i] = [0] * dim
            for key in cluster[i]:
                for j in range(dim):
                    c_cluster[i][j] += data_dict[key][j]
            c_cluster[i] = [c_cluster[i][_i] / len(cluster[i]) for _i in range(dim)]
        _cluster = {}
        for key, data in data_dict.items():
            min_dist = float("inf")
            dim = len(data)
            nearest = None
            for i in range(k):
                dist = method(distance, data, c_cluster[i])
                if dist < min_dist:
                    min_dist = dist
                    nearest = i
            if nearest not in _cluster:
                _cluster[nearest] = []
            _cluster[nearest].append(key)
        if _cluster != cluster:
            change = True
        cluster = _cluster
    rst = set()
    for _, cls in cluster.items():
        rst.add(frozenset(cls))
    return rst


def bikmeans(data_dict, k, distance="euclid"):
    cluster = [[]]
    cluster_center = {}
    c_cluster0 = None
    dim = None
    for _, data in data_dict.items():
        if c_cluster0 is None:
            c_cluster0 = data
            dim = len(c_cluster0)
        else:
            c_cluster0 = [c_cluster0[i] + data[i] for i in range(dim)]
    c_cluster0 = [c_cluster0[i] / len(data_dict) for i in range(dim)]
    cluster_id = 0
    cluster_center[cluster_id] = c_cluster0
    for key in data_dict:
        cluster[cluster_id].append(key)
    while cluster_id + 1 < k:
        delta_sse = -1
        min_sse_cluster = None
        min_sse_index = None
        min_sse_c_a = None
        min_sse_c_b = None
        for i in range(cluster_id + 1):
            if len(cluster[i]) < 2:
                continue
            a_i = random.randint(0, len(cluster[i]) - 1)
            b_i = random.randint(0, len(cluster[i]) - 1)
            while a_i == b_i:
                b_i = random.randint(0, len(cluster[i]) - 1)
            c_a = data_dict[cluster[i][a_i]]
            c_b = data_dict[cluster[i][b_i]]
            cluster_a = []
            cluster_b = []
            for key in cluster[i]:
                if method(distance, data_dict[key], c_a) < method(distance, data_dict[key], c_b):
                    cluster_a.append(key)
                else:
                    cluster_b.append(key)
            change = True
            while change:
                change = False
                c_a = [0] * dim
                c_b = [0] * dim
                for key in cluster_a:
                    for _i in range(dim):
                        c_a[_i] += data_dict[key][_i]
                for key in cluster_b:
                    for _i in range(dim):
                        c_b[_i] += data_dict[key][_i]
                c_a = [c_a[_i] / len(cluster_a) for _i in range(dim)]
                c_b = [c_b[_i] / len(cluster_b) for _i in range(dim)]
                _cluster_a = []
                _cluster_b = []
                for key in cluster[i]:
                    if method(distance, data_dict[key], c_a) < method(distance, data_dict[key], c_b):
                        _cluster_a.append(key)
                    else:
                        _cluster_b.append(key)
                if _cluster_a != cluster_a:
                    change = True
                    cluster_a = _cluster_a
                    cluster_b = _cluster_b
            tmp_cluster = cluster.copy()
            tmp_cluster[i] = cluster_a
            tmp_cluster.append(cluster_b)
            sse_split = 0
            see_nosplit = 0
            for key in cluster_a:
                sse_split += method(distance, data_dict[key], c_a) ** 2
            for key in cluster_b:
                sse_split += method(distance, data_dict[key], c_b) ** 2
            for key in cluster[i]:
                see_nosplit += method(distance, data_dict[key], cluster_center[i]) ** 2
            if see_nosplit - sse_split > delta_sse:
                delta_sse = see_nosplit - sse_split
                min_sse_cluster = tmp_cluster
                min_sse_index = i
                min_sse_c_a = c_a
                min_sse_c_b = c_b
        cluster = min_sse_cluster
        cluster_center[min_sse_index] = min_sse_c_a
        cluster_id += 1
        cluster_center[cluster_id] = min_sse_c_b
    rst = set()
    for cls in cluster:
        rst.add(frozenset(cls))
    return rst