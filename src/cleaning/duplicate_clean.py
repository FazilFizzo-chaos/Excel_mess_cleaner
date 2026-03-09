

def clean_duplicate(df, config):
    print("STARTING CLEANING DUPLICATES............................................................................................")
    dup_config = config.get("duplicates", {})
    if dup_config.get("row_duplicates") == "remove":
        df = df.drop_duplicates()

    unique_columns = dup_config.get("unique_columns", [])
    if unique_columns:
        df = df.drop_duplicates(subset=unique_columns)
      # for unique_column in unique_columns:
      #     df = df.drop_duplicates(subset=unique_column)

    return df