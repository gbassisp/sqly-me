




def combine_dataframes(dataframes):
    headers = []
    for df in dataframes:
        headers.append(list(df.columns))
    for h in headers:
        print(h)
    return headers