from xlrd import open_workbook


# def read_locator(sheetname):
#     book = open_workbook(r"C:\Users\Sakshee\Desktop\hms_locators.xls")
#
#     sheet = book.sheet_by_name(sheetname)
#
#     used_row = sheet.nrows
#
#     data = {}
#     for i in range(1,used_row):
#         row = sheet.row_values(i)
#         data[row[0]] = (row[1],row[2])
#
#     return data

def attach_locator(sheetname):
    def _attach_locator(cls):
        book = open_workbook(r"C:\Users\Sakshee\PycharmProjects\hospital_managment_framework\hms_locators.xls")
        sheet = book.sheet_by_name(sheetname)
        used_rows = sheet.nrows
        data = {}
        for i in range(1, used_rows):
            row = sheet.row_values(i)
            setattr(cls, row[0], (row[1], row[2]))
        return cls

    return _attach_locator


def read_headers(sheetname, test_case_name):
    book = open_workbook(r"C:\Users\Sakshee\PycharmProjects\hospital_managment_framework\test_data.xls")
    sheet = book.sheet_by_name(sheetname)
    used_rows = sheet.nrows
    for i in range(0, used_rows):
        row = sheet.row_values(i)
        if row[0] == test_case_name:
            headers = sheet.row_values(i - 1)
            valid_headers = [header.strip() for header in headers if header.strip()]
            return ",".join(valid_headers[2:])


def read_data(sheetname, test_case_name):
    book = open_workbook(r"C:\Users\Sakshee\PycharmProjects\hospital_managment_framework\test_data.xls")
    sheet = book.sheet_by_name(sheetname)
    used_rows = sheet.nrows
    final_data = []
    for i in range(0, used_rows):
        row = sheet.row_values(i)
        if row[0] == test_case_name:
            temp_record = [item.strip() for item in row if item.strip()]
            if temp_record[1].upper() == "YES":
                final_data.append(tuple(temp_record[2:]))
    return final_data
