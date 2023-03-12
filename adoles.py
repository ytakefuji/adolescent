import pandas as pd
import matplotlib.pyplot as plt
import subprocess as sp
sp.call('wget -nc https://data.cdc.gov/api/views/chcz-j2du/rows.csv', shell=True)
d=pd.read_csv('rows.csv')
years=d.Year.unique()
a1=[]
a2=[]
a3=[]
for i in years:
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='10-14 years'),'Total Deaths']
 a1.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='15-19 years'),'Total Deaths']
 a2.append(a)
 a=d.loc[(d.Year==i) &
  (d['Sex']=='All Sexes') & (d['Age Group']=='20-24 years'),'Total Deaths']
 a3.append(a)
plt.ylim([0,30000])
plt.plot(years,a1,':k')
plt.plot(years,a2,'-k')
plt.plot(years,a3,'--k')
plt.legend(('10-14 years','15-19 years','20-24 years'))
plt.title('Impact of COVID-19 on montality of adolescent')
plt.savefig('adolescent.png')
plt.show()
