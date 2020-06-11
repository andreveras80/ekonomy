from pandas_datareader import wb
import psycopg2
import os

from sqlalchemy import create_engine
engine = create_engine('postgres://dbvbnsaobxgadt:ecf6895ee7eccdd930382020298a116479bc44eeb8a0090992fa638b3418d6a7@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d35346em5lnoul')

df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'BR'], start=2005, end=2008)
df.columns = ['gdp']

print(df)

#df.to_csv('../gdp_wb.csv', index = True, header=True)
df.to_sql('tb_gdp', engine)
