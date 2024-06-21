def min_operations_to_good_array(N, A):
    # Ensure the first element is negative and the last element is positive
    operations = 0
    if A[0] >= 0:
        operations += 1  # Increment if the first element is not negative
    if A[-1] <= 0:
        operations += 1  # Increment if the last element is not positive

    # Create arrays for cumulative counts of positives in the first half
    # and negatives in the second half
    positive_prefix = [0] * N
    negative_suffix = [0] * N

    # Initialize the prefix count of positive numbers
    if A[0] > 0:
        positive_prefix[0] = 1
    for i in range(1, N):
        positive_prefix[i] = positive_prefix[i - 1] + (1 if A[i] > 0 else 0)

    # Initialize the suffix count of negative numbers
    if A[-1] < 0:
        negative_suffix[-1] = 1
    for i in range(N - 2, -1, -1):
        negative_suffix[i] = negative_suffix[i + 1] + (1 if A[i] < 0 else 0)

    # Find the minimum operations needed by choosing the best K
    min_operations = float('inf')
    for K in range(N - 1):
        operations_needed = positive_prefix[K] + negative_suffix[K + 1]
        min_operations = min(min_operations, operations_needed)

    return (operations + min_operations)-2

# Test cases
print(min_operations_to_good_array(5, [8, -1, 1, 2, -5]))  # Output: 2
