from pandas_datareader import wb
import pandas_datareader.data as web
import datetime

from sqlalchemy import create_engine
engine = create_engine('postgres://dbvbnsaobxgadt:ecf6895ee7eccdd930382020298a116479bc44eeb8a0090992fa638b3418d6a7@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d35346em5lnoul')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)

df = web.DataReader(['CPILFESL'], 'fred', start, end)

print(df)

#df.to_csv('../gdp_wb.csv', index = True, header=True)
df.to_sql('tb_gdp1', engine)
