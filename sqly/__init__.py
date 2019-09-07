'''
The sqly module does not initialize by itself
It only lists the available input CSV files

It is the user duty to tell the module to convert the files
'''

greeting_message = '''

Welcome to the SqlyMe project

This project is an open source (under the Apache License, see the docs) solution to the GovHack event, 
held in South Australia 2019, but it should be useful to use in other cases

I hope it is good enough...

Cheers,
Guilherme Bassi Pontes

'''.lstrip()
print(greeting_message)


#Start here

from . import readcsv, inputfiles, combinedataframe
in_path = inputfiles.in_path
out_path = inputfiles.out_path

available_csv_files, available_csv_file_names = inputfiles.get_in_files(in_path, csv_only=True)


