
def quick_overview(df):
    print(f"\nShape: {df.shape}")
    print(f"\nData Info: ")
    df.info()
    print(f"\nSample Rows: ")
    print(f"{df.head(11)}")
    # print(f"\nStatistics: ")
    # print(f"{df.describe(include='all')}")