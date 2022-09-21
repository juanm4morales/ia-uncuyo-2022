import matplotlib.pyplot as plt
import pandas as pd
import os
#plt.style.use('fivethirtyeight')


fileName = 'results.csv'
currentPath = os.path.dirname(__file__)
parentPath = os.path.dirname(currentPath)
path=os.path.join(parentPath,fileName)
results=pd.read_csv(path)


results.boxplot(by='Search_Strategy',grid=True,column=['Explored_Nodes'])
plt.title('')
plt.suptitle('')
plt.ylabel('Explored Nodes')
plt.show()


