# Function to read and display content of a text file line by line
def read_file_line_by_line(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Print each line
            print(line, end='')

# Call the function with the filename
read_file_line_by_line("ABC.txt")
