import pandas as pd
import numpy as np

# Load the raw dataset
df = pd.read_csv("ai_job_dataset.csv")

# Clean up column names and remove any duplicate rows
df.columns = df.columns.str.strip().str.lower()
df = df.drop_duplicates()

# Keep only rows that have the key fields we actually need
df = df.dropna(subset=[
    "salary",
    "ai_risk_score",
    "year",
    "job_title",
    "job_openings",
    "experience_level"
])

# Convert important columns to numeric (coerce errors to NaN first)
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["ai_risk_score"] = pd.to_numeric(df["ai_risk_score"], errors="coerce")
df["job_openings"] = pd.to_numeric(df["job_openings"], errors="coerce")
df["skill_demand_score"] = pd.to_numeric(df["skill_demand_score"], errors="coerce")

# Drop any rows that failed conversion
df = df.dropna(subset=["year", "salary", "ai_risk_score", "job_openings"])

# Finalize types for consistency
df["year"] = df["year"].astype(int)
df["job_openings"] = df["job_openings"].astype(int)

# For optional fields, fill missing values with something reasonable
df["skill_demand_score"] = df["skill_demand_score"].fillna(df["skill_demand_score"].median())

# --- Feature engineering starts here ---

# Log-transform salary to reduce skew (helps visualization a lot)
df["salary_log"] = np.log(df["salary"].clip(lower=1))

# Turn the continuous risk score into simple categories
def risk_category(score):
    if score < 0.3:
        return "Low Risk"
    elif score < 0.6:
        return "Medium Risk"
    else:
        return "High Risk"

df["ai_risk_category_clean"] = df["ai_risk_score"].apply(risk_category)

# Bucket job demand into easier-to-read groups
def demand_category(x):
    if x < 10000:
        return "Low Demand"
    elif x < 30000:
        return "Medium Demand"
    else:
        return "High Demand"

df["job_demand_category"] = df["job_openings"].apply(demand_category)

# Map experience levels to numbers so Tableau can sort them properly
experience_map = {"Entry": 1, "Mid": 2, "Senior": 3}
df["experience_level"] = df["experience_level"].fillna("Entry")
df["experience_level_num"] = df["experience_level"].map(experience_map).fillna(1)

# Create a simple "efficiency" metric: salary relative to number of openings
df["salary_per_opening"] = df["salary"] / (df["job_openings"] + 1)

# Adjust salary by AI risk to estimate long-term value (key insight feature)
df["risk_adjusted_salary"] = df["salary"] * (1 - df["ai_risk_score"])

# Group similar job titles into broader categories for cleaner visuals
def get_job_sector(title):
    if pd.isna(title):
        return "Other"

    title = str(title).lower()

    if any(x in title for x in ["data scientist", "data analyst", "ml engineer", "ai researcher"]):
        return "Data & AI"
    elif any(x in title for x in ["software engineer", "backend", "frontend"]):
        return "Software Engineering"
    elif any(x in title for x in ["devops", "cloud"]):
        return "Cloud & DevOps"
    elif any(x in title for x in ["cybersecurity", "security"]):
        return "Cybersecurity"
    elif any(x in title for x in ["business analyst", "product manager"]):
        return "Business & Analytics"
    else:
        return "Other"

df["job_sector"] = df["job_title"].apply(get_job_sector)

# Fill any remaining missing categorical values
df = df.fillna({
    "job_sector": "Other",
    "ai_risk_category_clean": "Unknown",
    "job_demand_category": "Unknown"
})

# Save the cleaned dataset for Tableau
df.to_csv("cleaned_ai_jobs_final.csv", index=False)