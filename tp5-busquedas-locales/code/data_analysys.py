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


fig, axs = plt.subplots(1,3)

sns.boxplot(data=s4, x='Algorithm', y='Time')

plt.yscale("log")

plt.show()
