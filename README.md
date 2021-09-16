# python_excel_app

# dynamic add columns from csv to database [pandas]


```python
import pandas as pd

df = pd.read_csv('data.csv')

#print(df['Duration'])

db = []
#dynamic function not depend on static csv names
for i in range(df.shape[0]):
    obj = {'duration': '', 'pulse': '', 'maxpulse': '', 'calories': ''}
    for x in df.columns:    
        if x == "Duration":
            obj['duration'] = df[x].loc[i]
        if x == "Pulse":
            obj['pulse'] = df[x].loc[i]
        if x == "Maxpulse":
            obj['maxpulse'] = df[x].loc[i]
        if x == "Calories":
            obj['calories'] = df[x].loc[i]
    db.append(obj)
           
     
print(db)
print(df.loc[[0,1]])


```
