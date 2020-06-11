

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()
sql = "create table tb_gdp (country varchar(128), year integer, gdp real);"
cursor.execute(sql)
conn.commit()
