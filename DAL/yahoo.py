__author__ = 'ict'

import os
import mysql.connector

from DAL.driver.csv import CSV
from DAL.driver.mysqldb import MySQL
from DAL.VDC.yahoo import Yahoo


def csv(path, option, align=True):
    if path[-1] != os.path.sep:
        path += os.path.sep
    if not os.path.isdir(path):
        raise NotADirectoryError("No such directory: " + path)
    drivers = []
    for file in os.listdir(path):
        if file[-4:].lower() != ".csv":
            continue
        drivers.append(CSV(path + file))
    vdc = Yahoo(drivers)
    vdc.create(option=option, align=align)
    return vdc.get_data()


def mysqldb(host, user, password, database, option, align=True):
    con = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute("show tables")
    drivers = []
    for t in cur:
        drivers.append(MySQL(host, user, password, database, t[0]))
    vdc = Yahoo(drivers)
    vdc.create(option=option, align=align)
    return vdc.get_data()