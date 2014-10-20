__author__ = 'ict'

from DAL.driver.base import Base
import mysql.connector


class MySQL(Base):
    def __init__(self, host=None, user=None, password=None, database=None, table=None):
        Base.__init__(self)
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    def load(self, host=None, user=None, password=None, database=None, table=None):
        if host is None:
            host = self.host
        if user is None:
            user = self.user
        if password is None:
            password = self.password
        if database is None:
            database = self.database
        if table is None:
            table = self.table
        if host is None:
            raise Exception("Need input host of mysql")
        if user is None:
            raise Exception("Need input username of mysql")
        if database is None:
            raise Exception("Need input database of mysql")
        if table is None:
            raise Exception("Need input data table")
        self.tag = table
        con = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        select = "select * from " + table
        cur.execute(select)
        for l in cur:
            self.data.append(list(l))
        cur.close()
        con.close()
        self.loaded = True

    def save(self, dal_driver, host=None, user=None, password=None, database=None, table=None):
        if host is None:
            host = self.host
        if user is None:
            user = self.user
        if password is None:
            password = self.password
        if database is None:
            database = self.database
        if table is None:
            table = self.table
        if host is None:
            raise Exception("Need input host of mysql")
        if user is None:
            raise Exception("Need input username of mysql")
        if database is None:
            raise Exception("Need input database of mysql")
        if table is None:
            raise Exception("Need input data table")
        loaded = True
        if not dal_driver.done():
            dal_driver.load()
            loaded = False
        data = dal_driver.get_data()
        if not loaded:
            dal_driver.clean()
        length = 0
        for d in data:
            if len(d) > length:
                length = len(d)
        con = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        create = "create table " + table + " ("
        for i in range(length - 1):
            create += "data%d varchar(255)," % i
        create += "data%d varchar(255))" % (length - 1)
        cur.execute(create)
        for d in data:
            insert = "insert into " + table + " ("
            for i in range(len(d) - 1):
                insert += "data%d, " % i
            insert += "data%d) " % (len(d) - 1)
            insert += "values ("
            for i in range(len(d) - 1):
                insert += "'%s', " % d[i]
            insert += "'%s')" % d[len(d) - 1]
            cur.execute(insert)
        con.commit()
        cur.close()
        con.close()