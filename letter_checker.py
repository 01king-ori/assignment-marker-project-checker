# Define a function that takes a string as an input and returns the number of words
def count_words(input_string):
  # Split the string by whitespace characters and store the result in a list
  words = input_string.split()
  # Return the length of the list, which is the number of words
  return len(words)

# Test the function with some examples
print(count_words("Hello world")) # Output: 2
print(count_words("This is a sentence with seven words")) # Output: 7
print(count_words("")) # Output: 0
