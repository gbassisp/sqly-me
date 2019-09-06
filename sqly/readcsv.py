#import pandas as pd
from pandas import read_csv
import pandas_profiling as pp
import csv
from .inputfiles import is_csv


def import_csv(in_file_name):
    '''Import a csv file and convert it to a pandas DataFrame'''
    if not is_csv(in_file_name):
        raise Exception('Could not import {}: it is not a CSV file'.format(in_file_name))
    data = read_csv(in_file_name)
    print('Data read from {}'.format(in_file_name))
    return data

def generate_report(in_data, is_csv=False):
    '''Convert a csv file / dataframe into an HTML report'''
    if is_csv:
        in_data = import_csv(in_data)
    report = pp.ProfileReport(in_data)
    report.title = 'Your data profile'
    return report

def save_report(report, out_file_name):
    '''Save the report into a file'''
    report.to_file(out_file_name)
    return None

def csv_to_report_file(csv_file_name, report_file_name):
    report = generate_report(csv_file_name,is_csv=True)
    save_report(report, report_file_name)
    print('{} file converted into {}'.format(csv_file_name, report_file_name))
    return None

