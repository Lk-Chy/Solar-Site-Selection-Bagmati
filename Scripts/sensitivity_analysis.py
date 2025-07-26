def vary_weight(weights, index, change_percent):
    modified = weights.copy()
    delta = weights[index] * change_percent
    modified[index] += delta
    # Reduce other weights proportionally
    others_sum = sum(modified) - modified[index]
    scale = (1 - modified[index]) / others_sum
    for i in range(len(modified)):
        if i != index:
            modified[i] *= scale
    return modified
