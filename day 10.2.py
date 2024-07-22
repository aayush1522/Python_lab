# Function to count and display the total number of words in a text file
def count_words_in_file(filename):
    # Initialize word count
    word_count = 0

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into words and count them
            words = line.split()
            word_count += len(words)

    # Display the total number of words
    print("Total number of words:", word_count)

# Call the function with the filename
count_words_in_file("ABC.txt")
