import xlwt
from datetime import date

class ExcelWriter:
    
    def __init__(self):
        self.wb = xlwt.Workbook()
        self.sheet1 = self.wb.add_sheet('Sheet 1')
        self.row = 0
        self.col = 0
        self.sheet1.write(self.row, self.col, "Student ID")
        self.sheet1.write(self.row, self.col+1, "Time taken")
        self.row = self.row + 1
        
    def __writeSheet__(self, studentid, time):
        self.sheet1.write(self.row, self.col, studentid)
        self.sheet1.write(self.row, self.col+1, time)
        self.row = self.row + 1
        self.wb.save(date.today().strftime('%m%d%Y')+'.xls')
        