import sys #imprt the library sys to connect the notebook to linux

from table_reader.read_table import print_table #use the script read_table.py from the directory table_reader to import the "print_table" function from the module

headers=sys.argv[1:] #create a variable header to all command-line arguments sent to the script (sys.argv)
print_table(headers) #call the function print_table() (this script) and apply it to the variable headers
