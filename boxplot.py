import matplotlib.pyplot as plt

import pandas as pd


uncleaned_raw = pd.read_csv('uncleaned_raw.csv')
#Mengetahui kolom yang memiliki outliers!
uncleaned_raw.boxplot()
plt.show()