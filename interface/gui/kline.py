__author__ = 'ict'

from tkinter import Tk
from tkinter import Canvas

open_offset = 0
high_offset = 1
low_offset = 2
close_offset = 3

x_offset = 0
block_y_low = 1
block_y_high = 2
line_y_low = 3
line_y_high = 4
status_offset = 5

up = 1
down = -1


class Kline:
    def __init__(self, width=1280, height=800, title="K line"):
        self.data = []
        self.height = height
        self.width = width
        self.title = title
        self.block = []
        self.block_width = 0
        pass

    def stock_data(self, data_list):
        self.data = list(data_list)

    def draw(self):
        main = Tk()
        main.title(self.title)
        can = Canvas(main, bg="black", height=self.height, width=self.width)
        for b in self.block:
            bx1 = b[x_offset]
            bx2 = bx1 + self.block_width
            by1 = b[block_y_low]
            by2 = b[block_y_high]
            lx = (bx1 + bx2) / 2
            ly1 = b[line_y_low]
            ly2 = b[line_y_high]
            if b[status_offset] == up:
                color = "red"
            else:
                color = "green"
            if by1 - by2 == 0:
                by2 += 2
                color = "yellow"
            can.create_rectangle([bx1, self.height - by1, bx2, self.height - by2], fill=color)
            can.create_line([lx, self.height - ly1, lx, self.height - ly2], fill=color)
        can.pack()
        main.mainloop()

    def create_block(self):
        block_width = self.width / len(self.data)
        if block_width == 0:
            raise Exception("GUI is too small")
        self.block_width = block_width
        mi_list = []
        ma_list = []
        for n_list in self.data:
            mi_list.append(min(n_list[: 4]))
            ma_list.append(max(n_list[: 4]))
        mi = min(mi_list)
        ma = max(ma_list)
        scale = self.height / (ma - mi)
        x = 0
        for n_list in self.data:
            s_open = n_list[open_offset]
            s_high = n_list[high_offset]
            s_low = n_list[low_offset]
            s_close = n_list[close_offset]
            x += self.block_width
            if s_open <= s_close:
                status = up
                byh = scale * (s_close - mi)
                byl = scale * (s_open - mi)
            else:
                status = down
                byh = scale * (s_open - mi)
                byl = scale * (s_close - mi)
            lyh = scale * (s_high - mi)
            lyl = scale * (s_low - mi)
            self.block.append([x, byl, byh, lyl, lyh, status])