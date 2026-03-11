## Excel Mess Cleaner

# Excel Mess Cleaner is a Python-based data cleaning pipeline designed to transform messy tabular datasets into structured and analysis-ready data.

# The project focuses on automating common data cleaning tasks that frequently occur when working with Excel or CSV datasets collected from real-world sources.

# Features

- Automatic column name normalization
- Whitespace trimming for text columns
- Datatype standardization (dates, numbers, categories)
- Missing value handling
- Duplicate detection and removal
- Export to both CSV and Excel formats

# Why this project exists
Real-world datasets are often messy and inconsistent. Before analysis or machine learning can begin, datasets usually require significant cleaning.
Excel Mess Cleaner demonstrates how to build a reproducible data cleaning pipeline using Python and pandas.

# Technologies Used
- Python
- pandas
- openpyxl
- numpy

# Example Workflow
1. Load raw Excel/CSV files
2. Normalize column names
3. Trim text whitespace
4. Convert columns to correct datatypes
5. Handle missing values
6. Remove duplicates
7. Export clean datasets

# Example Use Case
Raw dataset:

Name| Visit Date| Age
Alice| 23/4/2023| 25
Bob| 04-23-2023| 30

After cleaning:

name| visit_date| age
Alice| 2023-04-23| 25
Bob| 2023-04-23| 30

Future Improvements

- Automatic datatype inference
- Data quality reporting
- Outlier detection
- CLI interface
- Dataset profiling
- Batch processing

License

MIT License
