# Building detection using Satellite imagery in South India
This project detects buildings on Sentinel 2 Satelite images and was trained using YOLOv8 and Roboflow. The model was evluated on satellite data covering parts of Tamil Nadu.
### Google Doc
 https://docs.google.com/document/d/1rwxETUBSJR45rE4G4-ERb-VCAmlVL5FeIzWFk-3Yh3U/edit?usp=sharing
### Overleaf 
 [https://www.overleaf.com/6567118731jkrgfyjkprfj#cb308f](https://www.overleaf.com/2887651616xwmcxyxshpwk#ae2f4a)
## Data Aquisition
To obtain the sentinel-2 data, [this](GeoAI_and_DL_Seminar_Uni_HD_4/data_aquisition/tile_download_script.py) Google Earth Engine script was created. In order to use it, one has to register to Google Cloud, create a project and use the tile_download_script on https://code.earthengine.google.com. 
The data is made up of .tif files if the specified region.
