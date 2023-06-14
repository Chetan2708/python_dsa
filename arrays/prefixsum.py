# Define a function to calculate prefix sums
def prefix(l,n):
    prefix_sum[0]=l[0]
    for i in range(1, len(l)):
        prefix_sum[i] = prefix_sum[i-1] + l[i]

# Define a function to get the sum of a range using prefix sums
def getsum(prefix_sum, le, r):
    if le != 0:
        return prefix_sum[r] - prefix_sum[le-1]
    else:
        return prefix_sum[r]

# Create an empty list
l = []

# Get the value of n from the user
n = int(input("Enter the value of n: "))

# Populate the list with user input values
for i in range(n):
    f = int(input("Enter a number: "))
    l.append(f)

# Get the values of le and r from the user
le = int(input("Enter the value of le: "))
r = int(input("Enter the value of r: "))

# Create a prefix sum list of zeros
prefix_sum = n * [0]

# Calculate the prefix sums
prefix(l, n)

# Print the sum of the range using the prefix sums
print(getsum(prefix_sum, le, r))
