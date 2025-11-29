#Task 1: Data Acquisition and Loading
import pandas as pd
df=pd.read_csv('weather_data.csv')
print (df)
print(df.head())
print (df.info())
print (df.describe())
#Task 2: Data Cleaning and Processing
df=df.dropna()
print (df)
