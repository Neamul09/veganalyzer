import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

def get_daily_trends_multi(keywords, start_date, end_date, geo='BD'):
    date_ranges = pd.date_range(start=start_date, end=end_date, freq='270D').tolist()
    if date_ranges[-1] != pd.to_datetime(end_date):
        date_ranges.append(pd.to_datetime(end_date))

    all_data = pd.DataFrame()

    for i in range(len(date_ranges) - 1):
        start = date_ranges[i].strftime('%Y-%m-%d')
        end = date_ranges[i + 1].strftime('%Y-%m-%d')
        timeframe = f'{start} {end}'

        pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')

        data = pytrends.interest_over_time()
        if not data.empty:
            data = data.reset_index()
            data = data[['date'] + keywords]
            all_data = pd.concat([all_data, data], ignore_index=True)

    # Remove duplicates, NA
    all_data = all_data.drop_duplicates(subset='date').dropna()

    # Rename columns
    col_renames = {kw: f"trend_score_{kw}" for kw in keywords}
    all_data.rename(columns=col_renames, inplace=True)

    return all_data

# Define keywords and date range
keywords = ["পেঁয়াজ", "onion"]
start_date = "2021-05-17"
end_date = datetime.today().strftime('%Y-%m-%d')

# Get trends data
df = get_daily_trends_multi(keywords, start_date, end_date)

# Save to CSV
df.to_csv("bangladesh_onion_trends.csv", index=False)

print(df.head())
