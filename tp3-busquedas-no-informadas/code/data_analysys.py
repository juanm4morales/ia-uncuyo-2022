import matplotlib.pyplot as plt
import pandas as pd


#plt.style.use('fivethirtyeight')

results=pd.read_csv("results.csv")
results.boxplot(by='Search_Strategy',grid=True,column=['Explored_Nodes'])
plt.title('')
plt.suptitle('')
plt.ylabel('Explored Nodes')
plt.show()


