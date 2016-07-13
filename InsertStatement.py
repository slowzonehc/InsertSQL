import numpy as np 
import csv
from sys import argv

# tests to see whether a value is a number
# will add '' around the value if needed
def is_number(s):
    try:
        float(s)
        return s
    except ValueError:
        return "'" + s + "'"

# removes speech marks from the dataset
# build: can have a replace dictionary
def clean_string(t):
	return t.replace('"','')

# call argv to call everything from the command line
script = argv

# ask the user for the variables
datebase_name = raw_input("DataBase Name:")
table_name = raw_input("Table Name:")
input_file = raw_input("Input File:")
output_file = raw_input("Output File:")

# load the input into an array
input_file = csv.reader(open(input_file))
header = input_file.next()

input_data = []
for row in input_file:
	input_data.append(row)

input_data = np.array(input_data)

# create an output document
output_file = open(output_file,"w")

# loop through each line / entry and add to the output
for row in input_data:
	output_line = "insert into " + datebase_name + "." + table_name + "("
	for item in row:
			output_line = output_line + is_number(clean_string(item)) + ","
	output_line = output_line[0:len(output_line)-1] + ");"
	output_file.write(str(output_line) + "\n")