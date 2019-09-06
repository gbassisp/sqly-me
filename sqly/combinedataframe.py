




def combine_dataframes(dataframes):
    '''The dataframes parameter should be an iterable object of dataframes'''
    headers = []
    for df in dataframes:
        headers.append(list(df.columns))
    for h in headers:
        print(h)
    return headers