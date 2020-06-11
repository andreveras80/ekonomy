from pandas_datareader import wb
import psycopg2
import os

from sqlalchemy import create_engine
engine = create_engine('postgres://nmkeqfzylbgsyx:54bd78f6ee3957e7765b5cd8fcfaf21651f165a7cab99b06fa92754dfdb684ac@ec2-34-202-88-122.compute-1.amazonaws.com:5432/dcnr29vkhe97fv')

df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'BR'], start=2005, end=2008)
df.columns = ['gdp']

print(df)

#df.to_csv('../gdp_wb.csv', index = True, header=True)
df.to_sql('tb_gdp', engine)
