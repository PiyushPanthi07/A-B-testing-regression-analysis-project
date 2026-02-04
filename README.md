# A/B Testing Regression Analysis Project

A comprehensive analysis comparing Facebook Ads vs. Google AdWords performance using A/B testing, statistical inference, regression modeling, and time-series trends.

## Overview
This project evaluates two advertising platforms to determine which performs better on key marketing metrics such as clicks, conversions, CTR, and cost efficiency. It combines exploratory data analysis, hypothesis testing, and predictive modeling to support data‑driven decision‑making.

## Objectives
- Compare Facebook and AdWords performance across clicks and conversions.
- Test whether observed differences are statistically significant.
- Build a regression model to forecast conversions based on clicks.
- Identify weekly and monthly seasonality patterns.

## Dataset
File: A_B_testing_dataset.csv

Key columns used:
- date_of_campaign_of_campaign
- facebook_ad_clicks, adword_ad_clicks
- facebook_ad_conversions, adword_ad_conversions
- facebook_ctr, adword_ctr
- facebook_cost_per_ad, adword_cost_per_ad
- facebook_conversion_rate, adword_conversion_rate
- facebook_cost_per_click, adword_cost_per_click

## Methods & Tools
- Data cleaning for currency and percentage fields
- Exploratory Data Analysis (histograms, boxplots, scatter plots)
- Hypothesis testing with independent t‑test
- Linear regression for conversion prediction
- Time series analysis by weekday and month

## Project Structure
- A_B_Testing.ipynb — end‑to‑end analysis notebook
- A_B_testing_dataset.csv — dataset used for analysis
- fix_notebook_columns.py — helper script for cleaning/formatting

## Results Summary
- The notebook reports descriptive statistics and visual comparisons.
- T‑test indicates whether differences between platforms are significant.
- Regression model provides conversion forecasts with R² and MSE.
- Weekly and monthly plots highlight seasonality in conversions.

## How to Run
1. Open the notebook A_B_Testing.ipynb in Jupyter or VS Code.
2. Run cells from top to bottom.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit‑learn
- statsmodels
- scipy

## Notes
If you encounter formatting issues in the dataset, run fix_notebook_columns.py before executing the notebook.

## Author
Piyush Panthi

## License
MIT
