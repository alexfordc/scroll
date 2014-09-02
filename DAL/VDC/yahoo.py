__author__ = 'ict'

date_offset = 0
price_offset = 6


class Yahoo:
    def __init__(self, drivers=None):
        self.drivers = drivers
        self.data = {}

    def create(self, drivers=None):
        if drivers is None:
            drivers = self.drivers
        if drivers is None:
            raise Exception("Need input a list of drivers")
        date_set = set()
        tmp_dict = {}
        for dv in drivers:
            tmp_data = {}
            loaded = True
            if not dv.done():
                loaded = False
                dv.load()
            for item in dv.get_data():
                date = int(item[date_offset])
                tmp_data[date] = float(item[price_offset])
                date_set.add(date)
            tmp_dict[dv.get_tag()] = tmp_data
            if not loaded:
                dv.clean()
        date_list = [int(date) for date in list(date_set)]
        date_list.sort()
        for stock_id, tmp_data in tmp_dict.items():
            price_list = []
            zero_start = False
            nozero = 0
            for date in date_list:
                if date in tmp_data:
                    if zero_start and nozero == 0:
                        nozero = len(price_list)
                    price_list.append(tmp_data[date])
                elif len(price_list) == 0:
                    price_list.append(0)
                    zero_start = True
                else:
                    price_list.append(price_list[-1])
            if zero_start:
                for i in range(nozero):
                    price_list[i] = price_list[nozero]
            self.data[stock_id] = price_list

    def data(self, stock_id):
        if stock_id not in self.data:
            return None
        return self.data[stock_id]

    def get_data(self):
        return self.data