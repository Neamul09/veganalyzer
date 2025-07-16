# import pandas as pd

# # Load the merged data with weather and trend columns
# merged_df = pd.read_csv("merged_data_with_gtrends.csv", parse_dates=["date"])

# # Forward fill missing values in both trend columns
# merged_df['trend_score_পেঁয়াজ'] = merged_df['trend_score_পেঁয়াজ'].ffill()
# merged_df['trend_score_onion'] = merged_df['trend_score_onion'].ffill()

# # Optional: Fill any remaining NaN at the top with 0 (if needed)
# # merged_df[['trend_score_পেঁয়াজ', 'trend_score_onion']] = merged_df[['trend_score_পেঁয়াজ', 'trend_score_onion']].fillna(0)

# # Save the forward-filled version
# merged_df.to_csv("merged_data_ffilled.csv", index=False)

# # Show first few rows
# print(merged_df.head(10))

import pandas as pd

# Load your data
df = pd.read_csv("merged_data_ffilled.csv", parse_dates=["date"])

# Sort by date just to be safe
df = df.sort_values("date").reset_index(drop=True)

# Define trend columns
trend_cols = ['trend_score_পেঁয়াজ', 'trend_score_onion']

# Create features
for col in trend_cols:
    # 1-day lag
    df[f"{col}_lag1"] = df[col].shift(1)

    # 3-day rolling average (including today)
    df[f"{col}_avg3"] = df[col].rolling(window=3, min_periods=1).mean()

    # Spike feature: 1 if today > 1.5 * 3-day average, else 0
    df[f"{col}_spike"] = (df[col] > 1.5 * df[f"{col}_avg3"]).astype(int)

# Save to new CSV
df.to_csv("final_data.csv", index=False)

# Display result
print(df[[ 'date',
           'trend_score_পেঁয়াজ', 'trend_score_পেঁয়াজ_lag1', 'trend_score_পেঁয়াজ_avg3', 'trend_score_পেঁয়াজ_spike',
           'trend_score_onion', 'trend_score_onion_lag1', 'trend_score_onion_avg3', 'trend_score_onion_spike'
         ]].head(10))
