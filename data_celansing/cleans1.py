import pandas as pd 
pd.options.display.max_columns = 50

#import dataset
df_load = df_load = pd.read_csv('dqlab_telco.csv')

#Tampilkan jumlah baris dan kolom
print(df_load.shape)

#Tampilkan 5 data teratas
print(df_load.head())

#Jumlah ID yang unik
print(df_load['customerID'].unique())

#FILTER CustomerID

df_load['valid_id'] = df_load['customerID'].astype(str).str.match(r'(45\d{9,10})')
df_load = (df_load[df_load['valid_id'] == True]).drop('valid_id', axis = 1)
print('Hasil jumlah ID Customer yang terfilter adalah',df_load['customerID'].count())

#Drop Duplicate Rows
df_load.drop_duplicates()
#Drop duplicate ID sorted by Periode
df_load = df_load.sort_values('UpdatedAt',ascending=False).drop_duplicates(['customerID'])
print('Hasil jumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah',df_load['customerID'].count())

#Mengatasi Missing Values dengan Penghapusan Rows
print('Total missing values data dari kolom Churn',df_load['Churn'].isnull().sum())
print('Total Rows dan kolom Data setelah dihapus data Missing Values adalah',df_load.shape)

#handling missing values Tenure fill with 11
print('Status Missing Values :',df_load.isnull().values.any())
print('\nJumlah Missing Values masing-masing kolom, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

# handling missing values Tenure fill with 11
df_load['tenure'].fillna(11, inplace=True)

# Handling missing values num vars (except Tenure)
for col_name in list(['MonthlyCharges','TotalCharges']):
    median = df_load[col_name].median()
    df_load[col_name].fillna(median, inplace=True)

print('\nJumlah Missing Values setelah di imputer datanya, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

print('\nPersebaran data sebelum ditangani Outlier: ')
print(df_load[['tenure','MonthlyCharges','TotalCharges']].describe())

# Creating Box Plot
import matplotlib.pyplot as plt
import seaborn as sns

# Masukkan variable
# plt.figure() # untuk membuat figure baru
# sns.boxplot(x=df_load['tenure'])
# plt.show()
# plt.figure() # untuk membuat figure baru
# sns.boxplot(x=df_load['MonthlyCharges'])
# plt.show()
# plt.figure() # untuk membuat figure baru
# sns.boxplot(x=df_load['TotalCharges'])
# plt.show()

#--------------- MENGATASI OUTLIER ------------------
Q1 = (df_load[['tenure','MonthlyCharges','TotalCharges']]).quantile(0.25)
Q3 = (df_load[['tenure','MonthlyCharges','TotalCharges']]).quantile(0.75)
IQR = Q3 - Q1
maximum = Q3 + (1.5*IQR)
print('Nilai Maximum dari masing-masing Variable adalah: ')
print(maximum)
minimum = Q1 - (1.5*IQR)
print('\nNilai Minimum dari masing-masing Variable adalah: ')
print(minimum)
more_than = (df_load > maximum)
lower_than = (df_load < minimum)
df_load = df_load.mask(more_than, maximum, axis=1)
df_load = df_load.mask(lower_than, minimum, axis=1)
print('\nPersebaran data setelah ditangani Outlier: ')
print(df_load[['tenure','MonthlyCharges','TotalCharges']].describe())