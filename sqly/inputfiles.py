import pandas as pd
import os
import pathlib as pl
from . import readcsv
import csv

in_path = pl.Path(os.getcwd()) / 'in'
out_path = pl.Path(os.getcwd()) / 'out'


def xlsx_to_csv(file_name):
    df = pd.read_excel(file_name)
    df.to_csv('{}.csv'.format(file_name), index=False)


def is_csv(file_name,convert=True):
    '''
    Check if has csv extension, returns boolean value
    Raise exception if file does not exist
    '''
    file_name = pl.Path(file_name)
    if not file_name.exists:
        raise Exception('No such file')
    if file_name.suffix.lower() == '.csv':
        return True
    else:
        if convert and (file_name.suffix.lower() == '.xlsx'):
            try:
                xlsx_to_csv(str(file_name))
                return True
            except Exception as e:
                print('Could not convert xlsx file to csv. Encountered {}'.format(e))
        return False


def get_in_files(in_path, csv_only=True, convert=True):
    '''Get all files inside the input folder'''
    path = in_path
    print('Reading files at {}'.format(path))
    files = os.listdir(path)
    names = []
    new_files = []
    for f in files:
        if csv_only:
            if is_csv(in_path / f, convert=convert):
                new_files.append(path / f)
                names.append((path / f).stem)
        else:
            new_files.append(path / f)
    files = new_files
    return files, names

def generate_report_names(filenames, out_path):
    for f in filenames:
        yield out_path / (pl.Path(f).stem + '.html')

def generate_all_reports(in_files, out_files=None):
    if out_files is None:
        out_files = generate_report_names(in_files, out_path)
    for fin, fout in zip(in_files, out_files):
        readcsv.csv_to_report_file(fin, fout)