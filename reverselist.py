def reverse_list(x):
    reverse_x = []
    for i in range (len(x) - 1, -1, -1):
        reverse_x.append(x[i])
    
    return reverse_x

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)
