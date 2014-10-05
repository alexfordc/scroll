__author__ = 'ict'

from tkinter import Tk
from tkinter import Canvas

open_offset = 0
high_offset = 1
low_offset = 2
close_offset = 3
volume_offset = 4

x_offset = 0
block_y_low = 1
block_y_high = 2
line_y_low = 3
line_y_high = 4
volume_y = 5
status_offset = 6

up = 1
down = -1


class Kline:
    def __init__(self, width=1280, height=800, title="K line"):
        self.data = []
        self.have_volume = False
        self.height = height
        self.width = width
        self.top_offset = 10
        self.buttom_offset = 30
        self.graph_buttom_offset = self.buttom_offset
        self.vgraph_height = 150
        self.side_offset = 50
        self.graph_height = height - self.top_offset - self.buttom_offset
        self.graph_width = width - self.side_offset
        self.title = title
        self.block = []
        self.block_width = 0
        self.curve = []
        self.ma = 0
        self.mi = 0
        self.vma = 0
        self.vmi = 0
        self.price = []
        self.step = 0

    def stock_data(self, data_list):
        self.data = list(data_list)

    def draw(self):
        main = Tk()
        main.title(self.title)
        can = Canvas(main, bg="black", height=self.height, width=self.width)
        side_x1 = self.side_offset
        side_y1 = 0
        side_x2 = self.width
        side_y2 = self.height - self.buttom_offset
        step_y = self.graph_height / (self.step - 1)
        can.create_line([side_x1, side_y1, side_x1, side_y2], fill="red")
        can.create_line([side_x1, side_y2, side_x2, side_y2], fill="red")
        text_y = self.top_offset
        self.price.sort(reverse=True)
        for i in range(len(self.price)):
            can.create_text([self.side_offset / 2, text_y], text=str(self.price[i])[:7], fill="red")
            if i < len(self.price) - 1:
                can.create_line([side_x1, text_y, side_x2, text_y], fill="red", dash=1)
            else:
                can.create_line([side_x1, text_y, side_x2, text_y], fill="red")
            text_y += step_y
        text_y -= step_y - self.buttom_offset
        can.create_line([side_x1, text_y, side_x2, text_y], fill="red", dash=1)
        text_y += self.vgraph_height / 2
        can.create_line([side_x1, text_y, side_x2, text_y], fill="red", dash=1)
        for b in self.block:
            bx1 = b[x_offset]
            bx2 = bx1 + self.block_width - 1
            by1 = b[block_y_low]
            by2 = b[block_y_high]
            lx = (bx1 + bx2) / 2
            ly1 = b[line_y_low]
            ly2 = b[line_y_high]
            if b[status_offset] == up:
                color = "red"
            else:
                color = "cyan"
            if abs(by1 - by2) < 2:
                by2 = by1 + 2
                if ly1 == ly2:
                    color = "yellow"
            can.create_line([lx, ly1, lx, ly2], fill=color)
            if color == "red":
                can.create_rectangle([bx1, by1, bx2, by2], outline=color, fill="black")
                if self.have_volume:
                    vy = b[volume_y]
                    can.create_rectangle([bx1, vy, bx2, self.height - self.buttom_offset - 1], outline=color, fill="black")
            else:
                can.create_rectangle([bx1, by1, bx2, by2], fill=color)
                if self.have_volume:
                    vy = b[volume_y]
                    if color != "yellow":
                        can.create_rectangle([bx1, vy, bx2, self.height - self.buttom_offset - 1], fill=color)
        for curve_class in self.curve:
            cx = self.side_offset + 1 + self.block_width * curve_class[2] + self.block_width / 2
            color = curve_class[1]
            data_list = curve_class[0]
            for i in range(1, len(data_list)):
                can.create_line([cx, data_list[i - 1], cx + self.block_width, data_list[i]], fill=color)
                cx += self.block_width
        can.pack()
        main.mainloop()

    def create_basic(self, data_list=None, step=5):
        if data_list is not None:
            self.data = data_list
        block_width = self.graph_width / len(self.data)
        if block_width == 0:
            raise Exception("GUI is too small")
        self.block_width = block_width
        mi_list = []
        ma_list = []
        for n_list in self.data:
            mi_list.append(min(n_list[: 4]))
            ma_list.append(max(n_list[: 4]))
        self.mi = min(mi_list)
        self.ma = max(ma_list)
        vlist = [s[volume_offset] for s in self.data]
        self.vmi = min(vlist)
        self.vma = max(vlist)
        vsub = self.vma - self.vmi
        if vsub == 0:
            vsub = 1
        x = self.side_offset + 1
        if len(self.data[0]) > 4:
            self.have_volume = True
            self.graph_height -= self.vgraph_height + self.buttom_offset
            self.graph_buttom_offset += self.vgraph_height + self.buttom_offset
        scale = self.graph_height / (self.ma - self.mi)
        for n_list in self.data:
            s_open = n_list[open_offset]
            s_high = n_list[high_offset]
            s_low = n_list[low_offset]
            s_close = n_list[close_offset]
            vy = -1
            if self.have_volume:
                s_volume = n_list[volume_offset]
                vh = (self.vgraph_height / vsub) * (s_volume - self.vmi)
                vy = self.graph_height + self.buttom_offset + self.top_offset + (self.vgraph_height - vh)
            if s_open <= s_close:
                status = up
                byh = self.height - scale * (s_close - self.mi) - self.graph_buttom_offset - 1
                byl = self.height - scale * (s_open - self.mi) - self.graph_buttom_offset - 1
            else:
                status = down
                byh = self.height - scale * (s_open - self.mi) - self.graph_buttom_offset - 1
                byl = self.height - scale * (s_close - self.mi) - self.graph_buttom_offset - 1
            lyh = self.height - scale * (s_high - self.mi) - self.graph_buttom_offset - 1
            lyl = self.height - scale * (s_low - self.mi) - self.graph_buttom_offset - 1
            self.block.append([x, byl, byh, lyl, lyh, vy, status])
            x += self.block_width
        price_step = (self.ma - self.mi) / step
        for i in range(step):
            self.price.append(self.mi + price_step * i)
        self.step = step

    def create_curve(self, data_list, color, offset=0, price=False):
        if len(self.block) == 0:
            raise Exception("Need invoke create_basic first")
        if price:
            scale = self.graph_height / (self.ma - self.mi)
            tmp_list = []
            for data in data_list:
                tmp_list.append(self.height - scale * (data - self.mi) - self.graph_buttom_offset - 1)
            self.curve.append((tmp_list, color, offset))
        else:
            ma = max(data_list)
            mi = min(data_list)
            if ma == mi:
                return
            tmp_list = []
            for data in data_list:
                tmp_list.append(self.height - (self.graph_height / (ma - mi)) * (data - mi) - self.graph_buttom_offset - 1)
            self.curve.append((tmp_list, color, offset))