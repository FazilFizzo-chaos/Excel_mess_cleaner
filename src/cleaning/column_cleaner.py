
def normalize_columns(df):
  df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w]", "", regex=True)
  return df
