import pandas as pd

print("############ SLICING PART 1")

# Baca file sample_csv.csv
df = pd.read_csv("sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["order_date"] == "2019-01-01") &
		          (df["product_id"].isin(["P2154","P2556"]))
				 ]
print("Slice langsung berdasarkan kolom:\n", df_slice)

print("############ SLICING PART 2")
df = pd.read_csv("sample_csv.csv")
# Set index dari df sesuai instruksi
df = df.set_index(["order_date","order_id","product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01",1612339,["P2154","P2159"]),:]
print("Slice df:\n", df_slice)

# /////////////// quiz
print("###### QUIZ ####")
sample_csv = pd.read_csv('sample_csv.csv')
sample_csv = sample_csv.set_index(['province','product_id'])
idx = pd.IndexSlice
sample_csv.sort_index().loc[idx['Sulawesi Selatan', 'P3082':'P3357'], :]
print(sample_csv)