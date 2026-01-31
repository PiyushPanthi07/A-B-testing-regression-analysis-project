# Marketing Campaign Analysis: A/B Testing & Regression

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit_Learn-orange)
![Statsmodels](https://img.shields.io/badge/Statistics-Hypothesis_Testing-green)

## 📌 Executive Summary
This project analyzes the performance of two distinct marketing campaigns (Facebook Ads vs. AdWords) conducted over a 12-month period. The primary objective was to determine which platform yields a better Return on Investment (ROI) and to predict future conversions based on ad engagement.

**Key Outcome:** The analysis confirmed with **95% statistical confidence** that Facebook Ads significantly outperform AdWords in daily conversion rates. Additionally, a linear regression model was developed to predict conversions with **76% accuracy (R² Score)**.

---

## 📂 Business Problem
**Objective:** A marketing agency ran two parallel campaigns throughout 2019. The stakeholders need to optimize their advertising budget by identifying the most effective platform in terms of:
1. **Clicks & Conversions:** Which platform drives more user action?
2. **Cost Efficiency:** Which platform offers a better Cost Per Conversion (CPC)?
3. **Predictability:** Can we forecast conversions based on ad clicks?

**KPIs Analyzed:**
* Click-Through Rate (CTR)
* Conversion Rate
* Cost Per Click (CPC)
* Return on Ad Spend (ROAS)

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Statistical Analysis:** Statsmodels (T-Test, Cointegration Test)
* **Machine Learning:** Scikit-Learn (Linear Regression)

---

## 📊 Methodology & Analysis

### 1. Data Cleaning & Engineering
* Processed a raw dataset containing 365 days of campaign metrics (Views, Clicks, Cost, Conversions).
* Handled data type constraints by cleaning currency symbols (`$`) and percentage signs (`%`) to enable numerical analysis.
* Engineered new features including `Month` and `Day_of_Week` to detect temporal trends.

### 2. Exploratory Data Analysis (EDA)
* **Distribution Analysis:** Analyzed the skewness of clicks and conversions; identified that data was symmetrical with no significant outliers.
* **Correlation Matrix:** Discovered a **strong positive correlation (0.87)** between Clicks and Conversions for Facebook, compared to a moderate correlation (0.45) for AdWords.

### 3. Hypothesis Testing (A/B Testing)
Performed an independent two-sample **T-Test** to compare the mean daily conversions of both platforms.
* **Null Hypothesis ($H_0$):** There is no difference in mean conversions between Facebook and AdWords.
* **Alternate Hypothesis ($H_1$):** There is a significant difference in performance.
* **Result:** Rejected $H_0$ with a T-statistic of **32.8** and a p-value < 0.05.
* **Insight:** Facebook Ads demonstrated a statistically significant higher average conversion rate (~11.7/day) vs. AdWords (~5.9/day).

### 4. Regression Analysis
Developed a Linear Regression model to quantify the relationship between Ad Clicks (Independent Variable) and Conversions (Dependent Variable).
* **Model Performance:** Achieved an **R² Score of 0.76**, indicating the model explains 76% of the variance in conversion data.
* **Business Application:** This model allows the team to forecast expected conversions for proposed budget allocations.

### 5. Time Series Trends
* **Weekly Trends:** Identified that **Mondays and Tuesdays** consistently show the highest conversion rates, suggesting users are most responsive at the start of the work week.
* **Seasonality:** Observed dips in conversion efficiency during February, April, and November, indicating seasonal factors affecting user behavior.

---

## 💡 Key Findings & Recommendations

| Metric | Facebook Ads | AdWords | Verdict |
| :--- | :--- | :--- | :--- |
| **Correlation (Click-to-Sale)** | 0.87 (Strong) | 0.45 (Moderate) | Facebook leads clearly to sales |
| **Mean Daily Conversions** | ~11.7 | ~5.9 | Facebook volume is 2x higher |
| **Cost Efficiency** | High | Moderate | Facebook provides better ROI |

**Strategic Recommendations:**
1.  **Budget Reallocation:** Shift 60-70% of the ad budget to Facebook Ads, as they drive double the conversions for similar engagement.
2.  **Schedule Optimization:** Increase bidding caps on **Mondays and Tuesdays** to capitalize on peak weekly engagement.
3.  **AdWords Review:** Investigate the low correlation on AdWords; high clicks but low conversions suggest a disconnect between ad copy and landing page relevance (high bounce rate).

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/marketing-campaign-analysis.git](https://github.com/yourusername/marketing-campaign-analysis.git)
