import pandas as pd

data = pd.read_excel('test2.xlsx', index_col=0,
            dtype={'Time': str, 'Name':str, 'Wake_up': str, 'Satisfaction':str})

print(data)
