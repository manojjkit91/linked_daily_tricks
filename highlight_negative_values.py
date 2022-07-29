# Highlight all negative values in a dataframe

import pandas as pd

def highlight_all_negative ( val ):
    clr = 'red' if val < 0 else 'black'
    return 'color: %s' % clr

df = pd.DataFrame({'col_1':[1.15,-5.5,3.46], 
                   'col_2':[-41.5,10.6,0],
                   'col_3':[14.5,0.4,10]})
df.style.applymap(highlight_all_negative)