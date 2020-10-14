from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print("Dictionary : ")
print(raw_data)
print("\n\nDataFrame : ")
print(data)

print(data['col1'])
print(type(data['col1']))


daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
cols =['open', 'high', 'low', 'close']
daeshin_day = DataFrame(daeshin,columns=cols, index = date)
print(daeshin_day)

print(daeshin_day['close'])
print(daeshin_day.loc['16.02.26'])
