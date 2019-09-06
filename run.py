import sqly

def run():

    files = sqly.available_csv_files
    #print(files)

    #sqly.inputfiles.generate_all_reports(files)
    #print('Files created')
    df = []
    for f in files:
        df.append(sqly.readcsv.import_csv(f))
    print(sqly.readcsv.combine_dataframes(df))

    #for f in files:
    #    sqly.readcsv.


if __name__ == "__main__":
    run()