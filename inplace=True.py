from pandas import DataFrame
import numpy as np
df = DataFrame(np.random.randn(5,3) ,index=list('abcde'), columns=['one', 'two', 'three'])
df.ix[1,:-1] = np.nan
df.ix[1:-1,2] = np.nan
df.fillna('missing')#, inplace=True)
print df
