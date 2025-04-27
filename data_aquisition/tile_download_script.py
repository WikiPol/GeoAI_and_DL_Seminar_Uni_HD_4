#Earth Engine Script to download .tif files 

import ee
import geemap
from PIL import Image
import os
import shutil

# Connection with a Google account and Google Cloud
ee.Authenticate()
ee.Initialize()

# Defined Region in a [lon, lat, lon, lat,] format
# The two Tamil Nadu bounding boxes used are defined here:
# #1 79.0, 12.0, 80.35, 13.35 
# #2. 78.0, 10.65, 79.35, 12.0 

region = ee.Geometry.Rectangle([77.0, 8.65, 78.35, 10.0])

# Satelite band selection to be included
common_bands = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B8A", "B9", "B11", "B12"]

# Sentinel-2 data specifications
collection = (
    ee.ImageCollection("COPERNICUS/S2_SR")
    .filterBounds(region)
    .filterDate("2023-01-01", "2023-12-31")
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 5))
    .select(common_bands)
)

# Creating image out of the median of the collection
image = collection.median().clip(region)

# Setting RGB visualization 
Map = geemap.Map()
Map.centerObject(region, 10)
Map.addLayer(image, {"min": 0, "max": 3000, "bands": ["B4", "B3", "B2"]}, "Sentinel-2 RGB")
Map

# Bounding box extraction out of the coordinates
coords = region.bounds().coordinates().getInfo()[0]
xmin, ymin = coords[0]
xmax, ymax = coords[2]

# Tile size
tile_width = 640
tile_height = 640

# Transformation into meters
region_width = (xmax - xmin) * 111320
region_height = (ymax - ymin) * 110574

# Tile splitting number generation
scale = 10  # 10m per pixel
num_tiles_x = int(region_width / (tile_width * scale))
num_tiles_y = int(region_height / (tile_height * scale))

# Tile generation
tiles = []
for i in range(num_tiles_x):
    for j in range(num_tiles_y):
        x1 = xmin + (xmax - xmin) * i / num_tiles_x
        y1 = ymin + (ymax - ymin) * j / num_tiles_y
        x2 = xmin + (xmax - xmin) * (i + 1) / num_tiles_x
        y2 = ymin + (ymax - ymin) * (j + 1) / num_tiles_y
        tile = ee.Geometry.Rectangle([x1, y1, x2, y2])
        tiles.append(tile)

total_tiles = len(tiles) 

#Progress information
for index, tile in enumerate(tiles):
  
    bbox = tile.bounds().coordinates().getInfo()[0]
    print(f" Tile {index+1}/{total_tiles} Bounding Box: {bbox}")

    # Progress
    percent_done = ((index + 1) / total_tiles) * 100
    print(f" Progress: {percent_done:.2f}%")

    #Earth Engine task generation and RGB band selection
    task = ee.batch.Export.image.toDrive(
        image=image.select(["B4", "B3", "B2"]),
        description=f"Tile_{index}",
        region=tile.getInfo()["coordinates"],
        scale=scale,
        fileFormat="GeoTIFF",
        maxPixels=1e9,
    )
    task.start()
    print(f" Started export: Tile_{index}")

print("All exports started")

