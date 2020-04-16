import pytrends
from pytrends.request import TrendReq
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

pytrends = TrendReq()
kw_list=['Corona Virus Symptoms']
#pytrends = TrendReq(hl='en-US', tz=360, timeout=(400,2500), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1)
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')
dataframe=pytrends.interest_over_time()
dataframe.to_csv('file_name.csv')
dates,interest= np.loadtxt('file_name.csv',dtype='str',delimiter=',',skiprows=1,usecols=(0,1),unpack=True)
date_objects = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
interest = [int(i) for i in interest] 
plt.plot(date_objects,interest)
plt.show()
