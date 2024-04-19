# ML Model Development Pipeline
## **Feature Engineering**

Welcome to the feature_engineering folder in your ML model development pipeline. 

## **Purpose**: This folder is where the engineering of derived features from the preprocessed data takes place. The goal is to extract valuable information from the data to enhance the model's predictive performance.

## **How to Use** :
1. **Import and Run the Script**: Open the 'feature_engineering.py' script using a Python interpreter. 



```python
python feature_engineering.py
```




2. **Explore Derived Features**: The script will create new features and save the updated dataset. Run the script to inspect the DataFrame containing the engineered features. Understand the transformations and feature selections made here.

## **Contents**
- **'feature_engineering.py'**: The main Python script for feature engineering. This script should:
    - Import the preprocessed data.
    - Perform feature engineering tasks such as:
        - creating lag features
        - scaling features
        - extracting time series features
        - engineering categorical features
        - selecting important features based on domain knowledge or statistical significance.
    - Save the dataset with engineered features to be used in subsequent steps.
- **'README.md'**: This file, providing an overview of the feature engineering module and detailing the derived features.