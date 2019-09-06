import sqly

def run():

    files = sqly.available_csv_files
    #print(files)

    #sqly.inputfiles.generate_all_reports(files)
    #print('Files created')
    df = []
    for f in files:
        df.append(sqly.readcsv.import_csv(f))
    dt = sqly.combinedataframe.merge_dataframes(df,merge_type='inner')
    #report = sqly.inputfiles.readcsv.generate_report(dt)
    #print(dt)
    #print(report)
    #for f in files:
    #    sqly.readcsv.


if __name__ == "__main__":
    run()
