def fibonacci_sequence(n):
    sequence = [0, 1]
    
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

sequence = fibonacci_sequence(num_terms)

print("Fibonacci sequence up to", num_terms, "terms:")
print(sequence)