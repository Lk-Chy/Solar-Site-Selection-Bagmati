import rasterio
import numpy as np

def reclassify_raster(input_path, output_path, bins, new_values):
    with rasterio.open(input_path) as src:
        data = src.read(1)
        profile = src.profile

    reclassified = np.digitize(data, bins=bins)
    reclassified = np.vectorize(lambda x: new_values[x - 1] if x > 0 else 0)(reclassified)

    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(reclassified, 1)

# Example usage for slope:
# bins = [10, 20, 30, 40] (slope breaks)
# values = [1, 2, 3, 4] (suitability ranks)
