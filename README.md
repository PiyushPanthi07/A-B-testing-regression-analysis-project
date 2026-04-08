# 📊 A/B Testing: Facebook vs Google AdWords — Marketing Campaign Analysis

> **Decision-focused analysis** of 365-day ad campaign data to determine optimal budget allocation between two platforms using statistical hypothesis testing, correlation analysis, and predictive modelling.

---

## 🎯 Business Objective

A marketing agency running parallel campaigns on **Facebook** and **Google AdWords** throughout 2019 needed a data-driven answer to one question:

> *Which platform delivers more conversions per dollar spent — and should we reallocate budget?*

---

## 📁 Project Structure

```
ab-testing-marketing/
│
├── AB_Testing_Marketing_Campaigns.ipynb   # Main analysis notebook
├── ABmarketing_campaign.csv               # Raw dataset (365 daily records)
└── README.md
```

---

## 📊 Dataset

| Field | Description |
|---|---|
| Date | Daily observation, Jan 1 – Dec 31, 2019 |
| Ad Views | Total impressions per platform per day |
| Ad Clicks | Total clicks per platform per day |
| Ad Conversions | Total conversions per platform per day |
| Cost per Ad | Daily ad spend per platform |
| CTR | Click-Through Rate (Clicks / Views) |
| Conversion Rate | Conversions / Clicks |
| CPC | Cost Per Click (Ad Cost / Clicks) |

**365 rows × 17 columns. No missing values.**

---

## 🔑 Key Results

| Metric | Facebook | AdWords | Winner |
|---|---|---|---|
| Total Conversions | **4,286** | 2,183 | ✅ Facebook (+96%) |
| Total Ad Spend | **$32,040** | $49,266 | ✅ Facebook ($17K cheaper) |
| Blended CPA | **$7.48** | $22.57 | ✅ Facebook (3× cheaper) |
| Mean Daily CTR | **2.20%** | 1.30% | ✅ Facebook |
| Mean Conversion Rate | **27.15%** | 10.18% | ✅ Facebook |
| Mean CPC | **$2.19** | $2.38 | ✅ Facebook (marginal) |
| Clicks → Conv Correlation | **r = 0.874** | r = 0.448 | ✅ Facebook |

---

## 🧪 Statistical Test

**Test:** Welch's Two-Sample t-test (one-sided, `alternative='greater'`)  
**Rationale:** Unequal variance confirmed via Levene's test (p < 0.05)

| | Value |
|---|---|
| H₀ | µ_Facebook ≤ µ_AdWords |
| H₁ | µ_Facebook > µ_AdWords |
| T-statistic | 32.88 |
| P-value (one-sided) | 4.67×10⁻¹³⁴ |
| Cohen's d | > 2.0 (Very large effect) |
| **Verdict** | **Reject H₀. Facebook's advantage is statistically conclusive.** |

---

## 📈 Predictive Model

A **Linear Regression** model was built to forecast Facebook conversions from daily clicks.

| | Train | Test (held-out 20%) |
|---|---|---|
| R² | 0.770 | 0.763 |
| RMSE | ~1.8 conversions | ~1.9 conversions |

> Each additional click on Facebook generates approximately **+0.22 conversions** on average.

---

## 📅 Temporal Insights

**Day of week:** Monday and Tuesday are peak conversion days for Facebook.

**Monthly CPA (Facebook):**
- Best month: **November** (~$6.88/conversion)
- Worst month: **February** (~$8.38/conversion)
- CPA is stable year-round — range of only ~$1.50

**Monthly CPA (AdWords):**
- Range: $21.55 – $23.93
- Higher AND more volatile than Facebook

---

## 💡 Recommendations

1. **Reallocate budget:** Shift from 39/61 (FB/AW) split to at least **70/30**. Same total spend → ~20% more conversions.
2. **Timing:** Concentrate high-spend days on **Monday & Tuesday**.
3. **Seasonal burst:** Increase Facebook budget in **November, September, and May** for lowest CPA.
4. **Do not kill AdWords** — audit keyword targeting and landing pages to diagnose the low 10.2% conversion rate before defunding entirely.
5. **Use the regression model** as a daily conversion forecast tool during campaign planning.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas & NumPy | Data wrangling |
| Matplotlib & Seaborn | Visualisation |
| SciPy | Hypothesis testing (Welch's t-test, Levene's) |
| Scikit-learn | Linear regression, train/test split |

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/ab-testing-marketing.git
cd ab-testing-marketing

# Install dependencies
pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter

# Launch notebook
jupyter notebook AB_Testing_Marketing_Campaigns.ipynb
```

---

## 👤 Author

**Piyush Panthi**  
B.Tech AI & Robotics — MITS Gwalior  
[LinkedIn]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/piyushpanthi/)) | [GitHub]([https://github.com/yourusername](https://github.com/PiyushPanthi07))
