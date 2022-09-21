import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

plt.style.use('bmh')
data1=pd.read_csv("dataset_sim_agent.csv")
data2=pd.read_csv("dataset_sim_agent_rdm.csv")

#df = DataFrame(data)
#df.plot(x=1,y=0)
size1=data1['Size']
perf1=data1['Performance']
dirt1=data1['Dirt Ratio']

size2=data2['Size']
perf2=data2['Performance']
dirt2=data2['Dirt Ratio']
figure, (ax1,ax2)=plt.subplots(1,2)

ax1.scatter(size2,perf2)
ax1.set_title("Performance by size")

ax2.scatter(dirt2,perf2)
ax2.set_title("Performance by dirt ratio")
ax1.set(xlabel='Size',ylabel='Performance')
ax2.set(xlabel='Dirt Ratio',ylabel='Performance')
plt.show()
