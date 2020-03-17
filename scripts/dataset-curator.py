import csv
import xlrd
import urllib.request
from datetime import datetime

url = "http://www.econ.yale.edu/~shiller/data/Fig2-1.xls"
urllib.request.urlretrieve(url, "../archive/source.xls")

workbook = xlrd.open_workbook("../archive/source.xls")
data_sheet = workbook.sheet_by_name("Data")


def check_value(value):
    if value == '':
        return 0
    else:
        return value


data = []
for i in range(7, data_sheet.nrows):
    row_dict = {}
    row = data_sheet.row_values(i)
    month = ''
    date = str(row[0]).split('.')
    if len(date) > 1:
        if date[-1] != '0':
            month = date[-1]
            month = float(month) / 125
            month = "%02d" % month
            row_dict['Date'] = str(date[0]) + '-' + month
        else:
            row_dict['Date'] = str(date[0]) + month
    row_dict['Real Home Price Index'] = round(check_value(row[1]), 2)
    row_dict['Real Building Cost Index'] = round(check_value(row[3]), 2)
    row_dict['U.S. Population Millions'] = row[4]
    row_dict['Long Rate'] = round(check_value(row[5]), 2)
    row_dict['Long Rate Source'] = row[6]
    row_dict['Nominal Home Price Index From_fig2.1Revised2011.xls'] = round(check_value(row[8]), 2)
    row_dict['HPI Source'] = row[9]
    row_dict['Nominal Building Cost Index'] = row[11]
    row_dict['Build Cost Source'] = row[12]
    row_dict['Consumer Price Index'] = round(check_value(row[14]), 2)
    row_dict['CPI Annual & Quarterly'] = row[15]
    row_dict['CPI Annual'] = round(check_value(row[18]), 2)

    data.append(row_dict)

keys = data[0].keys()
with open('../data/united_states_historical_house_prices.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
