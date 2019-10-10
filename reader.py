import pandas as pd

data = pd.read_csv('https://github.com/nickeubank/MIDS_Data/raw/master/World_Development_Indicators/raw_WDI_Data_csv.zip')

data2016 = data.loc[:,['Country Name' ,'Country Code', 'Indicator Name','2016']]

print(data2016.head())
data2016_reshape  = data2016.pivot_table(index='Country Name', columns='Indicator Name', values = '2016')
