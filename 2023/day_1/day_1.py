import re

def extract_digits_to_list_of_lists(file):
    """
    Extracts digits from each line of the file and returns a list of lists of integers.
    """
    digits_list = []    
    for line in file:
        # Removing whitespace and newlines from the ends
        line = line.strip()
        # Extract all digits using regex and convert to int
        digits = [int(char) for char in re.findall(r'\d', line)]
        digits_list.append(digits)
    
    return digits_list
def get_first_and_last_elements_concatenated(lst):
    """
    Concatenates the first and last elements of the list.
    If the list has less than 2 elements, concatenates the single element with itself.
    """
    if not lst:
        return 0  # No elements to concatenate
    # If there are only 1 element, repeat that element digit
    if len(lst) == 1:
        first, last = lst[0], lst[0]
    else:
        first, last = lst[0], lst[-1]

    concatenated_number = int(f"{first}{last}")
    return concatenated_number

def sum_concatenated_digits(file_path):
    digits_list = extract_digits_to_list_of_lists(file_path)
    total_sum = 0
    for digits in digits_list:
        concatenated_digits = get_first_and_last_elements_concatenated(digits)
        if concatenated_digits is not None:
            total_sum += concatenated_digits
    return total_sum

with open("input.txt", "r") as file:
    total = sum_concatenated_digits(file)
    print(total)
