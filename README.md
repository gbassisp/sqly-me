# sqly-me
 Python module for solving GovHack 2019 challenges

Before using this module, read how it works here.

## Structure:
This module contains functions related to importing data, parsing data and returning its outcome. It follows a standard Python package structure, with a setup.py for installation and the functionallity inside the source code folders.  
However, there are two important remarks:  
 1 - there is a script file named run.py, which is pretty self-explanatory. It is used on the video to easily run an example of script using this library. Remeber, the autorun file is not the project, it is a use case of the module.  
 2 - there are two extra folders inside the module directory. They are used for IO operations with files and they are non-surprisingly named "in" and "out". Again, the module can be used to do IO operations with any other folder the user opts to, but this is the standard for the showcase.  
 
## Use:
 The autorun file uses the module on a very simple way:  
  1 - It reads all files into the "in" folder. Excel files are converted into .csv files and all .csv files are return as input files to the module  
  2 - The module import all files into dataframes  
  3 - The module checks all combinations of "greedy" merge*  
  4 - The module returns, for each "greedy" merge, one sqlite database file and one HTML report  
  5 - These outputs are saved into the "out" folder and the report(s) spawn on the user browser (not mandatory, depends a the boolean argument passed into the module)  
  
## Notes:
 The autorun file should be enough to test the usage, keeping in mind that the "in" and "out" folders are set to default. The user should put their files into the "in" folder and run the file  
 The module does not check for the meaning of the data. It assumes the user has passed data which is somehow related to each other. The module seeks connectivity and correlation. If the user provides weather forecasting data and furniture pricing, with some common variable (such as date), the module might find a correlation between a sunny day and chair sales. It is the user responsibility to make good use of it.  
 
 
 *all combinations of "greedy" merge means it looks for the longest sequences of files it can merge. Once it finds the longest sequence, it removes those files from the list and moves on on finding new combinations with the remaining files. The merge uses the standard types of inner, outer, left and right merge.
