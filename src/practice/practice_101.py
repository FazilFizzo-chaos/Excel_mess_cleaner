from src.cleaning.cleaning_pipeline import cleaning_pipeline
from src.exporters.file_exporter import export_file
from src.ingestion.loader import load_tabular_files

loaded_dataFrames = load_tabular_files("D:\\PythonProject\\input")
cleaned_dataframes = cleaning_pipeline(loaded_dataFrames)
export_file(cleaned_dataframes)

