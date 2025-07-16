# import pandas as pd

# # Load weather data
# weather = pd.read_csv('weather_data.csv')
# weather.columns = weather.columns.str.strip()  # Strip whitespace

# # Rename necessary columns to lowercase
# weather = weather.rename(columns={'YEAR': 'year', 'MO': 'month', 'DY': 'day'})

# # Now this will work:
# weather['date'] = pd.to_datetime(weather[['year', 'month', 'day']])


# # Rename columns
# weather = weather.rename(columns={
#     'T2M': 'temp',
#     'PRECTOTCORR': 'rainfall',
#     'RH2M': 'humidity'
# })

# # Keep relevant columns
# weather = weather[['date', 'temp', 'rainfall', 'humidity']]

# # Load observation data
# obs = pd.read_csv('daily_onion_prices_sorted.csv', header=None, names=['date', 'min', 'max', 'avg', 'location'])
# obs['date'] = pd.to_datetime(obs['date'])

# # Merge on date
# merged = obs.merge(weather, on='date', how='left')

# # Create new features
# merged['rain_3day_sum'] = merged['rainfall'].rolling(window=3, min_periods=1).sum()
# merged['rain_flag'] = (merged['rainfall'] > 5).astype(int)
# merged['temp_lag'] = merged['temp'].shift(1)
# merged['humidity_diff'] = merged['humidity'].diff()

# # Drop rows where weather info is missing (optional)
# merged = merged.dropna(subset=['temp', 'rainfall', 'humidity'])

# # Output to CSV
# merged.to_csv('merged_data.csv', index=False)


import pandas as pd

# Load your weather/location data
weather_df = pd.read_csv("merged_data.csv", parse_dates=["date"])

# Load the trends data
trends_df = pd.read_csv("bangladesh_onion_trends.csv", parse_dates=["date"])

# Merge on 'date'
merged_df = pd.merge(weather_df, trends_df, on='date', how='left')

# Save merged data
merged_df.to_csv("merged_data_with_gtrends.csv", index=False)

print(merged_df.head())
