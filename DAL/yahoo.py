__author__ = 'ict'

import os

from DAL.driver.csv import CSV
from DAL.VDC.yahoo import Yahoo


def csv(path, option):
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
    vdc.create(data=option)
    return vdc.get_data()