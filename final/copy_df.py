import pandas as pd
#df_participant[___] = pd.___(df_participant[___], unit='___')
df = pd.read_csv('dqthon-participants.csv')
df['register_time'] = df['register_time'].astype(str)
print(';'.join(list(df.columns.values)))
for index, row in df.iterrows():
	val = list()
	for key in list(df.columns.values):
		val.append(row[key])
	print(";".join(val))