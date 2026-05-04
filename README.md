# AI Job Risk & Salary Visualization Dashboard

This project analyzes how AI automation risk affects salaries, job demand, and job structure from 2015 to 2035. It explores how different job sectors and experience levels are impacted by increasing levels of AI-driven automation over time with a focus on identifying long-term job market shifts rather than short-term fluctuations.

The dataset is preprocessed using Python, specifically the Pandas and NumPy libraries, to clean, standardize, and engineer key features (such as job sectors, experience levels) and derived metrics like risk-adjusted salary and AI risk categories. These transformations ensure consistency and allow for meaningful comparisons across the dataset.

The processed dataset is then visualized using an interactive Tableau Public dashboard. The dashboard enables users to explore trends dynamically across time, job sectors, and risk levels, supporting deeper insight into how AI may reshape employment patterns, salary distributions, and job demand structures in the evolving job market.

---

## Project Structure

- `ai_job_dataset.csv`: Original raw dataset
- `preprocessing.py`: Python script for data cleaning and feature engineering
- `cleaned_ai_jobs_final.csv`: Final processed dataset used in Tableau Public
- `README.md`: Project documentation
- `requirements.txt`: Python dependencies
- `final.twbx`: Tableau packaged dashboard

---

## Dataset

Dataset source:
https://www.kaggle.com/datasets/shree0910/ai-job-risk-and-salary-dataset-20152035

If not included locally, download and place `ai_job_dataset.csv` in the project folder.

---

## Dependencies

Install required Python libraries before running preprocessing:

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

1. Place the dataset (ai_job_dataset.csv) in the project folder  

2. Run the preprocessing script:

```bash
python preprocessing.py
```

3. This generates the cleaned dataset:

`cleaned_ai_jobs_final.csv`

4. Open Tableau Public and import the cleaned dataset to build the dashboard.

---

## How to View the Dashboard (Tableau)

Access the dashboard through the Tableau Public link: https://public.tableau.com/app/profile/xin.yu.zhang/viz/InfoVisFinal/Dashboard1?publish=yes

Or, this project includes a prebuilt Tableau file:

`final.twbx`

### Steps:
1. Install Tableau Public (free) or Tableau Desktop  
2. Open Tableau  
3. Click **File → Open**  
4. Select `final.twbx`  
5. The full interactive dashboard will load automatically  

---

## Example Usage

After preprocessing:
- Open `cleaned_ai_jobs_final.csv` in Excel or Python for data inspection and analysis
- Use the dataset for additional modeling, statistical analysis, or forecasting
- Load the dataset into Tableau if you want to modify or extend the visualizations
- The preprocessing ensures the dataset is cleaned, standardized, and ready for analysis

---

## Using the Dashboard (Tableau)

The dashboard is designed for interactive exploration of AI-driven job market trends.

### Getting Started:
- Open `final.twbx` using Tableau Public or Tableau Desktop or go to: https://public.tableau.com/app/profile/xin.yu.zhang/viz/InfoVisFinal/Dashboard1?publish=yes
- The dashboard will load with all visualizations already configured

### How to Explore:
- Hover over charts to view detailed values and tooltips
- Click on elements in one chart to highlight relationships across other charts (cross-filtering)

### What to Focus On:
- Long-term trends in AI automation risk (2015–2035)
- How salary changes correlate with increasing AI risk
- Differences in risk and salary across job sectors
- Relationship between job demand and automation exposure
- How experience level affects AI vulnerability

### Key Insight Goal:
- Understand how AI reshapes employment patterns over time rather than focusing on single-year snapshots

---

## Dashboard Overview

The interactive dashboard includes the following visualizations:

### 1. Time Series Analysis
- Line chart: Year vs Average Salary
- Line chart: Year vs Average AI Risk Score

These show how salary and automation risk evolve over time.

---

### 2. Job Sector Analysis
- Bar chart: Job Sector vs Average Salary
- Bar chart: Job Sector vs Average AI Risk Score

These compare economic value and automation risk across different job sectors.

---

### 3. Risk vs Salary Relationship
- Scatter plot: AI Risk Score vs Average Salary

This visual highlights the relationship between compensation and automation exposure.

---

### 4. Job Demand Distribution
- Treemap:
  - Color: Job Sector
  - Size: Total Job Openings

This shows which sectors dominate in job availability.

---

### 5. Experience Level Analysis
- Horizontal bar chart:
  - Experience Level vs Average AI Risk Score

This compares how automation risk varies across different experience levels.

---

## Key Feature Engineering Outputs

The preprocessing pipeline generated several derived features:

- Job Sector
- Experience Level
- AI risk categories (Low / Medium / High)
- Salary per job opening
- Risk-adjusted salary
- Log-transformed salary (for distribution stability)

---

## Notes

- The dashboard is fully interactive using Tableau filters and highlighting.
- Preprocessing ensures consistent aggregation across years, sectors, and job levels.
- The visual design prioritizes clarity, comparison, and trend discovery over time.
