def input_vector(n):
    vector = []
    for i in range(n):
        while True:
            try:
                value = float(input(f"Enter the {i+1}-th element of the vector: "))
                vector.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return vector

def vector_addition(u, v, a, b):
    if len(u) != len(v):
        raise ValueError("Vector dimensions do not match.")
    
    result = []
    for i in range(len(u)):
        result.append(a * u[i] + b * v[i])
    
    return result

def dot_product(u, v):
    if len(u) != len(v):
        raise ValueError("Vector dimensions do not match.")
    
    result = sum(u[i] * v[i] for i in range(len(u)))
    return result

# Input vectors u and v
n = int(input("Enter the dimension of the vectors (n): "))
u = input_vector(n)
v = input_vector(n)

# Enter values for a and b
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

# Calculate au + bv
result_vector = vector_addition(u, v, a, b)
print(f"{a}*u + {b}*v = {result_vector}")

# Calculate the dot product of u and v
dot_product_result = dot_product(u, v)
print(f"Dot Product of u and v: {dot_product_result}")
