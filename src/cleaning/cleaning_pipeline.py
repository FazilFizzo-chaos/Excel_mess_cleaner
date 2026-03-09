from src.cleaning.column_cleaner import normalize_columns
from src.cleaning.value_cleaner import trim_spaces
from src.cleaning.data_type_fix import fix_data_type
from src.ingestion.loader import load_tabular_files
from src.cleaning.apply_missing_strategy import apply_missing_strategy
from src.yaml_config_loader import config
from src.cleaning.duplicate_clean import clean_duplicate

def cleaning_pipeline(dataframes):
    for key, df in dataframes.items():
        print(f"cleaning {key} ...")
        dataframes[key] = normalize_columns(df)
        dataframes[key] = trim_spaces(df)
        dataframes[key] = fix_data_type(df)
        dataframes[key] = apply_missing_strategy(df, config)
        # dataframes[key] = clean_duplicate(df, config)

        dataframes[key] = df
    return dataframes

# dataFrames = load_tabular_files("D:\\PythonProject\\input")
# print(cleaning_pipeline(dataFrames))