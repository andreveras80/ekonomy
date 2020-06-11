from pandas_datareader import wb

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'BR'], start=2005, end=2008)

print(df)

#df.to_csv('../gdp_wb.csv', index = True, header=True)
df.to_sql('table_name', conn)
