

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

print("Dataset Preview:\n")
print(data.head())

column_name = 'values'   # Change if needed
values = data[column_name]

