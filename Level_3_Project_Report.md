
# Business Intelligence Analytics System
## Project Report — Level 3

### 1. Introduction
The Business Intelligence Analytics System analyzes retail sales
data to support data-driven business decisions.

### 2. Objectives
- Analyze sales, profit, quantity, region, and product categories.
- Clean and transform data using Python.
- Store and query sales data using SQLite.
- Build an interactive Power BI dashboard.
- Develop and evaluate a monthly sales forecasting model.

### 3. Tools and Technologies
Python, Pandas, NumPy, Matplotlib, SQLite, SQL,
Scikit-learn, and Microsoft Power BI.

### 4. Dataset
The dashboard and ETL analysis use the 9,994-row,
13-column Superstore dataset.
A date-enabled 21-column version is used for forecasting.

### 5. ETL Process
Extract: Load the sales CSV dataset.
Transform: Standardize column names, remove duplicate records,
convert numeric fields, and remove rows missing required values.
Load: Store the cleaned records in the SQLite sales_cleaned table.

### 6. SQL Analysis
SQL queries were used to calculate overall sales, profit,
quantity, regional performance, category performance,
and sub-category profitability.

### 7. Power BI Dashboard
The dashboard includes KPI cards for total sales, total profit,
and total quantity. Charts show sales by region, sub-category,
and category. Region, category, and segment slicers support
interactive exploration.

### 8. Forecasting Methodology
Monthly sales were aggregated from January 2014 to December 2017,
giving 48 monthly observations. A Random Forest Regressor was
trained on the first 36 months and tested on the final 12 months.
A seasonal baseline was used for comparison.

### 9. Model Evaluation
Random Forest:
MAE = 13,764.75
RMSE = 15,995.80

Seasonal baseline:
MAE = 18,031.99
RMSE = 20,424.97

Random Forest achieved approximately 23.7% lower MAE than
the seasonal baseline on the same test period. Prediction
errors remain substantial, so the model should be treated
as a baseline rather than a highly accurate forecasting system.

### 10. Forecast
The trained model generated estimated monthly sales forecasts
for January to December 2018. These are model predictions,
not actual sales figures.

### 11. Conclusion
The project demonstrates a complete basic business intelligence
workflow involving data preparation, SQL analysis, dashboard
visualization, and predictive modelling. Further work could
include improved forecasting methods, more robust validation,
and automated data refresh.

### 12. Deliverables
- Power BI dashboard
- SQLite database
- Python notebook
- ETL script
- Monthly forecast CSV and graph
- Model evaluation CSV
- README documentation
- Dashboard screenshots
