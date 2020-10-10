#先引入后面可能用到的包（package）  
import pandas as pd    
from datetime import datetime  
import backtrader as bt  
import matplotlib.pyplot as plt  
%matplotlib inline 

class my_strategy1(bt.Strategy):  
    #全局设定交易策略的参数  
    params=(  
        ('maperiod',20),  
           )  
  
    def __init__(self):  
        #指定价格序列  
        self.dataclose=self.datas[0].close  
        # 初始化交易指令、买卖价格和手续费  
        self.order = None  
        self.buyprice = None  
        self.buycomm = None  
  
        #添加移动均线指标，内置了talib模块  
        self.sma = bt.indicators.SimpleMovingAverage(  
                      self.datas[0], period=self.params.maperiod)  
    def next(self):  
        if self.order: # 检查是否有指令等待执行,   
            return  
        # 检查是否持仓     
        if not self.position: # 没有持仓  
            #执行买入条件判断：收盘价格上涨突破20日均线  
            if self.dataclose[0] > self.sma[0]:  
                #执行买入  
                self.order = self.buy(size=500)           
        else:  
            #执行卖出条件判断：收盘价格跌破20日均线  
            if self.dataclose[0] < self.sma[0]:  
                #执行卖出  
                self.order = self.sell(size=500)

  
#正常显示画图时出现的中文和负号 
from pylab import mpl
mpl.rcParams['axes.unicode_minus']=False
mpl.rcParams['font.sans-serif']=['SimHei']

#使用tushare旧版接口获取数据
#pip install tushare
import tushare as ts  
def get_data(code,start='2010-01-01',end='2020-03-31'):  
    df=ts.get_k_data(code,autype='qfq',start=start,end=end)  
    df.index=pd.to_datetime(df.date)  
    df['openinterest']=0  
    df=df[['open','high','low','close','volume','openinterest']]  
    return df


dataframe=get_data("600000")