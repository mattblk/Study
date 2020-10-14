from pandas import Series, DataFrame

print(Series)

kakao = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])

print(kakao)

print(kakao[1])
print(kakao['2016-02-15'])

for date in kakao.index :
    print(date)
for ending_price in kakao.values :
    print(ending_price)
