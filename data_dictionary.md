# Data Dictionary  
**Dataset:** Nashville Housing (Cleaned)  
**Cleaned File:** `housing_data_cleaned.csv`  
**Raw / Original File:** `Nashville Housing Data for Data Cleaning.xlsx` (56,477 records)  
**Time Period:** 2013 – 2016  
**Last Updated:** 2026-10-23  
**Owner:** Mathyas Tilahun  
**Version:** 1.1

---

## Purpose
This data dictionary defines every field in the cleaned Nashville Housing dataset. It serves as the single source of truth for field definitions, data types, allowed values, business rules, and cleaning decisions so that analysts, reviewers, and future users interpret the data consistently.

---

## Field Definitions

| Field Name              | Description                                      | Data Type          | Allowed Values / Format                  | Source / Origin                  | Example Value          | Notes / Business Rules                                                                 | Owner          | Last Updated |
|-------------------------|--------------------------------------------------|--------------------|------------------------------------------|----------------------------------|------------------------|----------------------------------------------------------------------------------------|----------------|--------------|
| UniqueID                | Unique identifier for each property record       | Integer (Int64)    | Positive integer                         | Original dataset                 | 2045                   | Primary key; no nulls expected                                                         | Mathyas Tilahun| 2026-10-23   |
| ParcelID                | County parcel identifier                         | String             | Alphanumeric                             | Original dataset                 | 007 00 0 038.00        | Used to populate missing PropertyAddress; standardized spacing                         | Mathyas Tilahun| 2026-10-23   |
| LandUse                 | Type of land use / property classification       | String             | Controlled vocabulary (e.g. SINGLE FAMILY, RESIDENTIAL CONDO, VACANT RESIDENTIAL LAND, etc.) | Original dataset | SINGLE FAMILY          | Values retained as provided                                                            | Mathyas Tilahun| 2026-10-23   |
| SalePrice               | Sale price of the property in USD                | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 240000                 | Converted to nullable integer                                                          | Mathyas Tilahun| 2026-10-23   |
| LegalReference          | Legal reference number for the sale              | String             | Alphanumeric                             | Original dataset                 | 20130412-0036474       | Used in duplicate detection                                                            | Mathyas Tilahun| 2026-10-23   |
| SoldAsVacant            | Indicates whether the property was sold as vacant or occupied | String | Yes / No                                 | Original (Y/N) → Standardized    | No                     | Standardized from Y/N to Yes/No                                                        | Mathyas Tilahun| 2026-10-23   |
| OwnerName               | Name of the property owner                       | String             | Free text                                | Original dataset                 | FRAZIER, CYRENTHA LYNETTE | Retained as-is; may contain nulls                                                   | Mathyas Tilahun| 2026-10-23   |
| Acreage                 | Size of the property in acres                    | Float (float64)    | ≥ 0                                      | Original dataset                 | 2.3                    | Converted to float; nulls retained                                                     | Mathyas Tilahun| 2026-10-23   |
| LandValue               | Assessed value of the land                       | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 50000                  | Converted to nullable integer                                                          | Mathyas Tilahun| 2026-10-23   |
| BuildingValue           | Assessed value of the building/improvements      | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 168200                 | Converted to nullable integer                                                          | Mathyas Tilahun| 2026-10-23   |
| TotalValue              | Total assessed value (Land + Building)           | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 235700                 | Converted to nullable integer                                                          | Mathyas Tilahun| 2026-10-23   |
| YearBuilt               | Year the property was constructed                | Integer (Int64)    | Approx. 1800 – 2016                      | Original dataset                 | 1986                   | Converted to nullable integer; nulls retained where missing                            | Mathyas Tilahun| 2026-10-23   |
| Bedrooms                | Number of bedrooms                               | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 3                      | Converted to nullable integer; nulls retained                                          | Mathyas Tilahun| 2026-10-23   |
| FullBath                | Number of full bathrooms                         | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 3                      | Converted to nullable integer; nulls retained                                          | Mathyas Tilahun| 2026-10-23   |
| HalfBath                | Number of half bathrooms                         | Integer (Int64)    | ≥ 0                                      | Original dataset                 | 0                      | Converted to nullable integer; nulls retained                                          | Mathyas Tilahun| 2026-10-23   |
| SaleDateConverted       | Sale date in proper datetime format              | DateTime           | YYYY-MM-DD                               | Derived from SaleDate            | 2013-04-09             | Converted from Excel serial / original SaleDate; original SaleDate dropped             | Mathyas Tilahun| 2026-10-23   |
| PropertySplitAddress    | Street address component of PropertyAddress      | String             | Free text                                | Derived from PropertyAddress     | 1808  FOX CHASE DR     | Created by splitting PropertyAddress on comma; whitespace stripped                     | Mathyas Tilahun| 2026-10-23   |
| PropertySplitCity       | City component of PropertyAddress                | String             | Free text (city name)                    | Derived from PropertyAddress     | GOODLETTSVILLE         | Created by splitting PropertyAddress on comma; whitespace stripped                     | Mathyas Tilahun| 2026-10-23   |
| OwnerSplitAddress       | Street address component of OwnerAddress         | String             | Free text                                | Derived from OwnerAddress        | 1808  FOX CHASE DR     | Created by splitting OwnerAddress; whitespace stripped                                 | Mathyas Tilahun| 2026-10-23   |
| OwnerSplitCity          | City component of OwnerAddress                   | String             | Free text (city name)                    | Derived from OwnerAddress        | GOODLETTSVILLE         | Created by splitting OwnerAddress; whitespace stripped                                 | Mathyas Tilahun| 2026-10-23   |
| OwnerSplitState         | State component of OwnerAddress                  | String             | Two-letter state code (e.g. TN)          | Derived from OwnerAddress        | TN                     | Created by splitting OwnerAddress; whitespace stripped                                 | Mathyas Tilahun| 2026-10-23   |

---

## Columns Removed During Cleaning
| Original Column   | Reason for Removal                                      |
|-------------------|---------------------------------------------------------|
| SaleDate          | Replaced by `SaleDateConverted` (proper datetime)       |
| PropertyAddress   | Split into `PropertySplitAddress` and `PropertySplitCity` |
| OwnerAddress      | Split into `OwnerSplitAddress`, `OwnerSplitCity`, `OwnerSplitState` |
| TaxDistrict       | Not required for analysis; dropped to reduce noise      |

---

## Data Type Enforcement
After structural cleaning, all columns are explicitly cast to the data types defined in this dictionary:
- Integer columns use pandas nullable `Int64` so missing values are preserved as `<NA>`.
- Text columns use the `string` dtype.
- `Acreage` is cast to `float64`.
- `SaleDateConverted` is stored as datetime.

---

## Overall Data Quality Rules Applied
- Missing `PropertyAddress` values were populated using matching `ParcelID` records where available.
- Duplicate records were removed based on the combination of: ParcelID, PropertyAddress, SalePrice, SaleDate, LegalReference (first occurrence kept).
- `SoldAsVacant` standardized to consistent “Yes” / “No” values.
- All address components stripped of leading/trailing whitespace.
- Final cleaned dataset contains no exact duplicate rows on the key fields listed above.
- Data types enforced to match this dictionary.

---

## Change Log
| Version | Date       | Author           | Changes                                                                 |
|---------|------------|------------------|-------------------------------------------------------------------------|
| 1.0     | 2026-04-28 | Mathyas Tilahun  | Initial data dictionary created after cleaning                          |
| 1.1     | 2026-10-23 | Mathyas Tilahun  | Updated header labels for clarity; refreshed notes |
