import pandas as pd
df=pd.read_csv('data.csv')
print('Average:',df['Marks'].mean())
print('Topper:',df.loc[df['Marks'].idxmax(),'Name'])
