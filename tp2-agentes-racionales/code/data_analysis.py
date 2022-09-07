import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

plt.style.use('bmh')
data=pd.read_csv("dataset_sim_agent.csv")

#df = DataFrame(data)
#df.plot(x=1,y=0)
size=data['Size']
perf=data['Performance']
dirt=data['Dirt Ratio']

figure, (ax1,ax2)=plt.subplots(1,2)

ax1.scatter(size,perf)
ax1.set_title("Performance by Size")


ax2.scatter(dirt,perf)
ax2.set_title("Performance by Dirt Ratio")
ax1.set(xlabel='Size',ylabel='Performance')
ax2.set(xlabel='Dirt Ratio')
plt.show()
