import pandas as pd
import numpy as np

df = pd.DataFrame({'column_1': range(7, 10),
                   'column_2': ['X','Y','Z'],
                   'column_3': np.random.rand(3),
                   'column_4': ['A','B','C']})
# df
# column_1 column_2 column_3 column_4
#    7        X     0.763125     A
#    8        Y     0.832541     B
#    9        Z     0.243810     C

# Includes only numeric columns 
df_numeric_columns = df.select_dtypes(include = np.number)
# df_numeric_columns
# column_1  column_3 
#    7      0.763125    
#    8      0.832541     
#    9      0.243810 

# Get list of numeric columns only from DataFrame
numeric_columns = df.select_dtypes(include = np.number).columns.tolist()
#numeric_columns
#['column_1', 'column_3']
