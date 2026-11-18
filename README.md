
# 🏦 Bank Customer Data Analysis Dashboard

## 1. Project Overview

This project is an interactive dashboard for analyzing bank customer data using Python.

The dashboard provides data exploration, statistical analysis, data visualization, and customer data insights through Streamlit.

The main objective is to understand customer data characteristics and identify meaningful patterns through exploratory data analysis (EDA).

## 2. Dataset

**Dataset:** Bank Customer Dataset

**Source:**
https://github.com/BU-SKHY/Bank/raw/main/bank_customer%20(1).xlsx

**File Format:** Excel (.xlsx)

The dataset is loaded directly from GitHub.

Users can also upload their own Excel files through the dashboard.

## 3. Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive dashboard |
| Pandas | Data processing |
| NumPy | Numerical analysis |
| Plotly | Interactive visualization |
| OpenPyXL | Excel file processing |

## 4. Project Structure

```text
Bank-Customer-Analysis/
│
├── app.py
├── README.md
└── requirements.txt
```

## 5. Main Features

### 1) Dashboard Overview
- Total number of records
- Total number of columns
- Missing values
- Duplicate records

### 2) Dataset Preview
- Display dataset records
- Check column names and data types
- Statistical summary

### 3) Missing Value Analysis
- Identify missing values
- Calculate missing value percentages
- Visualize missing values

### 4) Numerical Data Analysis
- Descriptive statistics
- Histogram
- Boxplot
- Distribution analysis

### 5) Categorical Data Analysis
- Category frequency
- Bar chart
- Pie chart
- Category distribution

### 6) Correlation Analysis
- Correlation matrix
- Heatmap visualization
- Identify relationships between numerical variables

### 7) Relationship Analysis
- Interactive scatter plots
- Compare numerical variables
- Trendline analysis

### 8) Data Download
- Download filtered data as CSV

## 6. Installation

### Step 1. Clone Repository

```bash
git clone https://github.com/your-username/Bank-Customer-Analysis.git

cd Bank-Customer-Analysis
```

### Step 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3. Run Streamlit

```bash
streamlit run app.py
```

### Step 4. Open Dashboard

Open the following address in your browser:

```text
http://localhost:8501
```

## 7. Requirements

```text
streamlit
pandas
numpy
plotly
openpyxl
statsmodels
```

## 8. Expected Results

This project helps users:

- Understand bank customer data.
- Identify missing and duplicate values.
- Explore numerical and categorical variables.
- Discover correlations between variables.
- Visualize customer data interactively.
- Export filtered datasets for further analysis.

## 9. Future Improvements

- Customer segmentation using K-Means clustering.
- Customer churn prediction using Machine Learning.
- Customer behavior analysis.
- Predictive modeling.
- Advanced banking business insights.

## 10. Author

Bank Customer Data Analysis Project

**Tools:** Python, Streamlit, Pandas, Plotly
