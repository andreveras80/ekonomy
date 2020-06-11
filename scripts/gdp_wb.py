from pandas_datareader import wb
import psycopg2
import os

from sqlalchemy import create_engine
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'BR'], start=2005, end=2008)
df.columns = ['gdp']

print(df)

#df.to_csv('../gdp_wb.csv', index = True, header=True)
df.to_sql('tb_gdp', engine)
