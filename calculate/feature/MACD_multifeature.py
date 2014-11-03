__author__ = 'cyh'

import calculate.feature.MACD

MF_strong_pull = 1
MF_1_pull = 2
MF_2_pull = 3
MF_weak_pull = 4
MF_strong_push = 5
MF_1_push = 6
MF_2_push = 7
MF_weak_push = 8
MF_micro_push = 9
MF_1_balance = 10
MF_2_balance = 11
MF_micro_pull = 12
MF_default = 0


def compute(data_list, long=26, short=12, m=9, section=5):
    sec = section
    diff_dea_cross = []
    macd_ps_ng = []
    diff_dea_ps_ng = []
    rst = []
    macdlist = calculate.feature.MACD.compute(data_list, long, short, m)
    diff = [item[0] for item in macdlist]
    dea = [item[1] for item in macdlist]
    macd = [item[2] for item in macdlist]
    if len(macd) < 3:
        for i in range(len(macd)):
            diff_dea_cross.append(0)
            macd_ps_ng.append(0)
    else:
        diff_dea_cross.append(0)
        macd_ps_ng.append(0)
        for i in range(1, len(macd) - 1):
            if diff[i - 1] < dea[i - 1] and diff[i + 1] > dea[i + 1]:
                diff_dea_cross.append(1)
            elif diff[i - 1] > dea[i - 1] and diff[i + 1] < dea[i + 1]:
                diff_dea_cross.append(-1)
            else:
                diff_dea_cross.append(0)
            if macd[i - 1] < 0 < macd[i + 1]:
                macd_ps_ng.append(1)
            elif macd[i - 1] > 0 > macd[i + 1]:
                macd_ps_ng.append(-1)
            else:
                macd_ps_ng.append(0)
        diff_dea_cross.append(0)
        macd_ps_ng.append(0)
    for i in range(len(diff)):
        if diff[i] > 0 and dea[i] > 0:
            diff_dea_ps_ng.append(1)
        elif diff[i] < 0 and dea[i] < 0:
            diff_dea_ps_ng.append(-1)
        else:
            diff_dea_ps_ng.append(0)
    for i in range(sec):
        rst.append(MF_default)
    for i in range(sec, len(diff)):
        if diff_dea_cross[i] == 1:
            if 1 in macd_ps_ng[i - sec: i]:
                if 1 in diff_dea_ps_ng[i - sec: i]:
                    rst.append(MF_strong_pull)
                else:
                    rst.append(MF_1_pull)
            elif 1 in diff_dea_ps_ng[i - sec: i]:
                rst.append(MF_2_pull)
            else:
                rst.append(MF_weak_pull)
        elif diff_dea_cross[i] == -1:
            if -1 in macd_ps_ng[i - sec: i]:
                if -1 in diff_dea_ps_ng[i - sec: i]:
                    rst.append(MF_strong_push)
                else:
                    rst.append(MF_1_push)
            elif -1 in diff_dea_ps_ng[i - sec: i]:
                rst.append(MF_2_push)
            else:
                rst.append(MF_weak_push)
        else:
            if -1 in macd_ps_ng[i - sec: i]:
                if -1 in diff_dea_ps_ng[i - sec: i]:
                    rst.append(MF_micro_push)
                else:
                    rst.append(MF_1_balance)
            elif -1 in diff_dea_ps_ng[i - sec: i]:
                rst.append(MF_2_balance)
            else:
                rst.append(MF_micro_pull)
    return rst