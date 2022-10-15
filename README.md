# excel-comparison

we need 3 modules 
pip install [modulename]     #to install the modules

PANDAS - It is used to read the excelsheets and in this module  iloc() function to used to select any particular cell in the dataset.
NUMPY - Considering Dataset as a multi dimensional array
OPENPYXL - its supports new Excel files           #install it if any compatability issues with the parameter : engine 

Reason for the error : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html#           #refer using this URL 
                                                                                                                     go to parameter : engine 
The code compares two excel sheets ,if both are not equal displays NOT EXIST (as there is no difference) and vice versa.
