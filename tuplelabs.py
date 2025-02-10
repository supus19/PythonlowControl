def sum_and_avg(f_tuple):
    # Unpacking tuple into variables
    x, y, z = f_tuple
    
    # Calculating sum and average
    total = sum(f_tuple)
    avg = total / len(f_tuple)
    
    # Returning the results as a tuple
    return (total, avg)

# Defining the tuple
my_tuple = (2, 6, 42)

# Calling the function and unpacking the returned tuple
(sum_result, avg_result) = sum_and_avg(my_tuple)

# Printing results
print((sum_result, avg_result))
print(type((sum_result, avg_result)))
print("Sum =", sum_result)
print("Sum is of type", type(sum_result))
print("Avg =", avg_result)
print("Avg is of type", type(avg_result))
