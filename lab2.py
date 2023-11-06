import sklearn.datasets as data
import pandas as pd
import numpy as np
ds = pd.Series([10, 20, 30])

ds = pd.Series([10, 20, 30], index=['A', 'B', 'C'])  # custom index
ds.keys()  # gives you index
print(ds)
ds.items()  # gives key- value pair as a tuple
ds[0]  # or ds['A'] return first element
ds[0:2]  # get element staring from 0 but not including 2
ds[ds > 10]  # returns all element >10


df = data.load_iris()

np.sum(ds)  # sum all elements of DataSeries
np.mean(df)  # perform column wise mean
np.sin(df)  # find sin of each element
ds = ds1+ds2  # element wise operation
