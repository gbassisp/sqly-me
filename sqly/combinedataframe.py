import pandas as pd




def analyse_headers(dataframes):
    '''The dataframes parameter should be an iterable object of dataframes'''
    headers = []
    for df in dataframes:
        headers.append(list(df.columns))
    for h in headers:
        print(h)
    return headers


def merge_dataframes(dataframes, headers=None, merge_type='inner'):
    
    t = len(dataframes)-1
    dt = dataframes[t]
    while t > 0:
        print('Merging')
        dt = pd.merge(dataframes[t-1],dt,how=merge_type)
        t -= 1

    return dt
    
