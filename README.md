# Building detection using Satellite imagery in South India
This project detects buildings on Sentinel 2 Satelite images and was trained using YOLOv8 and Roboflow. The model was evluated on satellite data covering parts of Tamil Nadu.
### Google Doc
 https://docs.google.com/document/d/1rwxETUBSJR45rE4G4-ERb-VCAmlVL5FeIzWFk-3Yh3U/edit?usp=sharing
### Overleaf 
 [https://www.overleaf.com/6567118731jkrgfyjkprfj#cb308f](https://www.overleaf.com/2887651616xwmcxyxshpwk#ae2f4a)
## Data Aquisition
To obtain the sentinel-2 data, [this](data/tile_download_script.py) Google Earth Engine script was created. In order to use it, one has to register to Google Cloud, create a project and use tile_download_script.py on https://code.earthengine.google.com. 
The data is made up of .tif files of the specified region.
## Data Preperation
Now the .tif files need to be split into smaller tiles in order to reduce the amount of labels on one tile and increase readability. The next step converts the .tif files into .jpg. The third does the automatic labeling. The last steps upload the labeled data to Roboflow. The Data Preparation can be done on this [Google Colab](data/tile_download_script.py) and requieres a connected Google account.
