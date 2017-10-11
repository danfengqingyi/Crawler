# -*-coding:utf-8-*-
from xlutils.copy import copy;

import xlrd
import xlwt


class Outputer(object):
    def __init__(self):
        self.i = 0
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('A Test Sheet')
        self.newwb = None

    def outputerexcel(self,var):
        # style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
        # style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
        # if u"卡" not in var[0] and u"顿" not in var[0] and u"慢" not in var[0]:
        #     return

        if self.i !=0:
            self.wb = xlrd.open_workbook("example.xls")
            self.newwb = copy(self.wb)
            self.ws = self.newwb.get_sheet(0)

        self.ws.write(self.i, 0, var[0])
        self.ws.write(self.i, 1, var[1])
        self.ws.write(self.i, 2, var[2])
        if self.i == 0:
            self.wb.save('example.xls')
        else:
            self.newwb.save('example.xls')
        self.i = self.i + 1


