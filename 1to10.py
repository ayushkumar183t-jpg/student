# 1. Creates a list of numbers from 1 to 10
original_list = list(range(1, 11))

# 2. Extracts the first five elements from the list using list slicing
extracted_list = original_list[:5]

# 3. Reverses these extracted elements using step slicing [::-1]
reversed_list = extracted_list[::-1]

# 4. Prints the original, extracted, and reversed lists
print(f"Original list: {original_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")