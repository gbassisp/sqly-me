import pandas as pd
from . import readcsv, tosql


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
    remaining_names = []
    merged = False #check if current df merges with any other df
    remaining_dfs = dataframes[:]
    while not done:
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
                    remaining_names = file_names[:-1]
                merged = True
                print('Merging something')
                dataframes[-1] = new_dt
                remaining_dfs = dataframes[:-1]
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
                if names_exist:
                    file_names.pop(right)

    return dt, name, remaining_dfs, remaining_names

def generate_reports(dataframe, file_names=[], merge_type='inner', merged=True, auto_save=True, show_reports=True):
    
    if not merged:
        merges, names = [], []
        unmerged_dataframes, unmerged_names = dataframe[:], file_names[:]
        while len(unmerged_dataframes) > 1:
            dataframe, merged_files, unmerged_dataframes, unmerged_names = merge_dataframes(unmerged_dataframes, unmerged_names, merge_type)
            merges.append(dataframe)
            names.append(merged_files)
        dataframes = merges
    for dataframe, merged_files in zip(dataframes, names):
        try:
            report = readcsv.generate_report(dataframe)
            report.title = 'Data from: {}'.format(merged_files)
            print('Report generated with {} files'.format(merged_files))
            if auto_save:
                name = readcsv.save_report(report,show=show_reports)
                tosql.create_db(name, dataframe, 'test')
                
        except Exception as e:
            print("Could not generate report. Encountered {}".format(e))
            report = None
        yield report

