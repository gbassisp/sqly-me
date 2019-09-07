import pandas as pd
from . import readcsv


def analyse_headers(dataframes):
    '''The dataframes parameter should be an iterable object of dataframes'''
    headers = []
    for df in dataframes:
        headers.append(list(df.columns))
    for h in headers:
        print(h)
    return headers


def merge_dataframes(dataframes, file_names=[], merge_type='inner'):
    
    t = len(dataframes)-1
    fn = len(file_names) - 1
    names_exist = True if t == fn else False
    while t >= 0: #remove empty data frames
        if dataframes[t].empty:
            print('Removing empty DataFrame')
            dataframes.pop(t)
            if names_exist:
                file_names.pop(t)
        t -= 1
    done = False
    name = ''
    while not done:
        merged = False #check if current df merges with any other df
        t = len(dataframes) - 1
        print('Initial number of dataframes is {}'.format(t+1))
        dt = dataframes[t]
        if names_exist:
            name = file_names[t]
        if t < 1: #one of the possibles way of finishing
            if not merged:
                print('Returning a report of unmerged data\nNo connection could be find at all')
            else:
                print('Returning a merged data report')
            break
        right  = t
        left = t
        while left > 0:
            left -= 1
            try:
                new_dt = pd.merge(dataframes[left],dt,how=merge_type)
                dataframes.pop(left)
                if names_exist:
                    name += ', {}'.format(file_names[left])
                    file_names.pop(left)
                    file_names[-1] = name
                merged = True
                dataframes[-1] = new_dt
                break
            except Exception as e:
                print('Could not merge with {}, moving on to next. Encountered {}'.format(name, e))
        else:
            print('{} could not merge with any other df'.format(right))
            if merged:
                print('Since it has merged, this is the final outcome. Other dfs are discarded')
                break
            else:
                print('Since it could not merge, it will be discarded and try with other dfs')
                dataframes.pop(right)



        '''print('Merging')
        try:
            new_dt = pd.merge(dataframes[t-1],dt,how=merge_type)
            dataframes.pop(t-1)
            if names_exist:
                name += ', {}'.format(file_names[t-1])
        except Exception as e:
            new_dt = dt
            print('Could not merge some data, encountered {}'.format(e))
            if names_exist:
                print('File {} did not merge with {}'.format(file_names[t-1], name))
                file_names.pop(t-1)
        dt = new_dt
        t -= 1'''

    return dt, name
    
def generate_report(dataframe, file_names=[], merge_type='inner', merged=True, auto_save=True):
    
    if not merged:
        dataframe, merged_files = merge_dataframes(dataframe, file_names, merge_type)
    report = readcsv.generate_report(dataframe)
    report.title = merged_files
    print('Report generated with {} files'.format(report.title))
    if auto_save:
        readcsv.save_report(report)
    return report