import pandas as pd

def apply_missing_strategy(df, config):
    print(f"MISSING STRATEGY STARTING...........................................................................................")
    for col, rules in config["columns"].items():
        if col not in df.columns:
            continue

        strategy = rules.get("missing_strategy")

        if strategy == "fill":
            values = rules.get("fill_value")
            df[col] = df[col].fillna(values)
        elif strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        elif strategy == "drop":
            df = df.dropna(subset=[col])
        elif strategy == "keep":
            pass

    return df