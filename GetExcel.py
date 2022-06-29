import openpyxl


class GetExcel:
    def __init__(self, file, sheetname):
        self.wb = openpyxl.load_workbook(file)
        self.sh = self.wb[sheetname]

    def read_all_data_line_by_line(self):
        """一行一行的获取数据"""
        row_datas = list(self.sh.rows)  # 按行获取数据转换成列表
        titles = []  # 获取表单的表头信息
        for title in row_datas[0]:  # 获取第一行的数据，row_datas从下标0开始
            titles.append(title.value)
        testdatas = []  # 存储所有行数据
        for case in row_datas[1:]:  # 从第二行开始获取数据，case为元组数据类型
            data = []  # 定义列表临时存储每一行数据
            for cell in case:
                try:
                    data.append(eval(cell.value))
                except:
                    data.append(cell.value)
            case_data = dict(list(zip(titles, data)))  # case_data 为存储一行的数据，存储格式如：{title：cell_value}
            testdatas.append(case_data)
        return testdatas


if __name__ == "__main__":
    filepath = r'C:\pythonwork\data\wzx.xlsx'  # 文件绝对路径
    sheetname = 'Sheet1'  # 表名
    sheetObject = GetExcel(filepath, sheetname)
    testdatas = sheetObject.read_all_data_line_by_line()
    for onetestdata in testdatas:
        print(onetestdata)
