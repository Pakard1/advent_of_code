import re

def convert_string(input_str):
    # Define a dictionary mapping words to their numeric equivalents
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    # Define a regex pattern to match word sequences followed by digits
    pattern = r'\b(?:' + '|'.join(word_to_number.keys()) + r')(?=\d)'
    
    # Function to replace matched patterns with their numeric equivalents
    def replace_word_with_number(match):
        word = match.group(0)
        number = word_to_number.get(word, '')
        return number
    
    # Replace the matched patterns using the defined function
    result = re.sub(pattern, replace_word_with_number, input_str)

    return result
for input_str in input_strings:
    output_str = convert_string(input_str)
    print(f"Input: '{input_str}', Output: '{output_str}'")