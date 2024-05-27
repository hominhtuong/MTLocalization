import xmltodict
import pandas as pd
import xlsxwriter


directoryParent = "Kotlin/res"
INPUT_FILE_NAME = directoryParent + "/strings.xml"
RESULTS_PATH = directoryParent + "/data.xlsx"


workbook = xlsxwriter.Workbook(RESULTS_PATH)
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "Text Key")
worksheet.write(0, 1, "Base(en)")

with open(INPUT_FILE_NAME) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

    df = pd.json_normalize(data_dict)
    values = df.values[0][0]
    for index, value in enumerate(values):
        for i, item in enumerate(value):
            worksheet.write(index + 1, i, value[item])

    workbook.close()
