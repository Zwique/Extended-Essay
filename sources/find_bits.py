import math

# --- Find the number of bits ---

# Enter the ciphertext (or any large number) in decimal form
large_number_str = ''  # Example: '12345678901234567890'

if not large_number_str.strip():
    raise ValueError("Please enter a number in large_number_str")

# Convert the string to an integer
large_number = int(large_number_str)

# Calculate the number of bits required to represent the number
num_bits = large_number.bit_length()  # More precise than math.log2 for integers

print(f"Number of bits required: {num_bits}")