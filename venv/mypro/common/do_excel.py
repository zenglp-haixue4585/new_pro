import openpyxl


class Cases:

    def __init__(self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.case_method = None
        self.expected = None
        self.actual = None
        self.result = None


class DoExcel:

    def __init__(self, file_name, sheet_name="sheet1"):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.workbook = openpyxl.load_workbook(self.file_name)

        self.sheet = self.workbook[sheet_name]

    def read_file(self):
        max_row = self.sheet.max_row

        cases = []

        for i in range(2, max_row + 1):
            print(self.sheet.cell(row=3, column=1).value)
            # case = Cases()
            # case.case_id = self.sheet.cell(row=i, column=1).value
            # case.url = self.sheet.cell(row=i, column=2).value
            # case.method = self.sheet.cell(row=i, column=3).value
            # case.data = self.sheet.cell(row=i, column=4).value
            # case.expected = self.sheet.cell(row=i, column=5).value
            # cases.append(case)
        self.workbook.close()
        return cases

    def write_file(self, row, actual, result):
        sheet = self.workbook[self.sheet]
        sheet.cell(row, 7).value = actual
        sheet.cell(row, 8).value = result
        self.workbook.save(filename=self.file_name)
        self.workbook.close()


if __name__ == '__main__':
    # my_excel = DoExcel(r"/Users/apple/Desktop/公众号引流页_基础用例_导入模板.xlsx", r"基础用例导入")
    # my_excel.read_file()
    import time
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(now_time)
