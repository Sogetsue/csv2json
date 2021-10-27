This is a simply python module to convert any csv file into key:value pairs using the headers as keys and cell values to complete the pair

The module must be imported like -

from csv2json import csvtojson

Use the module to convert the file like so -

csvtojson("C:\\Path\\To\\CSV.csv").convert_2_json()

This will produce no ouput at the command line, but will create a .txt file in json format within the same directory as the csv file you specified
