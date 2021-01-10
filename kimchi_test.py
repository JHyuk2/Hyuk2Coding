import pandas as pd
import numpy as np

raw_data = pd.read_csv('response_sheet.csv', encoding='utf-8', names=[i for i in range(1, 41)], header=0)
# print(type(raw_data))
# print(raw_data.shape)
# print(raw_data.head())

users = ['clerk', 'admin1', 'admin2', 'admin3']
dates = raw_data[1].apply(lambda x:x[:11])
print(dates.unique())

# records = dict()

# for tmp_data in raw_data:
#     if tmp_data[[3]] == '절임공정 이후' or tmp_data[[3]] == '세척공정 이후':
        