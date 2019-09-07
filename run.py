import sqly

def run():

    files, names = sqly.available_csv_files, sqly.available_csv_file_names
    df = []
    for f in files:
        t = sqly.readcsv.import_csv(f)
        df.append(t)
    dt = sqly.combinedataframe.generate_reports(df,file_names=names,merge_type='outer',merged=False)
    for d in dt:
        print('You have a new report')

if __name__ == "__main__":
    run()
