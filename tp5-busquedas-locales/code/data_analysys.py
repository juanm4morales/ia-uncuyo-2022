import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
#plt.style.use('fivethirtyeight')

fileName = 'results.csv'
currentPath = os.path.dirname(__file__)
parentPath = os.path.dirname(currentPath)
path=os.path.join(parentPath,fileName)
results=pd.read_csv(path)


s4 = results[results['Queens_Size']==4]
s8 = results[results['Queens_Size']==8]
s10 = results[results['Queens_Size']==10]
s12 = results[results['Queens_Size']==12]
s15 = results[results['Queens_Size']==15]


fig, axs = plt.subplots(1,2,figsize=(12,8))

#sns.boxplot(data=s4,x='Algorithm',y='Time',ax=axs[0])
#sns.boxplot(data=s8,x='Algorithm',y='Time',ax=axs[1])
#sns.boxplot(data=s10,x='Algorithm',y='Time',ax=axs[2])

sns.boxplot(data=s12,x='Algorithm',y='Time',ax=axs[0])
sns.boxplot(data=s15,x='Algorithm',y='Time',ax=axs[1])

axs[0].set(yscale='log')
axs[0].set_xlabel("")
axs[0].set_title("12 queens")
axs[1].set(yscale='log')
axs[1].set_xlabel("")
axs[1].set_ylabel("")
axs[1].set_title("15 queens")
#axs[2].set(yscale='log')
#axs[2].set_xlabel("")
#axs[2].set_ylabel("")
#axs[2].set_title("10 queens")

plt.show()
