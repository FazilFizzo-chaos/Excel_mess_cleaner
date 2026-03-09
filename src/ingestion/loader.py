from pathlib import Path
import pandas as pd
# from smart_xlsx_loader import smart_xlsx_loader
# from smart_xls_loader import smart_xls_loader
# from smart_csv_loader import smart_csv_loader
from src.ingestion.smart_xlsx_loader import smart_xlsx_loader
from src.ingestion.smart_csv_loader import smart_csv_loader
from src.ingestion.smart_xls_loader import smart_xls_loader
from src.utils.quick_overview import quick_overview

def load_tabular_files(path: str):
   dataframes = {}
   if Path(path).is_dir():
     for file in Path(path).rglob("*"):
      try:
        if file.suffix.lower() == ".csv":
                df = smart_csv_loader(file)
        elif file.suffix.lower() == ".xlsx":
                df = smart_xlsx_loader(file)
        elif file.suffix.lower() == ".xls":
                df = smart_xls_loader(file)
        else:
            continue

        dataframes[file.name] = df

      except Exception as e:
         print(f"Failed to load {file}:  {e}")
   # for key, value in dataframes.items():
   #     # print(type(value))
   #     quick_overview(value)
   #
   return dataframes
   # preview = []
# load_tabular_files("D:\\PythonProject\\input")
# load_tabular_files("E:\\MESS_CLEANER")
# load_tabular_files("E:\\MESS_CORRECT")