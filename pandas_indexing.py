import pandas as pd
print("######## SINGLE INDEX ##########")
df = pd.read_csv("sample_tsv.tsv", sep='\t')
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns)

print("########### MULTI INDEX #################")
df = pd.read_csv("sample_tsv.tsv", sep="\t")
# Set multi index df
df_x = df.set_index(['order_date', 'city', 'customer_id'])
print(df_x.index)
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level)

print("############### UPDATE INDEX #################")
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv("sample_tsv.tsv", sep="\t", nrows=10)
# Cetak data frame awal
print("Dataframe awal:\n", df)
# Set index baru
df.index = ["Pesanan ke-" + str(i+1) for i in range(0, 10)]
# Cetak data frame dengan index baru
print("Dataframe index baru:\n", df.index)
print("Dataframe dengan index baru:\n", df)

print("#################### INDEXING #####################")
# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("sample_tsv.tsv", sep="\t", index_col=["order_date", "order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))

