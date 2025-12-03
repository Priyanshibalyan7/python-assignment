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
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Temperature', 'Rainfall', 'Humidity']]  


#Task 3: Statistical Analysis with NumPy
import numpy as np

# Daily stats
daily_stats = df.describe()

# Monthly stats
df['Month'] = df['Date'].dt.to_period('M')
monthly_stats = df.groupby('Month').agg({
    'Temperature': [np.mean, np.min, np.max, np.std],
    'Rainfall': [np.mean, np.min, np.max, np.std],
    'Humidity': [np.mean, np.min, np.max, np.std]
})

# Yearly stats
df['Year'] = df['Date'].dt.year
yearly_stats = df.groupby('Year').agg({
    'Temperature': [np.mean, np.min, np.max, np.std],
    'Rainfall': [np.mean, np.min, np.max, np.std],
    'Humidity': [np.mean, np.min, np.max, np.std]
})

#Task 4: Visualization with Matplotlib
import matplotlib.pyplot as plt

# Line chart: Daily temperature
plt.figure(figsize=(10, 4))
plt.plot(df['Date'], df['Temperature'], label='Daily Temp')
plt.title('Daily Temperature Trends')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.savefig('daily_temperature.png')
plt.show()

# Bar chart: Monthly rainfall
monthly_rainfall = df.groupby('Month')['Rainfall'].sum()
monthly_rainfall.plot(kind='bar', figsize=(10, 4), color='skyblue')
plt.title('Monthly Rainfall Totals')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_rainfall.png')
plt.show()

# Scatter plot: Humidity vs Temperature
plt.figure(figsize=(6, 4))
plt.scatter(df['Temperature'], df['Humidity'], alpha=0.5)
plt.title('Humidity vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.savefig('humidity_vs_temperature.png')
plt.show()

# Combined plot
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
axs[0].plot(df['Date'], df['Temperature'], color='tomato')
axs[0].set_title('Daily Temperature')
axs[1].bar(monthly_rainfall.index.astype(str), monthly_rainfall.values, color='skyblue')
axs[1].set_title('Monthly Rainfall')
plt.tight_layout()
plt.savefig('combined_plot.png')
plt.show()

#Task 5: Grouping and Aggregation
# Group by month
monthly_avg = df.groupby('Month').mean()

# Group by season (example for India)
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Summer'
    elif month in [6, 7, 8, 9]:
        return 'Monsoon'
    else:
        return 'Post-Monsoon'

df['Season'] = df['Date'].dt.month.map(get_season)
seasonal_stats = df.groupby('Season').agg({
    'Temperature': 'mean',
    'Rainfall': 'sum',
    'Humidity': 'mean'
})

#Task 6: Export and Storytelling
df.to_csv('cleaned_weather_data.csv', index=False)



