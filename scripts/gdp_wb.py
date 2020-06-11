from pandas_datareader import wb

df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2005, end=2008)

#print(df)

df.to_csv('../gdp_wb.csv', index = True, header=True)
