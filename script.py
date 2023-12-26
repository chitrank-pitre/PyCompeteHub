import sys

# Specify the paths for input and output files
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# Open the input file in read mode
with open(input_file_path, 'r') as input_file:
    # Redirect standard input to read from the input file
    sys.stdin = input_file

    # Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # Redirect standard output to write to the output file
        sys.stdout = output_file

        # Code starts below
        # Read input and write output as needed
        
        a = input() #taking input
        print(a)

# Reset standard input and output to their default values
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__
