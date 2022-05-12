import pandas as pd
import csv

#데이터 불러오기
df = pd.read_csv('hotnow_test_img.csv', encoding='cp949')


"""
Q1. hotnow 매장이 가장 많은 시간대와 매장명은?
"""
# hotnow가 많이 뜨는 시간대 저장 변수 (결과출력변수)
hotmax_time = []

#time열을 기준으로 count
data = df['time'].value_counts()
#data변수안에 값중 가장 큰 값만 출력
data_max = data.max()

#데이터 필터링 ( Q1. 7시- 24시 중에서 가장 도넛이 많이 나오는 시간은? )
filters = df.groupby('time').filter(lambda x:x['time'].count() == data_max)
filter_data = filters['time'].value_counts()

for idx in range(0,len(filter_data),1):
    #필터링된 결과값에서 인덱스만 추출
    data_idx = filter_data.index[idx]
    
    #결과값출력 변수에 값 저장
    hotmax_time.append(data_idx) 
    
    # time열에서 인덱스와 같은 정보들만 추출
    reslut = df['time'] == data_idx
    
    #결과 출력
    
    print(df.loc[reslut])

print('============================================================')

# hotnow가 많이 뜨는 시간대 매장 갯수와 매장명 저장 변수 (결과출력변수)
hotmax_cnt = df.loc[reslut].loc[:,'store'].count()
hotmax_name = df.loc[reslut].loc[:,'store']  #loc[:,'store'] : store열 만을 대상으로 검색/추출

print('Q1. 7시 - 24시 중에서 가장 도넛이 많이 나오는 시간은? \n → {0}시 입니다. {1}개의 매장에서 도넛이 생산됩니다.'.format(hotmax_time,hotmax_cnt))
print(' → 매장명 : \n{}'.format(hotmax_name))

print('============================================================')

"""
Q2. 7시 - 24시 중에서 hotnow 매장이 없는 시간은?
"""

#카운트
none_cnt = df.query("store == 'NONE'").loc[:,'time'].count()
#시간대
none_time = df.query("store == 'NONE'").loc[:,'time'].values


print('Q2. 7시 - 24시 중에서 hotnow 매장이 없는 시간은? \n → {0}시 입니다.'.format(none_time))

print('============================================================')

"""
Q3. Hotnow 매장은 총 몇개인가?
"""
all_store_tit=[]
#hotnow 전체 매장
all_store = df.query("store != 'NONE'").loc[:,'store'].value_counts()
all_store_tit_index = all_store.index

for idx in range(0,len(all_store_tit_index),1):
    all_store_tit.append(all_store_tit_index[idx])
    
#hotnow 전체 매장 count
all_store_cnt = all_store.count()

print('Q3. Hotnow 매장은 총 몇개인가? \n → {0}개 입니다.'.format(all_store_cnt))
print('-> 매장명 : \n{}'.format(all_store_tit))

print('============================================================')
