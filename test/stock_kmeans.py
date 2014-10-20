__author__ = 'ict'

import DAL.yahoo
from calculate.cluster.kmeans import kmeans
from calculate.feature.core import method
import interface.console.print_cluster

data = DAL.yahoo.mysqldb("219.223.251.24", "root", None, "stock", "adjclose")
for key in data:
    data[key] = method("price return", data[key])
interface.console.print_cluster.print_cluster(kmeans(data, 100))