def kaprekar_constant(num):
    count = 0
    while num != 6174:
        # Convert number to a 4-digit string
        num_str = f"{num:04d}"
        
        # Sort digits in ascending and descending order
        asc_num = int("".join(sorted(num_str)))
        desc_num = int("".join(sorted(num_str, reverse=True)))
        
        # Calculate the difference
        num = desc_num - asc_num
        count += 1
        print(f"Iteration {count}: {desc_num} - {asc_num} = {num}")
    
    print(f"Kaprekar's Constant reached: {num}")

# Test
initial_number = 3462
kaprekar_constant(initial_number)
