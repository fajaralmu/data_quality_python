import pandas as pd
import mysql.connector as sql

# File CSV
print("######## CSV ##########")
df_csv = pd.read_csv("sample_csv.csv")
print(df_csv.head(3)) # Menampilkan 3 data teratas
# File TSV
print("######## TSV ##########")
df_tsv = pd.read_csv("sample_tsv.tsv", sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas
print("########### EXCEL ##########")
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("sample_excel.xlsx", sheet_name='test')
print(df_excel.head(4)) # Menampilkan 4 data teratas
print("############ JSON ############")
url = "covid2019.json"
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas

try:
    print("############ MYSQL ############")

    db_connection = sql.connect(host='localhost', database='dormitory', user='root', password='')
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT id, name, email FROM users limit 10')

    table_rows = db_cursor.fetchall()

    df = pd.DataFrame(table_rows)
    print(" ========== 3 data teratas")
    print(df.head(3))
    print(" ========== 3 data terbawah")
    print(df.tail(3))
except:
    print("An exception occurred when getting data from MYSQL") 