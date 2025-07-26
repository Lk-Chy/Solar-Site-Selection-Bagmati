import numpy as np

def calculate_ahp_weights(matrix):
    col_sum = np.sum(matrix, axis=0)
    normalized = matrix / col_sum
    weights = np.mean(normalized, axis=1)
    return weights

def calculate_consistency(matrix, weights):
    n = matrix.shape[0]
    lambda_max = np.sum(np.dot(matrix, weights) / weights)
    ci = (lambda_max - n) / (n - 1)
    ri = {3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    cr = ci / ri.get(n, 1.49)
    return cr

# Example usage:
# matrix = np.array([...])
# weights = calculate_ahp_weights(matrix)
# cr = calculate_consistency(matrix, weights)
