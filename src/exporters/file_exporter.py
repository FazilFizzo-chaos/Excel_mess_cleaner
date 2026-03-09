import os, pandas

output_folder = "E:\\MESS_CLEANER"
os.makedirs(output_folder, exist_ok=True)
def export_file(dataframes):
    for name, df in dataframes.items():
        xlsx_path = os.path.join(output_folder, f"cleaned_{name}.xlsx")
        csv_path = os.path.join(output_folder, f"cleaned_{name}.csv")

        df_csv = df.copy()
        for col in df_csv.select_dtypes(include=['datetime']):
            df_csv[col] = df_csv[col].dt.strftime('%Y-%m-%d')


        df_csv.to_csv(csv_path, index=False)
        df.to_excel(xlsx_path, index=False)

# print("All cleaned files saved successfully")