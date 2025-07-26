import rasterio
import numpy as np

def weighted_overlay(raster_paths, weights, output_path):
    layers = []
    for path in raster_paths:
        with rasterio.open(path) as src:
            layers.append(src.read(1).astype(float))

    combined = np.zeros_like(layers[0], dtype=float)
    for i, layer in enumerate(layers):
        combined += weights[i] * layer

    with rasterio.open(raster_paths[0]) as src:
        profile = src.profile

    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(combined, 1)

# Example:
# weighted_overlay(["slope.tif", "ghi.tif", "aspect.tif"], [0.17, 0.28, 0.17], "suitability.tif")
