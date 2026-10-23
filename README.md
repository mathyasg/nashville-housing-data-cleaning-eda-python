# Nashville Housing Data Cleaning & Analysis in Python

## Project Overview

This project demonstrates a complete **end-to-end data analytics workflow** on the Nashville Housing dataset. It covers thorough data cleaning, formal data quality documentation, explicit data-type enforcement, Exploratory Data Analysis (EDA), and visualizations using Python.

The goal was to transform raw, messy real-world data into a clean, well-documented, analysis-ready dataset and extract clear insights about price trends, geographic patterns, and property value drivers.

---

## Dataset

- **Raw / Original File**: `Nashville Housing Data for Data Cleaning.xlsx` (56,477 records)
- **Cleaned File**: `housing_data_cleaned.csv`
- **Time Period**: 2013 – 2016
- **Main Challenges**: Missing addresses, inconsistent values, unsplit address fields, duplicates, improper date formats, and mixed data types

---

## Repository Structure

```
nashville-housing-data-cleaning-eda-python/
├── README.md
├── data_dictionary.md                          # Formal field definitions, data types & business rules
├── SOP_data_quality_and_cleaning.md            # Standard Operating Procedure for cleaning, validation & type enforcement
├── nashville_housing_python_cleaning.py        # Data cleaning + data-type enforcement pipeline
├── nashville_housing_eda.py                    # EDA and visualizations
├── Nashville Housing Data for Data Cleaning.xlsx   # Raw data
├── housing_data_cleaned.csv                    # Cleaned dataset (with enforced types)
├── 01_avg_sale_price_per_year.png
├── 02_avg_price_by_year_built.png
├── 03_top_cities.png
└── 04_average_sale_price_top5.png
```

---

## Data Quality & Documentation

This project follows formal data management practices aligned with professional digital systems and analytics work:

- **Data Dictionary** (`data_dictionary.md`): Defines every field in the cleaned dataset, including data types, allowed values, business rules, source, and ownership.
- **Standard Operating Procedure** (`SOP_data_quality_and_cleaning.md`): Documents the complete, repeatable process for validation, cleaning, data-type enforcement, acceptance criteria, roles, and version control.
- Automated quality checks for missing values, duplicates, date conversion, address standardization, and value consistency.
- Explicit data-type enforcement so the cleaned file matches the documented schema (nullable integers, float, string, datetime).
- Clear audit trail of all transformations applied.

These documents make the cleaning process transparent, reproducible, and suitable for handover, training, or audit.

---

## Data Cleaning Summary

The cleaning pipeline (`nashville_housing_python_cleaning.py`) addresses common real-world data quality issues:

- Converted Excel serial / original dates to proper datetime format (`SaleDateConverted`)
- Populated missing `PropertyAddress` values using `ParcelID` logic
- Split `PropertyAddress` and `OwnerAddress` into structured components (Address, City, State)
- Standardized the `SoldAsVacant` column (Y/N → Yes/No)
- Removed duplicate records based on key fields
- Dropped unused original columns after transformation
- **Enforced data types** according to the Data Dictionary (nullable Int64, float64, string, datetime)

Full details of the cleaning process are documented in `SOP_data_quality_and_cleaning.md`.

---

## Exploratory Data Analysis (EDA)

After the cleaned dataset is produced, the script `nashville_housing_eda.py` performs exploratory analysis and generates the following visualizations:

1. **Average Sale Price per Year (2013–2016)**  
   Line chart showing the upward trend in average sale prices over the four-year period.  
   → `01_avg_sale_price_per_year.png`

2. **Average Sale Price by Year Built**  
   Bar chart grouping properties by decade built (`<1980`, `1980s`, `1990s`, `2000s`, `2010s`) and showing the clear price premium for newer homes.  
   → `02_avg_price_by_year_built.png`

3. **Top 5 Cities by Number of Housing Sales**  
   Bar chart ranking the cities with the highest transaction volume.  
   → `03_top_cities.png`

4. **Top 5 Cities by Average Sale Price**  
   Bar chart ranking the cities with the highest average sale prices, highlighting market segmentation.  
   → `04_average_sale_price_top5.png`

**Notes on analysis decisions:**
- Rows with missing or “Unknown” city values were excluded from geographic visualizations to improve reliability.
- The `SoldAsVacant` feature was analyzed but excluded from the final set of charts because it is extremely imbalanced (~99% Occupied vs ~1% Vacant), making visual insights unreliable.

---

## Key Insights from Exploratory Data Analysis

1. **Upward Price Trend (2013–2016)**  
   Average sale prices showed a steady increase over the four-year period, indicating a strengthening housing market in Nashville.

2. **Significant Premium for Newer Homes**  
   Homes built in the 2010s and later commanded substantially higher average sale prices compared to older properties, revealing strong buyer preference for modern construction.

3. **Geographic Concentration**  
   Housing sales are heavily concentrated in a small number of cities. The top 5 cities dominate both transaction volume and market value.

4. **Market Segmentation**  
   Different cities serve different market segments — some are high-volume markets with moderate prices, while others are premium markets with fewer transactions but significantly higher average sale prices.

5. **Strong Feature Relationships**  
   Correlation analysis showed very high positive correlations between `SalePrice`, `TotalValue`, and `BuildingValue`, confirming internal consistency of the dataset.

---

## Technologies Used

- **Python**: pandas, matplotlib, seaborn
- Reproducible workflows with clean, well-documented scripts
- Formal data quality documentation (Data Dictionary + SOP)
- Explicit data-type enforcement for schema consistency

---

## How to Reproduce

1. Clone the repository
2. Install dependencies:  
   `pip install pandas openpyxl matplotlib seaborn`
3. Run data cleaning + type enforcement (this also applies all quality checks):  
   `python nashville_housing_python_cleaning.py`
4. Run EDA and generate visualizations:  
   `python nashville_housing_eda.py`

---

## Future Improvements

- Build an interactive Power BI / Tableau dashboard
- Develop a machine learning model for price prediction
- Expand automated data quality rules and anomaly detection

---

## Author

**Mathyas Tilahun**  
Data Analyst  
· [LinkedIn](https://www.linkedin.com/in/mathyas-g)
