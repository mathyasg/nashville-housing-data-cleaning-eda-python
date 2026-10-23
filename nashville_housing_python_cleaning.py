"""
Nashville Housing Data Cleaning Script
Author: Mathyas Tilahun
Purpose: Reproducible data cleaning + data-type enforcement pipeline
"""

import pandas as pd

print("🚀 Starting Nashville Housing Data Cleaning...\n")

# ==================== LOAD RAW DATA ====================
print("Loading raw Nashville Housing data...")
df = pd.read_excel('Nashville Housing Data for Data Cleaning.xlsx')

df_clean = df.copy()  # Make a copy so original data is not altered

print(f"Original rows: {len(df_clean):,}")

# 1. Convert SaleDate to proper datetime
df_clean['SaleDateConverted'] = pd.to_datetime(df_clean['SaleDate'], errors='coerce')

# 2. Populate missing PropertyAddress using ParcelID
missing = df_clean['PropertyAddress'].isnull()
if missing.any():
    address_map = (df_clean.dropna(subset=['PropertyAddress'])
                   .set_index('ParcelID')['PropertyAddress']
                   .to_dict())
    df_clean.loc[missing, 'PropertyAddress'] = df_clean.loc[missing, 'ParcelID'].map(address_map)

# 3. Split PropertyAddress
df_clean[['PropertySplitAddress', 'PropertySplitCity']] = (
    df_clean['PropertyAddress'].str.split(',', n=1, expand=True)
)
df_clean['PropertySplitAddress'] = df_clean['PropertySplitAddress'].str.strip()
df_clean['PropertySplitCity'] = df_clean['PropertySplitCity'].str.strip()

# 4. Split OwnerAddress
owner_parts = df_clean['OwnerAddress'].str.replace(',', '.').str.split('.', expand=True)
df_clean['OwnerSplitAddress'] = owner_parts[0].str.strip()
df_clean['OwnerSplitCity'] = owner_parts[1].str.strip()
df_clean['OwnerSplitState'] = owner_parts[2].str.strip()

# 5. Standardize SoldAsVacant
df_clean['SoldAsVacant'] = df_clean['SoldAsVacant'].replace({'Y': 'Yes', 'N': 'No'})

# 6. Remove duplicates
duplicate_cols = ['ParcelID', 'PropertyAddress', 'SalePrice', 'SaleDate', 'LegalReference']
df_clean = df_clean.drop_duplicates(subset=duplicate_cols, keep='first').reset_index(drop=True)

print(f"Cleaned rows after deduplication: {len(df_clean):,}")

# 7. Drop unused columns
columns_to_drop = ['OwnerAddress', 'TaxDistrict', 'PropertyAddress', 'SaleDate']
df_clean = df_clean.drop(columns=columns_to_drop, errors='ignore')

# ==================== 8. ENFORCE DATA TYPES ====================
print("\nEnforcing data types...")

# Integer columns (nullable Int64 so missing values stay as <NA>)
int_cols = [
    'UniqueID', 'SalePrice', 'LandValue', 'BuildingValue', 'TotalValue',
    'YearBuilt', 'Bedrooms', 'FullBath', 'HalfBath'
]
for col in int_cols:
    if col in df_clean.columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce').astype('Int64')

# Float columns
if 'Acreage' in df_clean.columns:
    df_clean['Acreage'] = pd.to_numeric(df_clean['Acreage'], errors='coerce').astype('float64')

# String / text columns
str_cols = [
    'ParcelID', 'LandUse', 'LegalReference', 'SoldAsVacant', 'OwnerName',
    'PropertySplitAddress', 'PropertySplitCity',
    'OwnerSplitAddress', 'OwnerSplitCity', 'OwnerSplitState'
]
for col in str_cols:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].astype('string')

# Date column (already created earlier)
df_clean['SaleDateConverted'] = pd.to_datetime(df_clean['SaleDateConverted'], errors='coerce')

print("Data types enforced successfully.")

# ==================== FINAL INFO ====================
print("\n" + "="*60)
print("✅ CLEANING + TYPE ENFORCEMENT COMPLETED SUCCESSFULLY")
print(f"Final shape: {df_clean.shape}")
print("\nFinal columns and dtypes:")
print(df_clean.dtypes)
print("="*60)

# ==================== SAVE ====================
df_clean.to_csv('housing_data_cleaned.csv', index=False)
print("\n✅ 'housing_data_cleaned.csv' created successfully with appropriate data types!")