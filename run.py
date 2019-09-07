import sqly

def run():

    files, names = sqly.available_csv_files, sqly.available_csv_file_names
    df = []
    merge_type = "inner" #choose between inner, outer, right, left
    for f in files:
        t = sqly.readcsv.import_csv(f)
        df.append(t)
    dt = sqly.combinedataframe.generate_reports(df,file_names=names,merge_type=merge_type,merged=False, show_reports=True)
    for d in dt:
        print('You have a new report')

if __name__ == "__main__":
    run()
