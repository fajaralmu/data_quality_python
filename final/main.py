import pandas as pd
df_participant = pd.read_csv('dqthon-participants.csv', sep=';')
# print(df_participant.keys())
df_participant['city'] = df_participant['address'].str.extract(r'((?<=\\n).\w+)') #Masukkan regex Anda didalam fungsi extract
##r'(?:\d+)\n+(\w+)' 
print(df_participant['address'].head())
print(df_participant['city'].head())
df_participant['github_profile'] = 'https://github.com/' + df_participant['first_name'].str.lower() + df_participant['last_name'].str.lower()
print(df_participant['github_profile'].head())

print("--------------RAW PHONE NUMBER--------------")
print(df_participant['phone_number'].head())
print(" replace step 1 ")
df_participant['phone_number'] = df_participant['phone_number'].str.replace(r'[+]?62', '0')
print(df_participant['phone_number'].head())
df_participant['cleaned_phone_number'] = df_participant['phone_number'].str.replace(r'[(]|[)]|[-]', '')
print(df_participant['cleaned_phone_number'].head())
df_participant['cleaned_phone_number'] = df_participant['cleaned_phone_number'].str.replace(r'\s', '')
print(df_participant['cleaned_phone_number'].head())

#========== team name 
print("======== TEAM NAME ==========")
def func(col):
	abbrev_name = "%s%s"%(col['first_name'][0],col['last_name'][0]) #Singkatan dari Nama Depan dan Nama Belakang dengan mengambil huruf pertama
	country = col['country']
	abbrev_institute = '%s'%(''.join(list(map(lambda word: word[0], col['institute'].split())))) #Singkatan dari value di kolom institute
	return "%s-%s-%s"%(abbrev_name,country,abbrev_institute)

df_participant['team_name'] = df_participant.apply(func, axis=1)
print(df_participant['team_name'].head())

# =============== email
print("=========== EMAIL ADDRESS ===========")
def func2(col):
	first_name_lower = col['first_name'].lower()
	last_name_lower = col['last_name'].lower()
	institute = ''.join(list(map(lambda word: word[0], col['institute'].lower().split()))) #Singkatan dari nama perusahaan dalam lowercase

	if 'Universitas' in col['institute']:
		if len(col['country'].split()) > 1:
			country = ''.join(list(map(lambda word: word[0], col['country'].lower().split())))
		else:
			country = col['country'][:3].lower()
		return "%s%s@%s.ac.%s"%(first_name_lower,last_name_lower,institute,country)

	return "%s%s@%s.com"%(first_name_lower,last_name_lower,institute)

df_participant['email'] = df_participant.apply(func2, axis=1)
print(df_participant['email'].head())

#================== birth date
print(df_participant.dtypes)
df_participant['birth_date'] = pd.to_datetime(df_participant['birth_date'], format='%d %b %Y')
print(df_participant['birth_date'].head())

#============== register time
df_participant['register_at'] = pd.to_datetime(df_participant['register_time'], unit='s')
print(df_participant['register_at'].head())

ops1 = df_participant['participant_id'].str.replace(r'[a-zA-Z-]', '')
# ops2 = df_participant['participant_number'].str.replace(r'[a-zA-Z-]', '')
ops3 = df_participant['participant_id'].str.replace(r'[\w+-]', '')
ops4 = df_participant['participant_id'].str.replace(r'\d+', '')
ops5 = df_participant['participant_id'].str.replace(r'[\d+-]', '')
print(ops1)



