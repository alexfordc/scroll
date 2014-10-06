__author__ = 'ict'

import DAL.yahoo
from calculate.cluster.kmeans import kmeans
import interface.console.print_cluster

data = DAL.yahoo.csv(r"e:\stockdata", "adjclose")
interface.console.print_cluster.print_cluster(kmeans(data, 50))