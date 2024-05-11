import pandas as pd
data = pd.read_csv('test.csv',sep=",")

from sklearn.naive_bayes import BernoulliNB
x=data.drop(['年份','次年房价是否大幅上涨'],axis=1)
y=data['次年房价是否大幅上涨']
clf=BernoulliNB()
clf.fit(x,y)
print(clf.score(x,y))

x_2019=[[0,1,0]]
y_2020=clf.predict(x_2019)
print(y_2020)