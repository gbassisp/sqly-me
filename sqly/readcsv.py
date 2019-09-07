#import pandas as pd
from pandas import read_csv, DataFrame
import pandas_profiling as pp
import csv
from . import inputfiles
from .inputfiles import is_csv

in_path = inputfiles.in_path
out_path = inputfiles.out_path

def decode_file(file):
    with open(file,'r',encoding='utf-8',errors='ignore') as f:
        lines = f.readlines()
    lines = [bytes(line, 'utf-8').decode('ascii', 'ignore') for line in lines]
    #lines = u'\n'.join(lines).encode('utf-8').strip()
    with open(file, 'w') as f:
        f.writelines(lines)
    return None

def import_csv(in_file_name):
    '''Import a csv file and convert it to a pandas DataFrame'''
    decode_file(in_file_name)
    if not is_csv(in_file_name):
        raise Exception('Could not import {}: it is not a CSV file'.format(in_file_name))
    try:
        data = read_csv(in_file_name)
    except Exception as e:
        print('Could not import {}. Encountered {}'.format(in_file_name, e))
        data = DataFrame()
    print('Data read from {}'.format(in_file_name))
    return data

def generate_report(in_data, is_csv=False):
    '''Convert a csv file / dataframe into an HTML report'''
    if is_csv:
        in_data = import_csv(in_data)
    report = pp.ProfileReport(in_data)
    report.title = 'Your data profile'
    return report

def save_report(report, out_file_name=None, show=True):
    '''Save the report into a file'''
    if out_file_name is None:
        out_file_name = out_path / (report.get_unique_file_name())

    report.to_file(out_file_name, silent=(not show))
    return None

def csv_to_report_file(csv_file_name, report_file_name):
    report = generate_report(csv_file_name,is_csv=True)
    save_report(report, report_file_name)
    print('{} file converted into {}'.format(csv_file_name, report_file_name))
    return None

