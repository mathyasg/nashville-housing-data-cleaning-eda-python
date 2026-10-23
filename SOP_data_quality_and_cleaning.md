# Standard Operating Procedure (SOP)  
**Data Quality Validation & Cleaning – Nashville Housing Dataset**

**Version:** 1.1  
**Effective Date:** 2026-10-23  
**Owner:** Mathyas Tilahun  
**Review Cycle:** Annual or after major process change  

---

## 1. Purpose
This Standard Operating Procedure (SOP) defines the standard, repeatable process for validating, cleaning, enforcing data types, and preparing the Nashville Housing dataset so that it is analysis-ready, reproducible, and governed. It ensures consistent application of data quality rules, documentation of decisions, and clear responsibilities.

---

## 2. Scope
This SOP applies to:
- Ingestion of the raw Nashville Housing Excel file
- Automated and manual data quality checks
- Cleaning and transformation steps
- Explicit data-type enforcement according to the Data Dictionary
- Creation of the final cleaned dataset
- Updating of the Data Dictionary and related documentation

**Out of scope:** Exploratory Data Analysis (EDA) and visualization steps. Those are documented and executed separately in `nashville_housing_eda.py` (see Project README for details).

---

## 3. Prerequisites
- Python environment with `pandas` and `openpyxl` installed
- Access to the raw file: `Nashville Housing Data for Data Cleaning.xlsx`
- Current version of this SOP and the Data Dictionary (`data_dictionary.md`)
- Working directory containing the cleaning script: `nashville_housing_python_cleaning.py`

---

## 4. Procedure – Step by Step

### Step 1: Load Raw Data
1. Open a terminal in the project directory.
2. Run:  
   `python nashville_housing_python_cleaning.py`
3. Confirm the script prints the original row count (expected ≈ 56,477).

### Step 2: Structural Cleaning & Validation
The cleaning script performs the following checks and transformations in sequence:

1. **Date Conversion**  
   - Convert `SaleDate` to proper datetime → new column `SaleDateConverted`.

2. **Missing PropertyAddress Population**  
   - Identify rows where `PropertyAddress` is null.  
   - Create a lookup map from non-null `ParcelID` → `PropertyAddress`.  
   - Populate missing addresses where a matching `ParcelID` exists.

3. **Address Splitting**  
   - Split `PropertyAddress` on the first comma into `PropertySplitAddress` and `PropertySplitCity`.  
   - Split `OwnerAddress` into `OwnerSplitAddress`, `OwnerSplitCity`, and `OwnerSplitState`.  
   - Strip leading/trailing whitespace from all new address components.

4. **Standardization of SoldAsVacant**  
   - Replace “Y” → “Yes” and “N” → “No”.

5. **Duplicate Detection & Removal**  
   - Identify duplicates using the key combination:  
     `ParcelID`, `PropertyAddress`, `SalePrice`, `SaleDate`, `LegalReference`.  
   - Keep the first occurrence; drop subsequent duplicates.

6. **Column Dropping**  
   - Remove original columns no longer needed: `OwnerAddress`, `TaxDistrict`, `PropertyAddress`, `SaleDate`.

### Step 3: Enforce Data Types
After structural cleaning, all columns are explicitly cast to the data types defined in the Data Dictionary:
- Integer columns → pandas nullable `Int64` (preserves missing values as `<NA>`)
- Text columns → `string` dtype
- `Acreage` → `float64`
- `SaleDateConverted` → datetime

### Step 4: Generate & Review Quality Summary
- The script prints original row count, cleaned row count, final shape, and final dtypes.
- Manually review the printed summary.  
- If unexpected row loss or type issues appear, investigate before proceeding.

### Step 5: Save Cleaned Dataset
- The script automatically saves the cleaned data as:  
  `housing_data_cleaned.csv` (with headers, no index, and enforced data types).

### Step 6: Update Documentation
1. Open `data_dictionary.md`.  
2. Verify all final columns are documented with correct definitions, data types, and business rules.  
3. Update the “Last Updated” date and Change Log if any field definitions or types changed.  
4. Confirm this SOP still accurately reflects the process. Update version and date if process changes were made.

### Step 7: Archive & Version
- Keep the raw Excel file unchanged.  
- Store the cleaned CSV with a clear version or date if multiple runs occur.  
- Commit both the cleaned file and any documentation updates to the repository.

**Next step after cleaning:** Once the cleaned dataset has been accepted, run the separate EDA script (`nashville_housing_eda.py`) to generate visualizations and insights. EDA is intentionally kept outside this SOP.

---

## 5. Quality Acceptance Criteria
The cleaned dataset is considered acceptable when **all** of the following are true:

- No exact duplicate rows remain on the defined key fields.
- `SaleDateConverted` is in proper datetime format.
- `SoldAsVacant` contains only “Yes” or “No”.
- Address components have no leading/trailing whitespace.
- Missing `PropertyAddress` values have been populated where a matching `ParcelID` existed.
- All columns match the data types defined in the Data Dictionary.
- Final row count is documented and reasonable.
- Data Dictionary is up to date and matches the final column list and types.

---

## 6. Related Documents
- `data_dictionary.md` – Field definitions, data types, and business rules  
- `nashville_housing_python_cleaning.py` – Executable cleaning + type-enforcement script  
- `nashville_housing_eda.py` – Exploratory analysis and visualizations (run after this SOP is complete)  
- `README.md` – High-level overview and reproduction instructions  

---

## 7. Version History

| Version | Date       | Author           | Description of Changes                                      |
|---------|------------|------------------|-------------------------------------------------------------|
| 1.0     | 2026-04-28 | Mathyas Tilahun  | Initial SOP created after first full cleaning run           |
| 1.1     | 2026-10-23 | Mathyas Tilahun  | Updated acceptance criteria |

---

| Reviewer (if any) |                  |            |           |
