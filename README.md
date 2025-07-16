# 🧅 Onion Price Forecasting in Bangladesh 🇧🇩  
*Predicting short-term real-time price changes using weather, behavioral data & machine learning*


## 📌 Project Overview

This project explores how **climate conditions** and **public interest (Google Trends)** influence the **daily market price of onions in Dhaka, Bangladesh**. It leverages machine learning models (XGBoost, Random Forest) to predict short-term price changes using real-world signals.

🔍 **Why this matters:**  
Onion prices in Bangladesh are highly volatile, often affected by:
- Monsoon and flood conditions
- Import/export restrictions
- Consumer panic triggered by media or news

This volatility creates serious challenges for low-income households and policymakers. Forecasting prices can help enable better **planning**, **transparency**, and **intervention timing**.

---

## 🧠 Objectives

- Collect and clean real-world market price data from Bangladesh’s **TCB (Trading Corporation)** website
- Engineer features from:
  - 🌀 **Weather** (temperature, rainfall, humidity)
  - 🔍 **Google Trends** (English and Bangla search interest)
- Build predictive models to forecast short-term price changes
- Identify and explain which factors influence price volatility most

---

## 🗃️ Dataset Summary

| Source | Description |
|--------|-------------|
| 🏷️ TCB Notice Board | Daily onion price data (min, max, avg) from 2021–2025 |
| ☁️ NASA POWER data | Historical daily weather data (Dhaka-specific) |
| 🔍 Google Trends | Daily search volume for “onion” and “পেঁয়াজ” |

✅ After merging, cleaning, and aligning, the final dataset includes:

- 982 records
- Columns: date,min,max,avg,location,temp,rainfall,humidity,rain_3day_sum,rain_flag,temp_lag,humidity_diff,trend_score_পেঁয়াজ,trend_score_onion,trend_score_পেঁয়াজ_lag1,trend_score_পেঁয়াজ_avg3,trend_score_পেঁয়াজ_spike,trend_score_onion_lag1,trend_score_onion_avg3,trend_score_onion_spike


---

## 🧮 Feature Engineering

Key features created:

- 📅 **Time Lags:** 1-day lag for trend/temperature
- 🌧️ **Cumulative Weather Signals:** 3-day rain sum, rain flag
- 📈 **Behavioral Features:**
  - Trend score lag
  - 3-day average trend score
  - Spike detection based on threshold change

---

## 🛠️ Modeling

### Models Compared:
- ✅ **XGBoost Regressor**
- ✅ **Random Forest Regressor**

| Metric | XGBoost | Random Forest |
|--------|---------|----------------|
| 📉 RMSE | **13.17** | 13.66 |
| 📊 MAE | 7.70 | **7.58** |
| 🔍 R² Score | **0.824** | 0.811 |

✅ XGBoost offered the best overall performance, capturing complex weather-behavior-price interactions.

---

## 🔍 Key Findings

- 📈 **Google Trend spikes** (especially in Bangla) often **preceded price hikes**, likely reflecting panic-buying or news coverage
- 🌧️ **Rainfall sums and humidity shifts** played a significant role during monsoon months
- ⏳ Combining trend, weather, and lagged features gave the best predictive power

---

## 📊 Visualizations

- 📉 Actual vs. Predicted Price Plot
- 🔍 Google Trend Spikes vs. Price Spikes
- ☁️ Rainfall vs. Price Dip Periods

*(Plots available in `veganalyzer_eda.ipynb` and `/outputs/` folders)*

---

## 🛠️ Tools Used

- **Python** (pandas, numpy, scikit-learn)
- **XGBoost, Random Forest**
- **Google Trends API (pytrends)**
- **weatherapi.com API**
- **Matplotlib / Seaborn**
- **Jupyter Notebook**

---

